import { readFile } from 'node:fs/promises';
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

const prefix = (process.env.SITE_BASE || '').replace(/\/$/, '');
const route = (path = '') => `${prefix}/${path.replace(/^\//, '')}`;

test('home navigation and document links retain the deployment prefix', async ({ page }) => {
  const response = await page.goto(route());
  expect(response?.status()).toBe(200);
  await expect(page.locator('main h1')).toBeVisible();
  for (const href of await page.locator('a[href^="/"]').evaluateAll(links => links.map(link => link.getAttribute('href')!))) {
    if (!href.startsWith('//')) expect(href, `Unprefixed local link: ${href}`).toMatch(new RegExp(`^${prefix}/`));
  }
  for (const path of ['explorer/', 'playground/', 'library/unknown-not-dontcare/', 'library/field-before-spike/']) {
    const result = await page.request.get(route(path));
    expect(result.status(), path).toBe(200);
  }
});

test('Explorer filters curated documents, announces empty results, and retains URL state', async ({ page }) => {
  await page.goto(route('explorer/'));
  await page.getByLabel('Collection', { exact: true }).selectOption('curated');
  await expect(page.locator('.document:visible')).toHaveCount(6);
  await page.getByLabel('Title, author, or idea').fill('zzzz_no_such_document_zzzz');
  await expect(page.locator('#library-empty')).toBeVisible();
  await expect(page.locator('#library-count')).toHaveText('0 documents');
  await page.getByLabel('Title, author, or idea').fill('fixed point');
  await expect(page.locator('.document:visible')).toHaveCount(1);
  await expect(page.locator('#library-count')).toHaveText('1 document');
  await expect(page).toHaveURL(/q=fixed\+point/);
  await page.reload();
  await expect(page.locator('.document:visible')).toHaveCount(1);
  await page.getByRole('link', { name: 'Two Meanings of Fixed Point', exact: true }).click();
  await expect(page).toHaveURL(route('library/fixed-point-essay/'));
  await expect(page.locator('main h1')).toContainText('Two Meanings of Fixed Point');
});

test('Pagefind searches the full paper text and opens the Guardian manuscript', async ({ page }) => {
  await page.goto(route());
  await page.getByRole('button', { name: 'Search', exact: true }).click();
  const dialog = page.getByRole('dialog', { name: 'Search', exact: true });
  // This word occurs in the worked counterexample, not its catalog metadata.
  await dialog.getByRole('textbox', { name: 'Search', exact: true }).fill('nonterminal');
  const result = dialog.locator(`a[href="${route('library/unknown-not-dontcare/')}"]`);
  await expect(result).toHaveText('Unknown Is Not Don’t-Care');
  await result.click();
  await expect(page).toHaveURL(route('library/unknown-not-dontcare/'));
  await expect(page.locator('main')).toContainText('Consider two nonterminal instances labeled');
});

