## 2025-05-14 - [Accessible Voice Interaction]
**Learning:** For "Push to Talk" interfaces, keyboard accessibility (Space/Enter) and robust state management (stopping recording even if mouse leaves button) are critical for both UX and accessibility. Adding `aria-live` to status indicators ensures screen reader users are kept in the loop during async operations.
**Action:** Always implement keyboard listeners alongside mouse events for interactive elements and use `aria-pressed` for toggle/hold states.
