## 2025-05-15 - [Resource Management in Voice UX]
**Learning:** Always explicitly stop all tracks of a `MediaStream` when recording is finished. Just calling `mediaRecorder.stop()` does not always release the microphone hardware, which can leave the browser's "recording" indicator active and pose a privacy concern for users.
**Action:** Call `stream.getTracks().forEach(track => track.stop())` in the `onstop` callback of the `MediaRecorder`.

## 2025-05-15 - [Global Keyboard Listeners]
**Learning:** When adding global keyboard shortcuts (like Space for Push-to-Talk), it's important to consider future scalability. If inputs are added later, global listeners can interfere with typing.
**Action:** In larger apps, scope listeners to specific elements or check `event.target` before executing shortcut logic.
