## 2025-05-14 - Enhanced Push-to-Talk Robustness
**Learning:** In asynchronous voice interactions (like 'getUserMedia'), a race condition exists where users may release the 'Push to Talk' button before the promise resolves. This can lead to 'hot mic' situations or logic errors if state is not re-verified immediately after the await.
**Action:** Always re-verify the active intent flag (e.g., 'isRecording') immediately after any asynchronous call that precedes recording start to ensure the microphone stream is correctly cleaned up if the interaction was cancelled.

## 2025-05-14 - Multi-modal Voice Interaction
**Learning:** Mapping 'Space' for Push-to-Talk is highly intuitive but requires careful event management: 'event.repeat' check to prevent multiple starts, and 'event.target' checks to avoid interfering with input fields.
**Action:** Use global keydown/keyup listeners with 'event.repeat' protection and 'isContentEditable'/'tagName' filters for accessible keyboard shortcuts.
