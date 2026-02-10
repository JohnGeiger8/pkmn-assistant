# Product Context

## Purpose
The system helps players of Generation 3 Pokémon games build a balanced in-game team by parsing uploaded save files to extract owned Pokémon and generating a recommended team using in-game logic. The focus is a low-friction user experience with minimal manual input and high data correctness over competitive optimization.

## Target Users
- Players of Pokémon Ruby, Sapphire, Emerald, FireRed, and LeafGreen.
- Users on desktop or mobile browsers who can upload save files from supported emulators or devices.

## User Experience Goals
- Support save file uploads per session with a combined Pokémon pool from party and PC.
- Provide inventory review with optional exclusions before recommendation.
- Generate a simple, clear explanation for why a team is recommended.
- Keep the flow fast (≤5 seconds processing) and resilient to partial failures.

## Scope and Constraints
- Only Gen 3 English-language save formats; no ROM hacks.
- Eggs are treated as their hatch species when available in save parsing; shiny variants are treated as normal species; Unown forms are collapsed.
- No competitive assumptions (IVs/EVs, held items, advanced metas).

## Success Criteria
- Users can complete the flow without typing Pokémon names or manually entering Pokémon data.
- Save parsing accurately extracts party and PC Pokémon.
- A valid team recommendation is produced per session.