def is_solution(grid):
    if np.all(np.sum(grid, axis=1) == 45) and \
       np.all(np.sum(grid, axis=0) == 45) and \
       np.all(np.sum(get_subgrids(grid), axis=1) == 45):
        return True
    return False
