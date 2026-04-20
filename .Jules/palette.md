## 2025-05-14 - Robust Voice Interaction UX
**Learning:** Voice interaction frontends benefit greatly from synchronizing visual feedback (color, text), accessibility (ARIA, keyboard), and mobile support (touch events) into a single state-driven model. Handling 'hot mic' race conditions (re-checking state after permission grant) and ensuring resource cleanup (URL.revokeObjectURL) are critical for a production-ready feel.
**Action:** Always implement an 'isRecording' flag to synchronize multi-modal inputs and use CSS transitions for tactile-feeling buttons.
