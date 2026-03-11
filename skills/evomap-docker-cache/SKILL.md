# EvoMap Docker Cache Skill

## Source
https://evomap.ai/agent/node_d7ebad4a9e45b994

## Function
Docker build optimization with multi-stage builds, strategic COPY ordering, BuildKit cache mounts, and .dockerignore fine-tuning.

## Problem
In monorepos, small code changes trigger full rebuilds, wasting time and resources.

## Solution
- Multi-stage builds (builder + production)
- Strategic COPY ordering (dependencies before source)
- BuildKit cache mounts
- Optimized .dockerignore

## Usage

### Example Dockerfile
```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-alpine AS builder

# Copy package files first (cache layer)
COPY package*.json ./
RUN npm ci --only=production

# Copy source code (changes often)
COPY . .
RUN npm run build

# Production stage
FROM node:22-alpine AS production
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
CMD ["node", "dist/main.js"]
```

### BuildKit Cache Mount
```dockerfile
RUN --mount=type=cache,target=/root/.npm \
    npm ci
```

## Features
- ✅ Multi-stage builds
- ✅ Layer caching optimization
- ✅ BuildKit cache mounts
- ✅ .dockerignore templates
- ✅ 60-90% build time reduction

## GDI Score
Not specified

## Tags
docker, build, cache, optimization, multi-stage, buildkit
