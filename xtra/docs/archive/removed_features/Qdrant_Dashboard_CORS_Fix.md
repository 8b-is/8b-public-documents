# 🌊 Fixing CORS for Local Qdrant Dashboard

## Quick Fix Steps

### 1. Run Mem8's Qdrant API Server
```bash
# From Qmem8 directory
./scripts/manage.sh qdrant
```

### 2. Run Qdrant Dashboard Locally

Since you've cloned the dashboard at `/Users/wraith/source/qdrant-web-ui/`, run it with:

```bash
cd /Users/wraith/source/qdrant-web-ui/

# Install dependencies (if not done)
npm install

# Run with proxy to avoid CORS
npm run dev -- --proxy http://localhost:6333
```

### 3. Alternative: Disable CORS in Browser (Development Only!)

For Chrome on macOS:
```bash
open -n -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --user-data-dir="/tmp/chrome_dev_test" --disable-web-security --disable-features=IsolateOrigins,site-per-process
```

### 4. Or Use the Hosted Version

The hosted version at https://qdrant.github.io/qdrant-web-ui/ should work with our CORS settings.

## What Our CORS Config Does

Our server allows:
- ✅ Any origin (`allow_any_origin()`)
- ✅ All HTTP methods (GET, POST, PUT, DELETE, OPTIONS, HEAD, PATCH)
- ✅ All common headers
- ✅ Credentials
- ✅ Preflight caching (1 hour)

## Debugging CORS

If you still see CORS errors:

1. **Check browser console** for the exact error
2. **Look for preflight requests** (OPTIONS method)
3. **Verify the server is running** on port 6333
4. **Try a different browser** to rule out extensions

## Pro Tip from Trisha 💖

> "CORS is like a bouncer at a club - sometimes you need to sweet-talk it! Our server is already saying 'everyone's welcome', but browsers can be extra cautious. The proxy method is like having a friend vouch for you at the door!"

## Common Issues

### Issue: "CORS policy: No 'Access-Control-Allow-Origin'"
**Fix**: Make sure you're running the latest version with our updated CORS config

### Issue: "Preflight request failed"
**Fix**: The dashboard might be sending headers we're not allowing. Check browser network tab.

### Issue: "Connection refused"
**Fix**: Ensure the Mem8 server is running on port 6333

---

*Making waves across domains! 🌊*