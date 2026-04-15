## 2025-05-15 - Robust Push-to-Talk Interaction Pattern
**Learning:** For "Push-to-Talk" interfaces, attaching the "stop" listener to the `window` (mouseup) instead of the button itself prevents the "stuck recording" bug if the user moves their mouse away before releasing. Additionally, implementing `Space` bar shortcuts and touch events ensures a truly multi-modal and accessible experience.
**Action:** Always use global listeners for releasing "hold" interactions and ensure state-sync between keyboard, mouse, and touch events.
