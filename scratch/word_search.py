import random

# Example words to include in the word search
words = ["PYTHON", "SCRIPT", "WORD", "SEARCH", "PUZZLE"]

def generate_word_search(words, size=10):
    # Create an empty grid
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    
    directions = [
        (0, 1),     #right
        (1, 0),     #down
        (1, 1),     #diagonal down-right
        (0, -1),    #left
        (-1, 0),    #up
        (-1, -1),   #diagonal up-left
        (-1, 1),    #diagonal up-right
        (1, -1)     #diagonal down-left
        ]
    
    for word in words:
        word_length = len(word)
        placed = False
        
        while not placed:
            direction = random.choice(directions)
            if direction in [(0, 1), (0, -1)]:  # horizontal
                row = random.randint(0, size - 1)
                col = random.randint(0, size - word_length)
            elif direction in [(1, 0), (-1, 0)]:  # vertical
                row = random.randint(0, size - word_length)
                col = random.randint(0, size - 1)
            else:  # diagonal
                row = random.randint(0, size - word_length)
                col = random.randint(0, size - word_length)
            
            # Check if the word fits
            fits = True
            for i in range(word_length):
                new_row = row + i * direction[0]
                new_col = col + i * direction[1]
                if new_row < 0 or new_row >= size or new_col < 0 or new_col >= size or grid[new_row][new_col] not in (' ', word[i]):
                    fits = False
                    break
            
            if fits:
                for i in range(word_length):
                    grid[row + i * direction[0]][col + i * direction[1]] = word[i]
                placed = True
    
    # Fill empty spaces with random letters
    for row in range(size):
        for col in range(size):
            if grid[row][col] == ' ':
                grid[row][col] = chr(random.randint(65, 90))  # A-Z
    
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

# Generate the word search grid
word_search_grid = generate_word_search(words)

# Print the word search grid
print_grid(word_search_grid)