import asyncio
import os
from playwright.async_api import async_playwright

async def verify_ux():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        file_path = f"file://{os.path.abspath('resume-rag-voice-agent/frontend/index.html')}"
        await page.goto(file_path)

        # Mock BEFORE interacting
        await page.add_init_script("""
            window.navigator.mediaDevices.getUserMedia = async () => {
                return {
                    getTracks: () => [{ stop: () => {} }]
                };
            };
            window.MediaRecorder = class {
                constructor() {
                    this.state = 'inactive';
                    this.ondataavailable = null;
                    this.onstop = null;
                }
                start() { this.state = 'recording'; }
                stop() {
                    this.state = 'inactive';
                    if (this.onstop) this.onstop();
                }
            };
        """)

        # Refresh to apply mock (or just navigate after script addition)
        await page.reload()

        print("Checking initial state...")
        record_btn = page.locator("#recordBtn")
        status = page.locator("#status")

        assert await record_btn.get_attribute("aria-pressed") == "false"
        assert await status.get_attribute("aria-live") == "polite"

        print("Testing Push to Talk...")
        # Use mouse click hold simulation
        box = await record_btn.bounding_box()
        await page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
        await page.mouse.down()

        await asyncio.sleep(0.5)

        aria_pressed = await record_btn.get_attribute("aria-pressed")
        print(f"Aria-pressed during recording: {aria_pressed}")

        assert aria_pressed == "true"
        assert "recording" in (await record_btn.get_attribute("class") or "")

        await page.mouse.up()
        await asyncio.sleep(0.1)

        assert await record_btn.get_attribute("aria-pressed") == "false"

        print("Testing Space key...")
        await page.keyboard.down("Space")
        await asyncio.sleep(0.5)
        assert await record_btn.get_attribute("aria-pressed") == "true"

        await page.keyboard.up("Space")
        await asyncio.sleep(0.1)
        assert await record_btn.get_attribute("aria-pressed") == "false"

        print("UX verification passed!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_ux())
