## 2024-05-23 - Proper Microphone Release
**Learning:** Calling `mediaRecorder.stop()` does not automatically release the microphone hardware. The browser's "recording" indicator (e.g., the red dot in the tab) stays active until all tracks in the `MediaStream` are explicitly stopped.
**Action:** Always iterate over `stream.getTracks()` and call `.stop()` on each track in the `mediaRecorder.onstop` handler to ensure the microphone is fully released and user privacy is respected.
