## 2025-05-14 - Robust Voice Interaction UX
**Learning:** For "Push to Talk" interfaces, relying solely on 'mousedown'/'mouseup' is fragile. Using 'pointerdown' on the button and a window-level 'pointerup' ensures recording state is reliably terminated even if the interaction ends outside the button. Additionally, checking 'isRecordingIntent' after 'getUserMedia' resolves prevents 'hot mic' race conditions if the user releases the button during the permission prompt.
**Action:** Always use window-level 'pointerup' and an intent flag when implementing hold-to-interact patterns.
