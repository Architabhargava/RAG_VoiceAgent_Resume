## 2025-05-14 - [Interaction Safety in Async UI Flows]
**Learning:** In asynchronous UI flows like requesting microphone permissions via `getUserMedia`, the user might change their intent (e.g., release the button) before the promise resolves.
**Action:** Always re-verify the interaction state (e.g., `isRecording` flag) immediately after the `await` to ensure the action is still desired before proceeding with hardware-dependent logic.

## 2025-05-14 - [CSS Specificity and State Classes]
**Learning:** When adding state-based styles (like `.recording`) to an element with an ID in a single-file HTML, simple class selectors might be overridden by the higher specificity of the ID-based base styles.
**Action:** Combine state classes with the element ID (e.g., `#recordBtn.recording`) or use `!important` as a last resort in simple static files to ensure state-based visual feedback is correctly applied.

## 2025-05-14 - [Keyboard Accessibility for Hold-to-Talk]
**Learning:** Mapping the 'Space' bar to a hold-to-talk interaction provides a high-quality "walkie-talkie" feel for power users, but it must be carefully guarded.
**Action:** Global keyboard listeners for shortcuts like 'Space' should check `event.target.tagName` and `isContentEditable` to avoid interfering with natural typing in inputs or textareas.
