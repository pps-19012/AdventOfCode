def process_input(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            data.append(line)
    return data


def process_data(data, times):
    m, n = len(data), len(data[0])
    # True -> # found else False
    rows_present = [False] * m
    cols_present = [False] * n
    locs = []
    for i in range(m):
        for j in range(n):
            if data[i][j] == "#":
                rows_present[i] = True
                cols_present[j] = True
                locs.append([i, j])

    rows, cols = [0] * m, [0] * n
    for i in range(m):
        if not rows_present[i]:
            rows[i] = rows[i - 1] + times - 1
        else:
            rows[i] = rows[i - 1]
    for i in range(m):
        if not cols_present[i]:
            cols[i] = cols[i - 1] + times - 1
        else:
            cols[i] = cols[i - 1]

    for k in range(len(locs)):
        i, j = locs[k]
        i += rows[i]
        j += cols[j]
        locs[k] = [i, j]

    return locs


def find_dist(locs):
    tot_distance = 0
    for i in range(len(locs)):
        for j in range(i + 1, len(locs)):
            tot_distance += abs(locs[j][0] - locs[i][0]) + abs(locs[j][1] - locs[i][1])
    return tot_distance


if __name__ == "__main__":
    file_path = "input.txt"
    data = process_input(file_path)
    locations = process_data(data, 2)
    ans = find_dist(locations)
    print(ans)
