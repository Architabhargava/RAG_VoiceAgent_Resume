## 2025-05-14 - [Interruption Safety in Recording UI]
**Learning:** Asynchronous operations in UI handlers (like `getUserMedia`) can lead to race conditions if the user stops the action while the operation is pending. Always re-verify the interaction state after awaiting async calls before proceeding with UI or state updates.
**Action:** In voice recording flows, check `isRecording` immediately after `await navigator.mediaDevices.getUserMedia()` and stop the stream if the user has already released the trigger.

## 2025-05-14 - [CSS-First State Styling]
**Learning:** Prefer using CSS classes (e.g., `.recording`) for state-based visual changes rather than manipulating `element.style` directly in JavaScript. This keeps styling decoupled and more maintainable.
**Action:** Define state-specific styles in the CSS block and use `classList.add`/`classList.remove` to trigger them in response to user events.
