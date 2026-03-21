import { test, expect } from '@playwright/test';
import path from 'path';

test.describe('Frontend UX', () => {
  test.beforeEach(async ({ page }) => {
    // Mock WebSocket and MediaRecorder
    await page.addInitScript(() => {
      // Mock WebSocket
      window.WebSocket = class MockWebSocket extends EventTarget {
        constructor(url) {
          super();
          this.url = url;
          this.readyState = 1; // OPEN
          setTimeout(() => {
            this.dispatchEvent(new Event('open'));
          }, 0);
        }
        send(data) {}
        close() {}
      } as any;

      // Mock MediaRecorder
      window.MediaRecorder = class MockMediaRecorder extends EventTarget {
        state = 'inactive';
        constructor(stream) {
          super();
        }
        start() { this.state = 'recording'; }
        stop() {
          this.state = 'inactive';
          this.dispatchEvent(new Event('stop'));
        }
        ondataavailable = null;
        onstop = null;
      } as any;

      // Mock getUserMedia
      Object.defineProperty(navigator, 'mediaDevices', {
        value: {
          getUserMedia: async () => ({
            getTracks: () => [{ stop: () => {} }],
          }),
        },
      });
    });

    const filePath = path.resolve('resume-rag-voice-agent/frontend/index.html');
    await page.goto(`file://${filePath}`);
  });

  test('button has correct initial ARIA attributes', async ({ page }) => {
    const recordBtn = page.locator('#recordBtn');
    await expect(recordBtn).toHaveAttribute('aria-pressed', 'false');
    await expect(recordBtn).toHaveAttribute('aria-label', 'Push to Talk');
    await expect(recordBtn).toContainText('Push to Talk');
  });

  test('status element has aria-live', async ({ page }) => {
    const status = page.locator('#status');
    await expect(status).toHaveAttribute('aria-live', 'polite');
  });

  test('button changes state on mousedown', async ({ page }) => {
    const recordBtn = page.locator('#recordBtn');
    await recordBtn.dispatchEvent('mousedown');

    await expect(recordBtn).toHaveClass(/recording/);
    await expect(recordBtn).toHaveAttribute('aria-pressed', 'true');
    await expect(recordBtn).toContainText('Release to Send');

    const status = page.locator('#status');
    await expect(status).toContainText('Recording...');
  });

  test('button resets on mouseup', async ({ page }) => {
    const recordBtn = page.locator('#recordBtn');
    await recordBtn.dispatchEvent('mousedown');
    await recordBtn.dispatchEvent('mouseup');

    await expect(recordBtn).not.toHaveClass(/recording/);
    await expect(recordBtn).toHaveAttribute('aria-pressed', 'false');
    await expect(recordBtn).toContainText('Push to Talk');
  });

  test('button resets on mouseleave', async ({ page }) => {
    const recordBtn = page.locator('#recordBtn');
    await recordBtn.dispatchEvent('mousedown');
    await recordBtn.dispatchEvent('mouseleave');

    await expect(recordBtn).not.toHaveClass(/recording/);
    await expect(recordBtn).toHaveAttribute('aria-pressed', 'false');
  });

  test('space key triggers recording', async ({ page }) => {
    const recordBtn = page.locator('#recordBtn');

    await page.keyboard.down(' ');
    await expect(recordBtn).toHaveClass(/recording/);
    await expect(recordBtn).toHaveAttribute('aria-pressed', 'true');

    await page.keyboard.up(' ');
    await expect(recordBtn).not.toHaveClass(/recording/);
    await expect(recordBtn).toHaveAttribute('aria-pressed', 'false');
  });
});
