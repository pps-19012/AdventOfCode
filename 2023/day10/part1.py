def process_input(filename):
    data = []
    with open(filename, "r") as file:
        (x_idx, y_idx) = (0, 0)
        idx = 0
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            temp = []
            for i in line:
                temp.append(i)
            data.append(temp)
            if "S" in line:
                x_idx, y_idx = idx, line.index("S")
            idx += 1
    return (data, x_idx, y_idx)


def choose_replacement(maze, r, c):
    m, n = len(maze), len(maze[0])
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    valid = [0, 0, 0, 0]  # N S E W
    for dr, dc in dir:
        if (dr, dc) == (1, 0):
            new_r, new_c = r + dr, c + dc
            if new_r in range(m) and new_c in range(n) and maze[new_r][new_c] in "|LJ":
                valid[1] = 1
        if (dr, dc) == (-1, 0):
            new_r, new_c = r + dr, c + dc
            if new_r in range(m) and new_c in range(n) and maze[new_r][new_c] in "|7F":
                valid[0] = 1
        if (dr, dc) == (0, 1):
            new_r, new_c = r + dr, c + dc
            if new_r in range(m) and new_c in range(n) and maze[new_r][new_c] in "-J7":
                valid[2] = 1
        if (dr, dc) == (0, -1):
            new_r, new_c = r + dr, c + dc
            if new_r in range(m) and new_c in range(n) and maze[new_r][new_c] in "LF-":
                valid[3] = 1
    # print(valid)
    if valid[0] and valid[1]:
        return "|"
    elif valid[2] and valid[3]:
        return "-"
    elif valid[0] and valid[2]:
        return "L"
    elif valid[0] and valid[3]:
        return "J"
    elif valid[1] and valid[2]:
        return "F"
    elif valid[1] and valid[3]:
        return "7"


def max_step(maze, x, y):
    m, n = len(maze), len(maze[0])
    # dist = [[0 for _ in range(n)] for _ in range(m)]
    maze[x][y] = choose_replacement(maze, x, y)
    visit = set()
    q = [(x, y, 0)]
    visit.add((x, y))
    max_val = 0
    while q:
        r, c, steps = q.pop(0)
        # dist[r][c] = steps
        max_val = max(max_val, steps)
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if maze[r][c] == "|":
            for dr, dc in dir:
                if ((dr, dc) == (1, 0)) or ((dr, dc) == (-1, 0)):
                    new_r, new_c = r + dr, c + dc
                    if (
                        new_r in range(m)
                        and new_c in range(n)
                        and maze[new_r][new_c] != "."
                        and (new_r, new_c) not in visit
                    ):
                        q.append((new_r, new_c, steps + 1))
                        visit.add((new_r, new_c))
        if maze[r][c] == "-":
            for dr, dc in dir:
                if ((dr, dc) == (0, 1)) or ((dr, dc) == (0, -1)):
                    new_r, new_c = r + dr, c + dc
                    if (
                        new_r in range(m)
                        and new_c in range(n)
                        and maze[new_r][new_c] != "."
                        and (new_r, new_c) not in visit
                    ):
                        q.append((new_r, new_c, steps + 1))
                        visit.add((new_r, new_c))
        if maze[r][c] == "L":
            for dr, dc in dir:
                if ((dr, dc) == (0, 1)) or ((dr, dc) == (-1, 0)):
                    new_r, new_c = r + dr, c + dc
                    if (
                        new_r in range(m)
                        and new_c in range(n)
                        and maze[new_r][new_c] != "."
                        and (new_r, new_c) not in visit
                    ):
                        q.append((new_r, new_c, steps + 1))
                        visit.add((new_r, new_c))
        if maze[r][c] == "J":
            for dr, dc in dir:
                if ((dr, dc) == (0, -1)) or ((dr, dc) == (-1, 0)):
                    new_r, new_c = r + dr, c + dc
                    if (
                        new_r in range(m)
                        and new_c in range(n)
                        and maze[new_r][new_c] != "."
                        and (new_r, new_c) not in visit
                    ):
                        q.append((new_r, new_c, steps + 1))
                        visit.add((new_r, new_c))
        if maze[r][c] == "7":
            for dr, dc in dir:
                if ((dr, dc) == (0, -1)) or ((dr, dc) == (1, 0)):
                    new_r, new_c = r + dr, c + dc
                    if (
                        new_r in range(m)
                        and new_c in range(n)
                        and maze[new_r][new_c] != "."
                        and (new_r, new_c) not in visit
                    ):
                        q.append((new_r, new_c, steps + 1))
                        visit.add((new_r, new_c))
        if maze[r][c] == "F":
            for dr, dc in dir:
                if ((dr, dc) == (0, 1)) or ((dr, dc) == (1, 0)):
                    new_r, new_c = r + dr, c + dc
                    if (
                        new_r in range(m)
                        and new_c in range(n)
                        and maze[new_r][new_c] != "."
                        and (new_r, new_c) not in visit
                    ):
                        q.append((new_r, new_c, steps + 1))
                        visit.add((new_r, new_c))
    # for e in dist:
    #     print(e)
    return (max_val, visit)


if __name__ == "__main__":
    file_path = "input.txt"
    maze, x, y = process_input(file_path)
    ans, visit = max_step(maze, x, y)
    print(ans)
