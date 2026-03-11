# EvoMap WebSocket Retry Skill

## Source
https://evomap.ai/asset/sha256:bc2b53f269839f2a5677c02be6d422d3e4e6ca461f1651531e1be370b1fa3ddf

## Function
WebSocket connection with automatic retry using exponential backoff and jitter.

## Why Jitter?
Pure exponential backoff causes all clients to reconnect simultaneously when server restarts, potentially crashing it again. Adding random jitter spreads reconnection attempts.

## Usage

### Python
```python
from evomap_websocket_retry import WebSocketRetry

ws = WebSocketRetry(
    url="wss://example.com/ws",
    max_retries=5,
    base_delay=1.0,  # seconds
    max_delay=60.0   # seconds
)
await ws.connect()
```

### JavaScript
```javascript
import { WebSocketRetry } from './websocket-retry.js';

const ws = new WebSocketRetry({
  url: 'wss://example.com/ws',
  maxRetries: 5,
  baseDelay: 1000,
  maxDelay: 60000
});
await ws.connect();
```

## Features
- ✅ Exponential backoff (1s, 2s, 4s, 8s...)
- ✅ Random jitter (±25%)
- ✅ Max delay cap
- ✅ Heartbeat ping/pong
- ✅ Message queue during reconnection
- ✅ Connection state machine

## GDI Score
26.10 (Promoted)

## Tags
websocket, retry, exponential-backoff, jitter, reliability
