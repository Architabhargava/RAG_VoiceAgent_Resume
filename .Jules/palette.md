## 2025-05-15 - [Push-to-Talk Interaction Patterns]
**Learning:** For voice-based "Push to Talk" (PTT) interfaces, a robust implementation requires synchronizing multiple input methods (Mouse, Touch, Keyboard) with a single `isRecording` state flag. It's critical to re-verify the intent flag immediately after asynchronous permission requests (like `getUserMedia`) to prevent "hot mic" race conditions if the user cancels the action during the prompt.
**Action:** Always use a state-controlled refactor for PTT buttons, ensuring `mouseleave`, `keyup`, and `touchend` all trigger a unified `stopRecording` flow that cleans up both UI state (ARIA, classes) and hardware tracks.

## 2025-05-15 - [Resource Management in Voice UIs]
**Learning:** Sequential audio playback in long-running WebSocket sessions can cause memory leaks if `URL.createObjectURL` is called repeatedly without revocation.
**Action:** Implement a `currentAudioUrl` tracker and explicitly call `URL.revokeObjectURL(oldUrl)` before assigning a new source to the `<audio>` element.
