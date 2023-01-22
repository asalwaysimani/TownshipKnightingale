---
title: Project Knightingale Township Read Me
description: "Exactly what it says on the tin"
---

## Key Features

- Town building with various required & optional buildings
  - Upgradable buildings
- Resoruce gathering
  - Resouce mangement
- Quest System via NPC posting on town message board
- Quest System via NPC visiting tavern
- Hero collection via heroes visting tavern

### Town Management

Information Coming Soon

### Hero Collection

- Heroes all start at the same base tier
- Hero rarity tied to town level
  > The higher level your town the more rare heroes will appear in the tavern.

### Dungeon Exploration

Information Coming Soon

## Gameplay Loop

```mermaid
graph TD
    A[Establish Town] --> B1[New NPC visits] --> 
    D1(Request Item/Building/Upgrade) --> C1(Job Notice Posted) --> D2
    D2[New Hero visits] --> C2(Looks for Work) --> |Assemble Hero Team| D3(Explore Dugeon) -->
    E1(Hero Team Fails) --> E3(Hero Team Returns) --> B2(NPC Leaves Township) -->B1
    D3 --> E2(Hero Team Succesful) --> |Returns with additional loot| E3 --> R1[Add Building to Town] --> B3(NPC Settles in Township)
```

## Around The Internet

- Follow the development of [Project Knightingale Township](https://open.codecks.io/knightingale-township)
- Find my games on Itch.io under [Margaret Cattter Development](https://margaretcatter.itch.io/)
- Keep update on my projects on Cohost under [As Always Imani](https://cohost.org/asalwaysimani)
- Support my projects by buying me milk & cookies on Ko-fi under [As Always Imani](https://ko-fi.com/asalwaysimani)
- Follow my general creative account [As Always Imani on Twitter](https://twitter.com/asalwaysimani)
