## 2025-05-15 - Robust Push-to-Talk Interaction
**Learning:** For "hold to speak" interactions, using a combination of `pointerdown` on the trigger and a global `window.onpointerup` listener ensures the action reliably terminates even if the user moves their pointer off the button before releasing. Additionally, an `isRecordingIntent` flag is crucial to handle cases where `getUserMedia` (async) resolves after the user has already released the button, preventing "hot mic" scenarios.
**Action:** Implement window-level release listeners and intent flags for all asynchronous "hold" interactions.

## 2025-05-15 - Voice UI Accessibility
**Learning:** Combining `aria-pressed` on the trigger, `aria-live="polite"` on the status container, and dynamic button text ("Push to Talk" vs "Release to Send") provides a clear, accessible feedback loop for screen reader users during real-time voice interactions.
**Action:** Always synchronize ARIA states, live regions, and visible text during state-heavy interactions like recording.
