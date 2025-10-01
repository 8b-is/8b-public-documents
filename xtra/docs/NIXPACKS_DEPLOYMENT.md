# Nixpacks Deployment Guide for 8b-is Projects

This guide provides templates and instructions for deploying all 8b-is projects using Nixpacks, enabling rapid deployment on Railway, Render, Fly.io, and other modern platforms.

## What is Nixpacks?

Nixpacks automatically builds and packages apps into OCI-compliant containers without writing a Dockerfile. It detects your language/framework and creates optimized, minimal containers.

## Production vs Development Dependencies

**Important:** Nixpacks handles this automatically! 

- Nixpacks sets `NPM_CONFIG_PRODUCTION=false` during the build phase
- This ensures devDependencies are installed for building (Vite, TypeScript, etc.)
- After building, only production dependencies are kept in the final image
- You do **NOT** need to use `-P` or `--production` flags

This two-stage approach means:
1. **Build stage**: All dependencies installed (including devDependencies)
2. **Runtime stage**: Only production dependencies in final container

## Quick Start

1. Add a `nixpacks.toml` to your project root
2. Deploy to your platform of choice
3. That's it! 🚀

## Templates by Project Type

### Svelte/SvelteKit Projects (mem8-explorer style)

```toml
# nixpacks.toml for Svelte projects
[phases.setup]
nixPkgs = ["nodejs"]  # Version detected from package.json

[phases.install]
# Just use frozen-lockfile - Nixpacks handles dev/prod split automatically
cmds = ["pnpm install --frozen-lockfile"]

[phases.build]
# Build phase has access to all dependencies (including devDependencies)
cmds = ["pnpm run build"]

[start]
# Runtime only needs production deps to serve the built files
cmd = "pnpm run preview --host 0.0.0.0 --port ${PORT:-8424}"

[variables]
NODE_ENV = "production"
CI = "true"
```

### Rust Web Services (Mem8 API style)

```toml
# nixpacks.toml for Rust API servers
[phases.setup]
nixPkgs = ["rustup", "pkg-config", "openssl"]

[phases.build]
cmds = [
  "rustup default stable",
  "cargo build --release --bin mem8-api-server"
]

[start]
cmd = "./target/release/mem8-api-server --port ${PORT:-8420}"

[variables]
RUST_LOG = "info"
```

### Python Services (with UV for blazing speed! 🚀)

```toml
# nixpacks.toml for Python - using UV because waiting is so 2023
[phases.setup]
nixPkgs = ["python311"]

[variables]
# UV is the way - 10-100x faster than pip!
NIXPACKS_PYTHON_PACKAGE_MANAGER = "uv"
PYTHONUNBUFFERED = "1"

[start]
cmd = "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8422}"

# That's it! UV is automatically installed and used 🎉
```

### Python with CUDA (GPU support)

```toml
# nixpacks.toml for ML/AI workloads
[phases.setup]
nixPkgs = ["python311", "cudatoolkit", "cudnn"]
aptPkgs = ["libgl1-mesa-glx", "libglib2.0-0"]

[variables]
NIXPACKS_PYTHON_PACKAGE_MANAGER = "uv"  # Still using UV!
CUDA_VISIBLE_DEVICES = "0"

[phases.install]
# UV handles PyTorch with CUDA like a champ
cmds = [
  "uv pip install torch --index-url https://download.pytorch.org/whl/cu118"
]

[start]
cmd = "python main.py"
```

### Next.js Projects

```toml
# nixpacks.toml for Next.js
[phases.setup]
nixPkgs = ["nodejs-18_x", "pnpm-8_x"]

[phases.install]
cmds = ["pnpm install --frozen-lockfile"]

[phases.build]
cmds = ["pnpm run build"]

[start]
cmd = "pnpm start -p ${PORT:-8424}"

[variables]
NODE_ENV = "production"
```

### Static Sites (with nginx)

```toml
# nixpacks.toml for static sites
[phases.setup]
nixPkgs = ["nodejs-18_x", "pnpm-8_x"]

[phases.install]
cmds = ["pnpm install --frozen-lockfile"]

[phases.build]
cmds = ["pnpm run build"]

[staticAssets]
"dist" = "/"

[start]
cmd = "nginx -g 'daemon off;'"
```

## Port Configuration

All 8b-is services use standard ports:
- **8420**: Mem8 API endpoints
- **8422**: Cheet API
- **8424**: Web apps (dev/containers)
- **8428**: LLM endpoints

Example with custom port:
```toml
[start]
cmd = "node server.js"

[variables]
PORT = "8424"  # Override platform's PORT
```

## Multi-Stage Builds

For complex projects needing build optimization:

```toml
# Advanced Rust build with caching
[phases.setup]
nixPkgs = ["rustup", "pkg-config", "openssl", "sccache"]

[phases.prebuild]
cmds = [
  "export SCCACHE_DIR=/cache/sccache",
  "export RUSTC_WRAPPER=sccache"
]

[phases.build]
cmds = [
  "cargo build --release",
  "strip target/release/app",
  "upx --best target/release/app"  # Optional compression
]

[phases.cache]
paths = ["/cache/sccache", "target"]
```

## Environment Variables

### Development vs Production

