import part1 as p1


def make_new_grid(maze, visit):
    m, n = len(maze), len(maze[0])
    for r in range(m):
        for c in range(n):
            if (r, c) not in visit:
                maze[r][c] = "."
    outside = set()
    for r in range(m):
        within = False
        up = None
        for c in range(n):
            if maze[r][c] == "|":
                within = not within
            elif maze[r][c] in "LF":
                up = maze[r][c] == "L"
            elif maze[r][c] in "7J":
                if maze[r][c] != ("J" if up else "7"):
                    within = not within
                up = None
            elif maze[r][c] == ".":
                pass
            if not within:
                outside.add((r, c))
    return outside


if __name__ == "__main__":
    file_path = "input.txt"
    maze, x, y = p1.process_input(file_path)
    max_step, visit = p1.max_step(maze, x, y)
    outside = make_new_grid(maze, visit)
    ans = len(maze) * len(maze[0]) - len(outside | visit)
    print(ans)
