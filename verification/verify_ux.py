import os
from playwright.sync_api import sync_playwright, expect

def test_ux_improvement():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use file URL since it's a static HTML file
        curr_dir = os.getcwd()
        file_path = f"file://{curr_dir}/resume-rag-voice-agent/frontend/index.html"

        page = browser.new_page()

        # Mocking navigator.mediaDevices.getUserMedia and MediaRecorder
        page.add_init_script("""
            navigator.mediaDevices.getUserMedia = async () => {
                return {
                    getTracks: () => [{ stop: () => {} }]
                };
            };
            window.MediaRecorder = class {
                constructor() {}
                start() { this.state = 'recording'; }
                stop() {
                    this.state = 'inactive';
                    if (this.onstop) this.onstop();
                }
            };
            // Mock WebSocket
            window.WebSocket = class {
                constructor() { setTimeout(() => { if (this.onopen) this.onopen(); }, 10); }
                send() {}
            };
        """)

        page.goto(file_path)

        btn = page.locator("#recordBtn")
        status = page.locator("#status")

        # Initial state
        expect(btn).to_have_attribute("aria-pressed", "false")
        expect(btn).to_have_text("Push to Talk")
        expect(status).to_have_attribute("aria-live", "polite")

        # Test mouse down (recording start)
        page.mouse.move(btn.bounding_box()['x'] + 5, btn.bounding_box()['y'] + 5)
        page.mouse.down()

        # Allow time for async getUserMedia
        page.wait_for_timeout(500)

        expect(btn).to_have_attribute("aria-pressed", "true")
        expect(btn).to_have_text("Release to Send")
        expect(btn).to_have_class("recording")
        expect(status).to_contain_text("Recording...")

        page.screenshot(path="verification/recording_state.png")

        # Test mouse up (recording stop)
        page.mouse.up()
        expect(btn).to_have_attribute("aria-pressed", "false")
        expect(btn).to_have_text("Push to Talk")
        expect(btn).not_to_have_class("recording")

        # Test Space key
        page.keyboard.down("Space")
        page.wait_for_timeout(500)
        expect(btn).to_have_attribute("aria-pressed", "true")
        expect(btn).to_have_text("Release to Send")

        page.screenshot(path="verification/keyboard_recording_state.png")

        page.keyboard.up("Space")
        expect(btn).to_have_attribute("aria-pressed", "false")

        browser.close()

if __name__ == "__main__":
    test_ux_improvement()
