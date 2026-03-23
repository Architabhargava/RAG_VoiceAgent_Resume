## 2024-03-23 - [Interruption & State Management in Push-to-Talk]
**Learning:** In voice-enabled interfaces with asynchronous microphone permissions (getUserMedia), an `isRecording` flag is essential to prevent "hot mic" race conditions if the user releases the button before the permission is granted. Additionally, explicitly stopping all tracks of the MediaStream ensures the microphone is correctly released, which is critical for privacy and battery life.
**Action:** Always implement a state flag to re-verify intent immediately after await-ing media permissions, and use `stream.getTracks().forEach(track => track.stop())` in the cleanup phase.

## 2024-03-23 - [Keyboard and Touch Support for PTT]
**Learning:** Mapping the 'Space' bar to Push-to-Talk provides a natural and accessible alternative to mouse clicks. However, it must be carefully guarded to avoid interfering with keyboard focus on other interactive elements or typing in text areas.
**Action:** Check `event.target` and `isContentEditable` in global keyboard listeners before executing voice-related shortcuts.
