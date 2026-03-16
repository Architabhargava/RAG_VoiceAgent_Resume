## 2025-05-14 - [Aria-pressed and dynamic labels for PTT]
**Learning:** Using `aria-pressed` and dynamic `aria-label` updates on a Push-to-Talk button provides immediate and clear feedback to screen reader users about the state of the recording.
**Action:** Always implement `aria-pressed` and update `aria-label` when a button has a binary "active/recording" state.

## 2025-05-14 - [Push-to-Talk Interaction Safety]
**Learning:** Global keyboard listeners for PTT (like the Space bar) must check the event target to avoid interfering with users typing in input fields or textareas.
**Action:** Use `event.target.tagName` and `isContentEditable` checks in global keydown/keyup listeners.

## 2025-05-14 - [Microphone Resource Management]
**Learning:** Failing to stop all tracks of a `MediaStream` when recording ends can leave the microphone active in the browser, which is a privacy concern and poor UX.
**Action:** Explicitly call `stream.getTracks().forEach(track => track.stop())` in the `MediaRecorder.onstop` callback.
