# Conway's Game of Life (Python Terminal Implementation)

This is a simple, matrix-based command-line implementation of John Conway's famous **Game of Life** built using Python. The game simulates a cellular automaton on a fixed-size 2D grid where an initial pattern evolves over generations based on simple rules of survival, death, and reproduction.

## Features & Mechanics
- **Grid Size:** Fixed 20x30 matrix (20 Rows, 30 Columns).
- **Cell Representations:** - `.` represents a **Dead** cell.
  - `$` represents an **Alive** cell.
- **Timing:** A fixed **2-second delay** is enforced between every single generation so you can easily observe the pattern changes.
- **Continuous Print:** Generations are printed sequentially in the terminal without clearing the screen, allowing you to scroll back and track history.

---

## How the Rules Work
Every generation calculation evaluates the 8 surrounding neighbors of each individual cell:
1. **Underpopulation:** A live cell (`$`) with fewer than 2 live neighbors dies.
2. **Survival:** A live cell (`$`) with 2 or 3 live neighbors lives on.
3. **Overpopulation:** A live cell (`$`) with more than 3 live neighbors dies.
4. **Reproduction:** A dead cell (`.`) with exactly 3 live neighbors becomes a live cell (`$`).

---

## Prerequisites
You only need **Python 3.x** installed on your system. No external libraries or modules are required (the script uses the built-in `time` module).

---

## How to Run the Code

1. Copy the Python code and save it in a file named `game_of_life.py`.
2. Open your terminal or command prompt.
3. Navigate to the folder where you saved the file.
4. Run the script using the following command:
   ```bash
   python game_of_life.py
