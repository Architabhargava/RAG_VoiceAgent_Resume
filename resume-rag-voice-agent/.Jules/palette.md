## 2026-05-01 - Robust Push-to-Talk (PTT) Interaction
**Learning:** Implementing PTT with only mouse events is insufficient for touch devices and can lead to 'stuck' recording states if the user releases the pointer outside the button. Global keyboard listeners for Spacebar significantly improve accessibility for power users.
**Action:** Use `onpointerdown` on the target element combined with a window-level `onpointerup` listener for robust state termination. Always check `event.repeat` for keyboard shortcuts to prevent logic re-firing.
