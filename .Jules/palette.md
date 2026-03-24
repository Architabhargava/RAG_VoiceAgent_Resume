## 2024-03-24 - [Microphone Resource & State Management]
**Learning:** In asynchronous voice interaction flows, it is critical to re-verify the interaction intent (e.g., via an `isRecording` flag) immediately after the `getUserMedia` promise resolves. This prevents "hot mic" race conditions if the user cancels the action while permissions are being granted. Additionally, explicitly stopping all media tracks and revoking Blob URLs is essential to prevent hardware lock-in and memory leaks in long-running browser sessions.
**Action:** Always implement a state flag check after `getUserMedia` and include a cleanup routine that stops tracks and revokes previous `audio.src` URLs.

## 2024-03-24 - [Accessible Push-to-Talk Patterns]
**Learning:** A robust "Push to Talk" (PTT) implementation must go beyond `mousedown` to be truly accessible and intuitive. This includes:
1. Mapping the `Space` key with proper focus/input field safety checks.
2. Implementing `mouseleave` and `touchend` listeners to ensure recording stops when the interaction area is exited.
3. Using `aria-live="polite"` for status updates and `aria-pressed` for the button state to provide immediate feedback to assistive technologies.
**Action:** Use a unified `startRecording`/`stopRecording` logic across mouse, touch, and keyboard events, ensuring `e.preventDefault()` is used for keyboard shortcuts to avoid page scrolling.
