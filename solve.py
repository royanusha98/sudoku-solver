def solve(grid):
    grid = fill_singles(grid)
    if is_solution(grid):
        return grid
    if not is_valid_grid(grid):
        return None
    return make_guess(grid)
