## 2025-05-22 - [Voice Interaction Safety and Accessibility]
**Learning:** In asynchronous voice interactions (like requesting microphone permission), it is critical to re-verify the user's intent immediately after the promise resolves. A user might release the "Push to Talk" button while the browser is still prompting for permission, leading to a "hot mic" race condition if not handled. Additionally, for PTT buttons, using `aria-pressed` and `aria-live` provides essential state feedback for screen readers that visual changes (like color) alone do not.
**Action:** Always check a state flag (e.g., `isRecording`) after `await navigator.mediaDevices.getUserMedia()` and implement `aria-live="polite"` on status containers.

## 2025-05-22 - [Robust Push-to-Talk Event Handling]
**Learning:** For a reliable "Push to Talk" experience, mouse events alone are insufficient. `mouseleave` is necessary to stop recording if the user drags their cursor off the button while holding it. Keyboard support (Space bar) must prevent default scrolling behavior and avoid interfering with text inputs.
**Action:** Implement `mousedown`, `mouseup`, `mouseleave`, `touchstart`, `touchend`, and global `keydown`/`keyup` listeners for PTT interactions.