```toml
# Automatic environment detection
[variables]
API_URL = "${RAILWAY_ENVIRONMENT:=development} == 'production' ? 'https://api.8b.is' : 'http://localhost:8420'"
DEBUG = "${NODE_ENV:=development} != 'production'"
```

### Secrets Management

```toml
# Reference platform secrets
[variables]
DATABASE_URL = "${DATABASE_URL}"  # From platform
ANTHROPIC_API_KEY = "${ANTHROPIC_API_KEY}"
MEM8_LICENSE = "${MEM8_LICENSE:-trial}"
```

## Platform-Specific Configurations

### Railway

```toml
# Railway optimizations
[deploy]
startCommand = "pnpm start"
healthcheckPath = "/health"
healthcheckTimeout = 30

[variables]
RAILWAY_ENVIRONMENT = "${RAILWAY_ENVIRONMENT}"
```

### Render

```toml
# Render.com settings
[build]
buildCommand = "pnpm build"

[start]
cmd = "pnpm start"

[healthCheck]
path = "/api/health"
```

### Fly.io

```toml
# Fly.io with persistent storage
[mounts]
source = "mem8_data"
destination = "/data"

[variables]
MEM8_DATA_DIR = "/data"
```

## Common Patterns

### Hot Reload Development

```toml
# Development mode with hot reload
[phases.dev]
cmds = ["pnpm run dev --host 0.0.0.0"]

[start]
cmd = "${NODE_ENV:=development} == 'development' ? 'pnpm run dev' : 'pnpm run preview'"
```

### Database Migrations

```toml
[phases.release]
cmds = [
  "cargo run --bin migrate",
  "echo 'Migrations complete'"
]

[phases.build]
dependsOn = ["release"]
```

### Asset Optimization

```toml
[phases.build]
cmds = [
  "pnpm run build",
  "pnpm run optimize:images",
  "pnpm run compress:assets"
]
```

## Common Misconceptions

### Do I need `--production` or `-P` flags?

**No!** This is handled automatically by Nixpacks:

```toml
# ❌ DON'T DO THIS
cmds = ["pnpm install --frozen-lockfile --prod"]  # Wrong!
cmds = ["npm ci --production"]                     # Wrong!

# ✅ DO THIS
cmds = ["pnpm install --frozen-lockfile"]          # Correct!
cmds = ["npm ci"]                                  # Correct!
```

Nixpacks intelligently:
1. Installs ALL dependencies (including devDependencies) for the build
2. Removes devDependencies from the final runtime image
3. Results in smaller, optimized containers

## Troubleshooting

### Build Failures

1. **Missing dependencies**: Add to `nixPkgs` or `aptPkgs`
2. **Wrong Node version**: Specify exact version `nodejs-18_x`
3. **Build timeout**: Split into smaller phases

### Runtime Issues

1. **Port binding**: Always use `0.0.0.0` not `localhost`
2. **Missing env vars**: Check platform dashboard
3. **Memory limits**: Add swap or optimize

### Performance

1. **Cold starts**: Use `[phases.cache]` for dependencies
2. **Image size**: Multi-stage builds, remove dev dependencies
3. **Build speed**: Enable caching, use prebuilt binaries

## Quick Deployment Commands

```bash
# Railway
railway up

# Render
render deploy

# Fly.io
fly deploy

# Generic (using pack CLI)
pack build myapp --buildpack paketo-buildpacks/nodejs
```

## Example: Complete Mem8 Explorer Config

```toml
# Complete nixpacks.toml for mem8-explorer
[phases.setup]
nixPkgs = ["nodejs-18_x", "pnpm-8_x", "git"]

[phases.setup.node]
version = "18.19.0"

[phases.install]
cmds = ["pnpm install --frozen-lockfile"]
cacheDirectories = ["/root/.pnpm-store"]

[phases.build]
cmds = [
  "pnpm run build",
  "pnpm run test:ci || true",  # Optional tests
  "echo 'Build complete! 🚀'"
]

[start]
cmd = "pnpm run preview --host 0.0.0.0 --port ${PORT:-8424}"

[healthCheck]
path = "/"
interval = 30
timeout = 5

[variables]
NODE_ENV = "production"
PUBLIC_URL = "/"
VITE_API_URL = "${API_URL:-https://api.mem8.ai}"
VITE_ENABLE_ANALYTICS = "${ENABLE_ANALYTICS:-false}"

[phases.cache]
paths = ["node_modules", ".pnpm-store", "dist"]
```

## Best Practices

1. **Always use frozen lockfiles** (`--frozen-lockfile`)
2. **Specify exact versions** for consistency
3. **Cache aggressively** to speed builds
4. **Health checks** for reliability
5. **Strip debug symbols** in production
6. **Use multi-stage** for smaller images
7. **Environment variables** for configuration

## Resources

- [Nixpacks Docs](https://nixpacks.com/docs)
- [Railway Guide](https://docs.railway.app/deploy/nixpacks)
- [Render Guide](https://render.com/docs/nixpacks)
- [8b-is Deployment Standards](https://8b.is/docs/deployment)

---

*"Deploy faster than a neon sign flickers in cyberspace!" - The Mem8 Team* 🚀✨