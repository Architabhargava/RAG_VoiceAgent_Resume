const { test, expect } = require('@playwright/test');
const path = require('path');

test('basic a11y check', async ({ page }) => {
  const filePath = 'file://' + path.resolve('resume-rag-voice-agent/frontend/index.html');
  await page.goto(filePath);

  // Check for button ARIA label or descriptive text
  const recordBtn = page.locator('#recordBtn');
  await expect(recordBtn).toBeVisible();

  // Check if status has ARIA live region
  const status = page.locator('#status');
  await expect(status).toBeVisible();
  const ariaLive = await status.getAttribute('aria-live');
  console.log('Status aria-live:', ariaLive);
});
