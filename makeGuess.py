def make_guess(grid):
    grid = grid.copy()
    candidates = get_candidates(grid)
    # Getting the shortest number of candidates > 1:
    min_len = sorted(list(set(map(
        len, np.array(candidates).reshape(1,81)[0]))))[1]
    for i in range(9):
        for j in range(9):
            if len(candidates[i][j]) == min_len:
                for guess in candidates[i][j]:
                    grid[i][j] = guess
                    solution = solve(grid)
                    if solution is not None:
                        return solution
                    # Discarding incorrect guess
                    grid[i][j] = 0
