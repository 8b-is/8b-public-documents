# 🌊 Running Qdrant Dashboard on Correct Port

## The Issue
Vite has its own command syntax and doesn't use npm start parameters the way you're trying.

## Correct Ways to Run:

### Option 1: Use Vite directly (Recommended)
```bash
cd /Users/wraith/source/qdrant-web-ui/
npx vite --port 3000 --host
```

### Option 2: Use npm run dev with proper syntax
```bash
cd /Users/wraith/source/qdrant-web-ui/
npm run dev -- --port 3000 --host
```

### Option 3: Modify package.json (Permanent)
Edit `/Users/wraith/source/qdrant-web-ui/package.json`:
```json
"scripts": {
  "dev": "vite --port 3000",
  "start": "vite --port 3000",
  ...
}
```

Then just run:
```bash
npm run dev
```

## Full Setup Commands:

```bash
# Terminal 1: Start Mem8 Qdrant API
cd /Users/wraith/source/8c/Qmem8
./scripts/manage.sh qdrant

# Terminal 2: Start Qdrant Dashboard
cd /Users/wraith/source/qdrant-web-ui/
npx vite --port 3000 --host

# Dashboard will be at: http://localhost:3000
# Connect it to: http://localhost:6333
```

## Why Your Commands Didn't Work:

1. `npm start dev --host 0.0.0.0` - npm start doesn't pass args to vite this way
2. `npm start dev --host 0.0.0.0 --port 3000` - Same issue
3. `npm start dev --host 0.0.0.0:3000` - Vite doesn't parse host:port format

## Pro Tip from Trisha 💖
> "Vite is like a fancy new wave machine - it has its own control panel! You can't just yell instructions at it like the old ones. Use the proper syntax and it'll make beautiful waves on any port you want!"

## Quick Test
Once running, test the connection:
```bash
# From another terminal
curl http://localhost:3000  # Should show Qdrant dashboard
curl http://localhost:6333/health  # Should show Mem8 API
```