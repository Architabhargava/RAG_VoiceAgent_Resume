## 2025-05-15 - Robust Push-to-Talk Pattern
**Learning:** A momentary interaction like "Push to Talk" requires multi-modal feedback (color, animation, text change) and multi-input support (mouse, keyboard Space bar) to feel reliable. Using  and  updates synchronously ensures accessibility for screen readers.
**Action:** Use a state flag (e.g., ) to synchronize mouse and keyboard events and prevent race conditions or duplicate starts in voice agents.
## 2025-05-15 - Robust Push-to-Talk Pattern
**Learning:** A momentary interaction like "Push to Talk" requires multi-modal feedback (color, animation, text change) and multi-input support (mouse, keyboard Space bar) to feel reliable. Using aria-pressed and textContent updates synchronously ensures accessibility for screen readers.
**Action:** Use a state flag (e.g., isRecording) to synchronize mouse and keyboard events and prevent race conditions or duplicate starts in voice agents.
