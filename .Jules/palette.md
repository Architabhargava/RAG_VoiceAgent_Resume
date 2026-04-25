## 2025-05-15 - [Accessible Voice Interaction]
**Learning:** For voice-based "Push to Talk" interfaces, synchronizing visible text, ARIA attributes (aria-pressed), and keyboard shortcuts (Space bar) provides a cohesive experience for both visual and screen-reader users. Preventing default behavior on Space bar is critical to avoid accidental page scrolling.
**Action:** Always implement a unified state management for recording intent that bridges mouse, touch, and keyboard events, and ensure 'isRecordingIntent' is re-verified after async microphone permissions are granted.
