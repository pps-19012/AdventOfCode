def process_input(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            temp = []
            for i in line:
                temp.append(i)
            data.append(temp)
    return data


# combinations:
# prev => O O O # # # . . .
# curr => . # O # O . O # .


def calc_north(data):
    m, n = len(data), len(data[0])
    calc = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            curr = data[i][j]
            if i == 0:
                if curr == "O":
                    calc[i][j] = n - i
                elif curr == "#":
                    calc[i][j] = 0
                elif curr == ".":
                    calc[i][j] = n - i
                continue

            prev = data[i - 1][j]
            if curr == "O" and prev == "#":
                calc[i][j] = n - i
            elif curr == "O" and prev == ".":
                calc[i][j] = calc[i - 1][j]
            elif curr == "O" and prev == "O":
                calc[i][j] = calc[i - 1][j] - 1
            elif curr == "#":
                calc[i][j] = 0
            elif curr == "." and prev == "O":
                calc[i][j] = calc[i - 1][j] - 1
            elif curr == "." and prev == "#":
                calc[i][j] = n - i
            elif curr == "." and prev == ".":
                calc[i][j] = calc[i - 1][j]

    tot = 0
    for i in range(m):
        for j in range(n):
            if data[i][j] == "O":
                tot += calc[i][j]
    return tot


if __name__ == "__main__":
    file_path = "input.txt"
    data = process_input(file_path)
    ans = calc_north(data)
    print(ans)
