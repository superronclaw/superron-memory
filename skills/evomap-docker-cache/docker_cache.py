#!/usr/bin/env python3
"""
Docker build optimization utilities
"""

import os
import re
from pathlib import Path
from typing import List, Set

class DockerOptimizer:
    """Optimize Docker builds for better layer caching."""
    
    # Templates for common project types
    DOCKERIGNORE_TEMPLATES = {
        "node": """
# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.npm
.yarn-integrity
.pnp.*

# Build outputs
dist/
build/
coverage/

# Environment
.env
.env.local
.env.*.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Git
.git/
.gitignore

# Testing
*.test.js
*.spec.js
__tests__/
test/
tests/

# Documentation
*.md
docs/
""",
        "python": """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# Testing
.tox/
.pytest_cache/
.coverage
htmlcov/

# IDE
.vscode/
.idea/
*.swp

# Git
.git/
.gitignore

# Documentation
*.md
docs/
""",
        "generic": """
# Git
.git/
.gitignore
.gitattributes

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Documentation
*.md
README*
LICENSE*
CHANGELOG*
docs/

# CI/CD
.github/
.gitlab-ci.yml
.travis.yml
azure-pipelines.yml
Jenkinsfile

# Docker
Dockerfile*
docker-compose*.yml
.dockerignore
"""
    }
    
    @staticmethod
    def generate_dockerignore(project_type: str = "generic", extra_patterns: List[str] = None) -> str:
        """Generate optimized .dockerignore file."""
        template = DockerOptimizer.DOCKERIGNORE_TEMPLATES.get(
            project_type, 
            DockerOptimizer.DOCKERIGNORE_TEMPLATES["generic"]
        )
        
        if extra_patterns:
            template += "\n# Custom\n" + "\n".join(extra_patterns)
        
        return template.strip()
    
    @staticmethod
    def analyze_dockerfile(dockerfile_path: str) -> dict:
        """Analyze Dockerfile for optimization opportunities."""
        with open(dockerfile_path, 'r') as f:
            content = f.read()
        
        issues = []
        recommendations = []
        
        # Check for multi-stage builds
        if 'FROM' in content and content.count('FROM') < 2:
            issues.append("No multi-stage build detected")
            recommendations.append("Use multi-stage builds to reduce final image size")
        
        # Check for COPY before RUN
        copy_pattern = r'COPY.*\nRUN.*(apt-get|npm|pip|yarn)'
        if re.search(copy_pattern, content):
            issues.append("Source code may be copied before dependency installation")
            recommendations.append("Copy package files first, install deps, then copy source")
        
        # Check for BuildKit features
        if '--mount=type=cache' not in content:
            recommendations.append("Use BuildKit cache mounts for package managers")
        
        # Check for .dockerignore
        dockerfile_dir = Path(dockerfile_path).parent
        dockerignore = dockerfile_dir / '.dockerignore'
        if not dockerignore.exists():
            issues.append("No .dockerignore file found")
            recommendations.append("Create .dockerignore to reduce build context")
        
        return {
            "issues": issues,
            "recommendations": recommendations,
            "stages": content.count('FROM'),
            "has_buildkit": '--mount=type=cache' in content
        }
    
    @staticmethod
    def optimize_node_dockerfile(package_json_path: str = "package.json") -> str:
        """Generate optimized Dockerfile for Node.js projects."""
        return '''# syntax=docker/dockerfile:1
FROM node:22-alpine AS builder

WORKDIR /app

# Copy package files first (cache layer)
COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm \
    npm ci --only=production

# Copy source and build
COPY . .
RUN npm run build

# Production stage
FROM node:22-alpine AS production
WORKDIR /app

# Copy built assets
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package*.json ./

USER node
EXPOSE 3000

CMD ["node", "dist/main.js"]
'''
    
    @staticmethod
    def optimize_python_dockerfile(requirements_path: str = "requirements.txt") -> str:
        """Generate optimized Dockerfile for Python projects."""
        return '''# syntax=docker/dockerfile:1
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (cache layer)
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-slim AS production
WORKDIR /app

# Copy installed packages
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY . .

USER nobody
EXPOSE 8000

CMD ["python", "-m", "app"]
'''


def create_optimized_docker_project(project_type: str, target_dir: str = "."):
    """Create optimized Docker configuration for a project."""
    target = Path(target_dir)
    optimizer = DockerOptimizer()
    
    # Create .dockerignore
    dockerignore_content = optimizer.generate_dockerignore(project_type)
    (target / '.dockerignore').write_text(dockerignore_content)
    
    # Create Dockerfile
    if project_type == "node":
        dockerfile_content = optimizer.optimize_node_dockerfile()
    elif project_type == "python":
        dockerfile_content = optimizer.optimize_python_dockerfile()
    else:
        dockerfile_content = "# Generic Dockerfile\nFROM alpine:latest\n"
    
    (target / 'Dockerfile.optimized').write_text(dockerfile_content)
    
    print(f"✅ Created optimized Docker files in {target_dir}")
    print(f"   - .dockerignore ({project_type} template)")
    print(f"   - Dockerfile.optimized")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        create_optimized_docker_project(sys.argv[1])
    else:
        print("Usage: python docker_cache.py [node|python|generic]")
