## 2026-05-04 - Voice Interaction Robustness
**Learning:** In asynchronous Push-to-Talk (PTT) interfaces, a race condition exists where a user may release the trigger (key/pointer) before the microphone stream is fully initialized, leading to "stuck" recording states.
**Action:** Use a persistent `isRecordingIntent` flag to track the user's desire to record. Re-verify this flag immediately after the `getUserMedia` promise resolves; if the intent has since been cleared, explicitly stop all media tracks and abort the recording process.

## 2026-05-04 - Global Keyboard Shortcuts
**Learning:** Global keyboard shortcuts (like Space for PTT) can interfere with text entry if not properly scoped. However, restricting them too strictly (e.g., only `document.body`) can break functionality when the primary button has focus.
**Action:** Use a helper to check if the `event.target` is an input, textarea, or contentEditable element. If not, allow the global shortcut to proceed regardless of whether the focus is on the body or the specific interactive element.
