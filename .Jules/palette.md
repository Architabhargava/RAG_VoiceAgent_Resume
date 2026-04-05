## 2025-05-14 - Robust Voice Interaction State Management
**Learning:** Asynchronous UI flows (like requesting microphone permissions via `getUserMedia`) can create race conditions ("hot mic") if the user cancels the action while the promise is pending.
**Action:** Re-verify the interaction state flag (e.g., `isRecording`) immediately after the `await` to ensure the intent is still valid before proceeding with state-dependent logic.
