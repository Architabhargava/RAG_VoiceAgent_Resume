## 2025-05-14 - [Robust Push-to-Talk Implementation]
**Learning:** For voice-activated interfaces, "Push to Talk" requires multi-modal input handling (Mouse, Touch, and Keyboard). A critical race condition exists when using `getUserMedia`: the user may release the trigger before the browser permission prompt is accepted.
**Action:** Always re-verify the active recording state flag immediately after the `await navigator.mediaDevices.getUserMedia()` call. If the user is no longer intent on recording, immediately stop all tracks of the newly obtained stream to prevent a "hot mic" situation.
>>>>>>> REPLACE