test('Guardian works by keyboard and exports its complete scoped experiment', async ({ page }) => {
  const errors: string[] = [];
  page.on('pageerror', error => errors.push(error.message));
  await page.goto(route('playground/'));
  const send = page.getByRole('button', { name: 'Send cycles', exact: true });
  await send.focus();
  await page.keyboard.press('Enter');
  await expect(page.locator('[data-state="a-stage"]')).toHaveText('EarlyChildhood');
  await expect(page.locator('[data-state="b-stage"]')).toHaveText('Infant');
  await expect(page.locator('[data-status]')).toContainText('Their stage labels now differ');

  await page.getByRole('spinbutton', { name: 'Stable cycles to graduate' }).fill('3');
  await page.getByRole('spinbutton', { name: 'Nonviable cycles to Mercy' }).fill('4');
  await page.getByRole('button', { name: 'Apply and reset' }).focus();
  await page.keyboard.press('Enter');
  await expect(page.locator('[data-state="a-stable"]')).toHaveText('2');
  await expect(page.locator('[data-state="b-stable"]')).toHaveText('0');
  await page.getByRole('combobox', { name: 'Cycle input' }).selectOption('nonviable');
  await page.getByRole('spinbutton', { name: 'Cycles to send' }).fill('4');
  await send.click();
  await expect(page.locator('[data-state="a-verdict"]')).toHaveText('Terminate(NonViable)');
  await page.getByRole('combobox', { name: 'Cycle input' }).selectOption('stable');
  await page.getByRole('spinbutton', { name: 'Cycles to send' }).fill('3');
  await send.click();
  await expect(page.locator('[data-state="a-stage"]')).toHaveText('EarlyChildhood');
  await expect(page.locator('[data-state="a-verdict"]')).toHaveText('Terminate(NonViable)');

  const pending = page.waitForEvent('download');
  await page.getByRole('button', { name: 'Download complete trace (JSON)' }).click();
  const download = await pending;
  const trace = JSON.parse(await readFile((await download.path())!, 'utf8'));
  expect(trace.configuration).toEqual({ graduation: 3, mercy: 4 });
  expect(trace.initial.a.stable).toBe(2);
  expect(trace.cycles).toHaveLength(7);
  expect(trace.cycles.at(-1).a.verdict).toBe('Terminate(NonViable)');
  expect(trace.model).toContain('no watchdog simulation');
  expect(errors).toEqual([]);
});

test('illustration has an intact image, text transcription, and separate interpretation', async ({ page }) => {
  await page.goto(route('library/field-before-spike/'));
  const illustration = page.getByRole('img', { name: /Four illustrated panels/ });
  await expect(illustration).toBeVisible();
  expect(await illustration.evaluate((image: HTMLImageElement) => image.complete && image.naturalWidth > 0)).toBe(true);
  await expect(page.getByRole('heading', { name: 'Full text transcription', exact: true })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Editorial interpretation', exact: true })).toBeVisible();
  const imageSource = await illustration.getAttribute('src');
  expect(imageSource).toMatch(new RegExp(`^${prefix}/`));
  expect((await page.request.get(imageSource!)).status()).toBe(200);
});

for (const theme of ['light', 'dark'] as const) {
  test(`${theme} theme passes automated WCAG 2 AA checks on the new experiences`, async ({ page }) => {
    for (const path of ['', 'explorer/', 'playground/', 'library/field-before-spike/']) {
      await page.goto(route(path));
      await page.evaluate(theme => {
        document.documentElement.dataset.theme = theme;
        localStorage.setItem('starlight-theme', theme);
      }, theme);
      const results = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21aa']).analyze();
      expect(results.violations, `${theme} ${path}: ${JSON.stringify(results.violations.map(v => ({ id: v.id, nodes: v.nodes.map(n => ({ target: n.target, failure: n.failureSummary })) })), null, 2)}`).toEqual([]);
    }
  });
}

test('new experiences fit a narrow mobile viewport without page overflow', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  for (const path of ['', 'explorer/', 'playground/', 'library/field-before-spike/']) {
    await page.goto(route(path));
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), path).toBe(true);
    await expect(page.locator('main h1')).toBeVisible();
  }
});

test('the worked example and document collection remain readable without JavaScript', async ({ browser }) => {
  const context = await browser.newContext({ javaScriptEnabled: false });
  const page = await context.newPage();
  const origin = process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:4321';
  await page.goto(`${origin}${route('playground/')}`);
  await expect(page.locator('noscript p')).toBeVisible();
  await expect(page.locator('noscript p')).toContainText('The interactive controls need JavaScript.');
  await expect(page.getByRole('button', { name: 'Send cycles', exact: true })).toBeDisabled();
  await expect(page.getByRole('cell', { name: 'Infant, stable streak 63', exact: true })).toBeVisible();
  await page.goto(`${origin}${route('explorer/')}`);
  await expect(page.locator('noscript p')).toBeVisible();
  await expect(page.locator('noscript p')).toContainText('Filtering needs JavaScript.');
  await expect(page.getByRole('link', { name: 'Unknown Is Not Don’t-Care', exact: true }).first()).toBeVisible();
  await context.close();
});
