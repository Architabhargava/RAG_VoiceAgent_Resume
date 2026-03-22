import os
import time
from playwright.sync_api import sync_playwright, expect

def test_race_condition_fix():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        curr_dir = os.getcwd()
        file_path = f"file://{curr_dir}/resume-rag-voice-agent/frontend/index.html"
        page = browser.new_page()

        # Mocking navigator.mediaDevices.getUserMedia with a delay
        # to simulate the race condition
        page.add_init_script("""
            window.tracksStopped = 0;
            navigator.mediaDevices.getUserMedia = async () => {
                await new Promise(r => setTimeout(r, 200));
                return {
                    getTracks: () => [{ stop: () => { window.tracksStopped++; } }]
                };
            };
            window.MediaRecorder = class {
                constructor() {}
                start() { this.state = 'recording'; }
                stop() { this.state = 'inactive'; if (this.onstop) this.onstop(); }
            };
            window.WebSocket = class { constructor() { }; send() {} };
        """)

        page.goto(file_path)

        btn = page.locator("#recordBtn")

        # Scenario: Rapid click and release
        page.mouse.move(btn.bounding_box()['x'] + 5, btn.bounding_box()['y'] + 5)
        page.mouse.down() # Start called
        time.sleep(0.05)
        page.mouse.up()   # Stop called (isRecording = false)

        # Wait for getUserMedia to finish (200ms delay in mock)
        page.wait_for_timeout(500)

        # The button should NOT be in recording state
        expect(btn).not_to_have_class("recording")
        expect(btn).to_have_text("Push to Talk")

        # Verify tracks were stopped even though mediaRecorder.start was never called
        tracks_stopped = page.evaluate("window.tracksStopped")
        assert tracks_stopped > 0, "Microphone tracks should have been stopped after release"

        page.screenshot(path="verification/race_condition_test.png")
        browser.close()

if __name__ == "__main__":
    test_race_condition_fix()
