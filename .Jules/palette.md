# Palette's Journal - Resume RAG Voice Agent

## 2025-03-14 - Accessible Push-to-Talk Pattern
**Learning:** For voice-based interfaces, a "Push to Talk" button requires multiple interaction triggers (mouse, touch, keyboard) and robust state management (ARIA attributes, visual feedback, MediaStream cleanup).
**Action:** Implement Space bar support, `aria-pressed`, `aria-live` for status, and ensure `MediaStream` tracks are stopped to release the microphone.
