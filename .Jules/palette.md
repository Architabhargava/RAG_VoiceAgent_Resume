## 2026-04-27 - Robust Push-to-Talk Interactions
**Learning:** For voice-based interfaces, a "Push to Talk" button must handle asynchronous initialization (like `getUserMedia`) robustly. Simple `mousedown`/`mouseup` events are prone to race conditions if the user releases the button before the microphone is ready.
**Action:** Always use a 'recording intent' flag. If the intent is lost before `getUserMedia` resolves, immediately stop the tracks. Use global `pointerup` and `keyup` listeners to ensure recording stops even if the interaction ends outside the button or focus is lost.

## 2026-04-27 - Keyboard Accessibility for Voice Agents
**Learning:** Users naturally expect the Spacebar to trigger recording in voice apps. Implementing this requires careful prevention of default scroll behavior and verification that the user isn't currently typing in an input field.
**Action:** Use a global `keydown` listener for `Space`, check for `e.repeat` to prevent rapid fire, and verify `e.target` is not an input, textarea, or contentEditable element before calling `e.preventDefault()` and starting the recording.
