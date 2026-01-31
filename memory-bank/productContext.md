# Product Context

## Purpose
The system helps players of Generation 3 Pokémon games build a balanced in-game team by automatically identifying Pokémon from uploaded PC box images and generating a recommended team using in-game logic. The focus is a low-friction user experience with minimal manual input and high identification reliability over competitive optimization.

## Target Users
- Players of Pokémon Ruby, Sapphire, Emerald, FireRed, and LeafGreen.
- Users on desktop or mobile browsers who can capture screenshots or phone photos of PC boxes.

## User Experience Goals
- Support multi-image uploads per session with a combined Pokémon pool.
- Provide automatic identification with optional corrections before recommendation.
- Generate a simple, clear explanation for why a team is recommended.
- Keep the flow fast (≤5 seconds processing) and resilient to partial failures.

## Scope and Constraints
- Only Gen 3 PC box screens in English UI; no ROM hacks or altered sprites.
- Eggs are excluded; shiny variants are treated as normal species; Unown forms are collapsed.
- No save parsing or competitive assumptions (IVs/EVs, held items, advanced metas).

## Success Criteria
- ≥95% Top-3 identification accuracy on acceptance data.
- Users can complete the flow without typing Pokémon names (post-ML milestone).
- A valid team recommendation is produced per session.