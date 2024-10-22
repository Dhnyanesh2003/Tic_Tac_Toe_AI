Tic Tac Toe Game
Overview
This is a simple yet engaging Tic Tac Toe game implemented in Python using the Tkinter library for the graphical user interface (GUI). The game allows players to challenge an AI with three difficulty levels: Simple, Moderate, and Hard. The AI uses the Minimax algorithm in the hard mode to provide a challenging experience.

Features
Two Game Modes: Play against the AI or a friend (currently set to AI mode).
AI Difficulty Levels:
Simple: Random moves.
Moderate: Blocks player from winning.
Hard: Uses Minimax algorithm for optimal play.
User-Friendly GUI: Interactive buttons for each cell, making the game easy to play.
Game Status Display: Shows the current game state (win, loss, draw).
Requirements
Python 3.x
Tkinter (usually included with Python installations)
Installation

Clone this repository:
git clone https://github.com/Dhnyanesh2003/tic-tac-toe.git

Choose to play against the AI. Click on the buttons to make your moves. The AI will respond according to the selected difficulty level.
How It Works
The game board is represented as a 3x3 grid.
Players take turns clicking buttons to place their marks (X for player, O for AI).
After each move, the game checks for a win condition or a draw.
The AI selects its moves based on the difficulty level chosen.
