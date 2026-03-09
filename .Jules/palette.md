## 2025-05-15 - [Push-to-Talk Micro-UX Improvements]
**Learning:** For 'Push to Talk' buttons, implementing a `mouseleave` event listener is critical to prevent the recording state from getting stuck if the user drags their cursor off the button. Additionally, mapping the `Space` key provides essential keyboard accessibility.
**Action:** Always include `mouseleave` and keyboard listeners (Space/Enter) when building press-and-hold interaction patterns. Use `aria-live="polite"` for status updates to ensure screen reader users are aware of the recording state change.
