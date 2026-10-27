# CECS 450 Data Visualization Project - Deadlock
This project analyzes data about the 1000 most recent matches of Deadlock, an online multiplayer game created by Valve.

In the game, 12 total players (6 per team) each select a unique character (or "hero") with their own set of abilities, and ultimately fight to break into each others' bases. To successfully do so they must earn enough money to purchase items that increase their strength. Money can be made in multiple ways: killing other players and non-player characters, breaking boxes around the map, and doing specific objectives around the map, just to name a few. 

Deadlock is an incredibly intricate game with a lot of moving parts, and as such there is a large amount of data to look at in any given match. There are 3 main numeric variables this project will be analyzing, as well as 2 categorical variable.

<b>For each player, we will analyze:
- Net worth at end of game (numerical)
- Kill / Death Ratio (numerical)
- Character played (categorical)
- Part of winning team (categorical)

Additionally, for each match, we will analyze its length.</b>

---
### Files
- <b>format_heroes.py</b>: Python file that retrieves the list of heroes from the Deadlock API, then produces a stripped down version used for mapping character names to their numerical IDs. <b>Run this first.</b>
- <b>generate_csv.ipynb</b>: Jupyter notebook for retrieving data from recent matches and formatting / saving to a CSV file. <b>Run this after format_heroes.</b>
- <b>wtf.json</b>: A single match's data used for testing and API reference. There's also a great story being told by numbers in this thing.