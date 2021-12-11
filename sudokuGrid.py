def create_grid(puzzle_str):
    # Deleting whitespaces and newlines (\n)
    lines = puzzle_str.replace(' ','').replace('\n','')
    # Converting it to a list of digits
    digits = list(map(int, lines))
    # Turning it to a 9x9 numpy array
    grid = np.array(digits).reshape(9,9)
    return grid
