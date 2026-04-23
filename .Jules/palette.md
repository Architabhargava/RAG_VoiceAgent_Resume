## 2025-05-15 - Robust Push-to-Talk Implementation
**Learning:** For voice interfaces, a simple "onmousedown/onmouseup" logic is insufficient due to the asynchronous nature of `getUserMedia`. Using an `isRecordingIntent` flag ensures that the recording only starts and stays active if the user is still holding the button when permission is granted, preventing "hot mic" race conditions.
**Action:** Always synchronize asynchronous hardware access with a persistent intent flag and use window-level release listeners (mouseup/touchend) for reliable state cleanup.
