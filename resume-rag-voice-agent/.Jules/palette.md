## 2024-05-22 - Global Keyboard Shortcuts for Voice Interaction

**Learning:** When implementing global keyboard shortcuts (like using 'Space' for push-to-talk), it's critical to check `event.target` and `isContentEditable` to ensure the shortcut does not interfere with the user's ability to type in input fields or textareas. Additionally, using `event.repeat` prevents the shortcut from firing multiple times if the key is held down.

**Action:** Always check `event.target.tagName` and `isContentEditable` before preventing default behavior in global `keydown` listeners for common keys like Space or Enter.

## 2024-05-22 - Async Interaction State Verification

**Learning:** In asynchronous UI flows (like requesting microphone permissions via `getUserMedia`), re-verify the interaction state (e.g., `isRecording` flag) immediately after the `await` to ensure the user hasn't cancelled the action while the promise was pending. This prevents "hot mic" race conditions where a recording starts even though the user has released the button.

**Action:** Always check the current application state immediately after an `await` in an event handler to ensure the original intent is still valid.

## 2024-05-22 - Resource Management with `URL.revokeObjectURL`

**Learning:** Using `URL.createObjectURL` to play dynamic media (like TTS audio blobs) without calling `URL.revokeObjectURL` causes memory leaks as the browser retains references to the blobs until the page is closed. For chat-based agents, this can lead to significant memory consumption over long sessions.

**Action:** Maintain a reference to the `currentAudioUrl` and always revoke it before creating a new one or when the session ends.
