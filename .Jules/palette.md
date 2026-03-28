# Palette's Journal - Resume RAG Voice Agent

## 2024-05-23 - Initial Project Assessment
**Learning:** The project uses a simple, single-file frontend (`index.html`) without a build system. This requires using standard CSS and vanilla JavaScript for all UX enhancements.
**Action:** Focus on improving the "Push to Talk" button's accessibility and interaction using standard web APIs.

## 2024-05-23 - Accessibility & CSS Specificity Refactor
**Learning:** Static `aria-label` attributes on buttons with dynamic text content (e.g., "Push to Talk" vs. "Release to Send") override the visible text for screen readers, leading to confusing states. Additionally, using ID-based selectors (`#recordBtn.recording`) is cleaner than `!important` for overriding base element styles.
**Action:** Always prefer dynamic `textContent` or update the `aria-label` alongside the text. Use specific selectors to manage state-based style overrides.
