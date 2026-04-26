## 2025-04-26 - [Robust Voice Interaction State Management]
**Learning:** In asynchronous voice applications, users may release a "Push to Talk" button before the microphone initialization (`getUserMedia`) completes, leading to "hot mic" race conditions where recording starts and continues after the user has stopped interacting.
**Action:** Always use an `isRecordingIntent` flag and re-verify it immediately after the `getUserMedia` promise resolves. If intent is lost, explicitly stop all stream tracks to ensure privacy and predictable state.
