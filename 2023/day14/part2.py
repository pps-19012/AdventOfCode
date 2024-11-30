import part1 as p1


def rotate(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [["x" for _ in range(rows)] for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            new_grid[c][rows - 1 - r] = grid[r][c]
    return new_grid


def roll(grid):
    rows, cols = len(grid), len(grid[0])
    for c in range(cols):
        for _ in range(rows):
            for r in range(rows):
                if grid[r][c] == "O" and grid[r - 1][c] == ".":
                    grid[r][c] = "."
                    grid[r - 1][c] = "O"
    return grid


def perform_cycles(grid):
    grids = dict()
    t, target = 1, 10**9
    while t <= target:
        for _ in range(4):
            grid = rotate(roll(grid))
        grid_tuple = tuple(tuple(row) for row in grid)
        if grid_tuple in grids:
            cycle_length = t - grids[grid_tuple]
            repetitions = (target - t) // cycle_length
            # print(repetitions, cycle_length, grids[grid_tuple], t)
            t += repetitions * cycle_length
        grids[grid_tuple] = t
        # print(t)
        t += 1
    return grid


def calc_load(grid):
    ans = 0
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "O":
                ans += rows - r
    return ans


if __name__ == "__main__":
    file_path = "test_input.txt"
    data = p1.process_input(file_path)
    final = perform_cycles(data)
    ans = calc_load(final)
    print(ans)
