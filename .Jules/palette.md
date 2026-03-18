## 2025-05-15 - [Accessible Voice Interaction Patterns]
**Learning:** In asynchronous voice-to-text flows (like using `getUserMedia`), user state can change while the permission promise is pending. Always re-verify the "isRecording" flag after the `await` and stop media tracks immediately if the user cancelled.
**Action:** Implement immediate UI feedback (ARIA, button text) upon interaction, but defer actual hardware/socket starts until promises resolve, with post-resolve state checks.

## 2025-05-15 - [Keyboard Shortcut Safety]
**Learning:** Global 'Space' bar listeners for "Push to Talk" can interfere with normal typing in inputs or textareas.
**Action:** Always check `event.target.tagName` and `isContentEditable` before preventing default or triggering recording logic in global keyboard listeners.

## 2025-05-15 - [Resource Cleanup in Voice Agents]
**Learning:** Microphones remain "active" in the browser UI even if `mediaRecorder.stop()` is called, unless all tracks in the underlying `MediaStream` are explicitly stopped.
**Action:** Always loop through `stream.getTracks()` and call `.stop()` on each track in the `onstop` handler or cleanup function.
