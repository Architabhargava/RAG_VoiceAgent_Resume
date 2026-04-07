# Palette's UX Journal

## 2025-05-14 - Robust Push-to-Talk Interactions
**Learning:** Using only `onmousedown` and `onmouseup` for voice recording interfaces often leads to "stuck" recording states if the user moves their cursor off the button before releasing. Keyboard accessibility is also frequently overlooked in these patterns.
**Action:** Always implement `mouseleave` and `keyup` (Space) listeners alongside mouse events, and use global `mouseup` listeners to ensure state cleanup regardless of where the interaction ends.
