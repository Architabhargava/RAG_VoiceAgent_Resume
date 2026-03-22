## 2024-03-22 - [Push to Talk Interaction Safety]
**Learning:** In asynchronous voice-enabled frontends, requesting microphone permissions via `getUserMedia` is a common source of "hot mic" race conditions. If a user releases the 'Push to Talk' button *before* the asynchronous permission request resolves, the subsequent `MediaRecorder.start()` will run and the microphone will remain active indefinitely because the internal `isRecording` flag was already reset to `false`.

**Action:** Always re-verify the interaction state (e.g., `isRecording` flag) immediately after the `await navigator.mediaDevices.getUserMedia()` call. If the intent has been cancelled while the promise was pending, explicitly stop all tracks of the newly obtained stream and return early.

## 2024-03-22 - [Release to Send UX Pattern]
**Learning:** For 'Push to Talk' interfaces, changing the button text from "Push to Talk" to "Release to Send" during the active recording state provides immediate, actionable feedback to the user on how to complete their action. This is more helpful than a generic "Recording..." status alone.

**Action:** Update the button's inner text to reflect the *next* action required to complete the interaction (e.g., "Release to Send") while the primary interaction is active.
