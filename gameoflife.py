import time
ROWS = 20
COLS = 30

def print_grid(grid, generation):
    print(f"\nGeneration {generation} : ")
    for row in grid:
        print(" ".join('$' if cell == 1 else '.' for cell in row))

def count_neighbors(grid, row, col):
    count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue  
            new_row = row + i
            new_col = col + j
                  
            if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col]==1:
                count += grid[new_row][new_col]
                
    return count

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    
max_generations = int(input("Enter the number of generations to run: "))

print(f"\nEnter the coordinates (Row and Column from 0 to 19) to place 1s.")
print("Type 'done' when you are finished setting up the grid.\n")
    
while True:
    user_input = input("Enter row and col (e.g., '5 5') or 'done': ").strip().lower()
    if user_input == 'done':
        break
            

    r_str, c_str = user_input.split()
    r, c = int(r_str), int(c_str)
            
    if 0 <= r < ROWS and 0 <= c < COLS:
        grid[r][c] = 1
        print(f"Placed a 1 at ({r}, {c})")
    else:
        print(f"Out of bounds! Rows must be 0-{ROWS-1} and columns must be 0-{COLS-1}.")
        

print_grid(grid, 0)
time.sleep(2)
for gen in range(1, max_generations + 1):
    next_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
    for r in range(ROWS):
        for c in range(COLS):
            neighbors = count_neighbors(grid, r, c)
                
            if grid[r][c] == 1:
                if neighbors == 2 or neighbors == 3:
                    next_grid[r][c] = 1
            else:
                if neighbors == 3:
                    next_grid[r][c] = 1
                        
    grid = next_grid
    print_grid(grid, gen)
        
    time.sleep(2)

print("\nSimulation complete.")