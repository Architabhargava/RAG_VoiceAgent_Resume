## 2025-05-22 - [Push-to-Talk Accessibility & Feedback]
**Learning:** For "Push-to-Talk" interfaces, users benefit significantly from multi-modal triggers (keyboard 'Space' in addition to mouse hold) and immediate visual/aural feedback. Relying only on mouse events creates accessibility barriers and can lead to "stuck" states if the user's pointer leaves the button.
**Action:** Always implement `keydown`/`keyup` for the Space bar, use `aria-pressed` for state communication, and add an `onmouseleave` safety to ensure recording stops when the interaction area is exited.
