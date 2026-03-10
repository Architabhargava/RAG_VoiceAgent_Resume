
## 2025-05-14 - [Voice Interaction UX & Accessibility Improvements]
**Learning:** Real-time voice interfaces require immediate UI feedback to be perceived as responsive. Keyboard support (Space key) and mobile touch events are critical for accessibility and usability in "Push to Talk" systems. Mousing away from a held button should automatically cancel/stop the recording to prevent stuck states.
**Action:** Always include keyboard ('Space'), touch ('touchstart/end'), and 'mouseleave' listeners for voice-recording triggers. Use 'aria-live="polite"' for status updates and ensure interactive buttons have clear focus indicators and disabled states reflecting the backend connection status.
