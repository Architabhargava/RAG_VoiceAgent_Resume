## 2025-05-15 - Dynamic Button Labels and ARIA
**Learning:** Avoid using static 'aria-label' attributes on buttons with dynamic visible text (e.g., 'Push to Talk' vs 'Release to Send') as it overrides the dynamic content for screen readers; rely on 'textContent' or update 'aria-label' synchronously with text changes.
**Action:** Always verify if a button's purpose is already clear from its dynamic text before adding an 'aria-label' that might become stale.

## 2025-05-15 - Media Stream Lifecycle
**Learning:** Always explicitly stop all tracks of a MediaStream obtained via 'getUserMedia' (using 'stream.getTracks().forEach(track => track.stop())') when recording finishes to ensure the microphone is correctly released.
**Action:** Include track cleanup in all future voice interaction implementations to prevent 'hot mic' indicators staying active.
