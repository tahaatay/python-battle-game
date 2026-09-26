# PDungeon Chaos - Python RPG

# Dungeon Chaos - Python RPG

A terminal-based RPG written in Python.

Fight different enemies, upgrade your equipment, use potions, earn gold and points, and try to survive the chaos of the dungeon.

## Features

- ⚔️ Turn-based combat system
- 👾 5 different enemies
- 💰 Gold and score system
- 🧪 Health and strength potions
- 🗡️ Sword upgrades
- 🛡️ Shield upgrades
- 🏪 In-game shop
- 🎲 Random "Death Dice" event
- 🏆 Scoreboard system
- 📊 Score visualization with Matplotlib
- 💀 Loss counter
- 🎨 Colored terminal output with Colorama

## Enemies

| Enemy | Health | Damage | Gold | Score |
|-------|--------|--------|------|-------|
| Rat | 60 | 7 | 10 | 5 |
| Kangal | 95 | 16 | 25 | 12 |
| Goblin | 125 | 21 | 30 | 15 |
| Orc | 150 | 25 | 40 | 20 |
| Dragon | 275 | 30 | 1000 | 50 |

## Equipment

### Sword
Upgrading the sword increases the damage dealt to enemies.

### Shield
Upgrading the shield reduces incoming damage.

Both the sword and shield have 3 upgrade levels.

## Potions

There are two types of potions:

- **Health Potion** - Restores health.
- **Strength Potion** - Increases the damage of the next attack.

Potions can also be purchased from the shop.

## Random Events

The game includes a random event called **Death Dice**.

It can change the player's or enemy's health and may also activate a potion effect.

## Scoreboard

When the adventure ends, the player's score is saved to `skor.txt`.

Scores are loaded, sorted from highest to lowest, and displayed as a leaderboard.

The game also creates a bar chart using Matplotlib.

## Loss Counter

Player losses are stored in `kayiplar.txt`.

The counter is updated whenever the player loses the adventure.

## Requirements

Python 3.x

Install the required libraries:

```bash
pip install colorama matplotlib
colorama
