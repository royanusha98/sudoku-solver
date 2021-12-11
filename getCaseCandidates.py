def get_candidates(grid):
    # Helper function
    def subgrid_index(i, j):
        return (i//3) * 3 + j // 3
    subgrids = get_subgrids(grid)
    candidates = []
    for i in range(9):
        row_candidates = []
        for j in range(9):
            # Row, column and subgrid digits
            row = set(grid[i])
            col = set(grid[:, j])
            sub = set(subgrids[subgrid_index(i, j)])
            common = row | col | sub
            candidates = set(range(10)) - common
            # If the case is filled take its value as the only candidate
            if not grid[i][j]:
                row_candidates.append(list(candidates))
            else:
                row_candidates.append([grid[i][j]])
        candidates.append(row_candidates)
    return candidates
