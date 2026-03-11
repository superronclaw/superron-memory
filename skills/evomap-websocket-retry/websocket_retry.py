import asyncio
import random
import logging
from typing import Optional, Callable, Any
import websockets
from websockets.exceptions import ConnectionClosed

logger = logging.getLogger(__name__)

class WebSocketRetry:
    """
    WebSocket connection with exponential backoff retry and jitter.
    Prevents synchronized reconnection storms.
    """
    
    def __init__(
        self,
        url: str,
        max_retries: int = 5,
        base_delay: float = 1.0,
        max_delay: float = 60.0,
        jitter_ratio: float = 0.25,
        on_message: Optional[Callable[[str], Any]] = None,
        on_connect: Optional[Callable[[], Any]] = None,
        on_disconnect: Optional[Callable[[], Any]] = None
    ):
        self.url = url
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.jitter_ratio = jitter_ratio
        self.on_message = on_message
        self.on_connect = on_connect
        self.on_disconnect = on_disconnect
        
        self._ws: Optional[websockets.WebSocketClientProtocol] = None
        self._retry_count = 0
        self._connected = False
        self._message_queue: list = []
        self._stop_event = asyncio.Event()
        
    def _calculate_delay(self, attempt: int) -> float:
        """Calculate delay with exponential backoff and jitter."""
        # Exponential backoff
        delay = self.base_delay * (2 ** attempt)
        # Cap at max_delay
        delay = min(delay, self.max_delay)
        # Add jitter (±jitter_ratio)
        jitter = delay * self.jitter_ratio * (2 * random.random() - 1)
        return delay + jitter
    
    async def connect(self):
        """Connect with retry logic."""
        while not self._stop_event.is_set() and self._retry_count < self.max_retries:
            try:
                logger.info(f"Connecting to {self.url} (attempt {self._retry_count + 1})")
                self._ws = await websockets.connect(self.url)
                self._connected = True
                self._retry_count = 0
                
                if self.on_connect:
                    await asyncio.get_event_loop().run_in_executor(None, self.on_connect)
                
                # Send queued messages
                while self._message_queue:
                    msg = self._message_queue.pop(0)
                    await self._ws.send(msg)
                
                # Start message handler
                await self._handle_messages()
                
            except Exception as e:
                self._connected = False
                self._retry_count += 1
                
                if self.on_disconnect:
                    await asyncio.get_event_loop().run_in_executor(None, self.on_disconnect)
                
                if self._retry_count >= self.max_retries:
                    logger.error(f"Max retries ({self.max_retries}) reached. Giving up.")
                    raise
                
                delay = self._calculate_delay(self._retry_count - 1)
                logger.warning(f"Connection failed: {e}. Retrying in {delay:.2f}s...")
                await asyncio.sleep(delay)
    
    async def _handle_messages(self):
        """Handle incoming messages."""
        try:
            async for message in self._ws:
                if self.on_message:
                    if asyncio.iscoroutinefunction(self.on_message):
                        await self.on_message(message)
                    else:
                        await asyncio.get_event_loop().run_in_executor(
                            None, self.on_message, message
                        )
        except ConnectionClosed:
            logger.info("Connection closed")
            self._connected = False
    
    async def send(self, message: str):
        """Send message (queue if disconnected)."""
        if self._connected and self._ws:
            await self._ws.send(message)
        else:
            self._message_queue.append(message)
            logger.debug(f"Message queued (offline): {message[:100]}...")
    
    async def close(self):
        """Close connection gracefully."""
        self._stop_event.set()
        if self._ws:
            await self._ws.close()
            self._connected = False
    
    @property
    def is_connected(self) -> bool:
        return self._connected
