import { defineConfig } from '@playwright/test';

// Build with the same SITE_BASE before running these tests.
// SITE_BASE=/8b-public-documents npm run build
// SITE_BASE=/8b-public-documents npx playwright test
const prefix = (process.env.SITE_BASE || '').replace(/\/$/, '');
export default defineConfig({
  testDir: './tests/browser',
  fullyParallel: false,
  workers: 2,
  timeout: 45_000,
  expect: { timeout: 10_000 },
  reporter: [['list'], ['html', { open: 'never' }]],
  use: {
    baseURL: process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:4321',
    browserName: 'chromium',
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
  },
  webServer: {
    command: 'npm run preview',
    url: `http://127.0.0.1:4321${prefix}/`,
    reuseExistingServer: !process.env.CI,
    env: { SITE_BASE: process.env.SITE_BASE || '/' },
  },
});
