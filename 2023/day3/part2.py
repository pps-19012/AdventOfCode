def create_array(filename):
    arr = []
    with open(filename, "r") as file:
        for line in file:
            temp = []
            for char in line:
                if char != "\n":
                    temp.append(char)
            arr.append(temp)
    return process_array(arr)


def process_array(arr):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    gears = {}
    m, n = len(arr), len(arr[0])
    for i in range(m):
        j = 0
        l, r = 0, 0
        while j < n:
            gearLocations = []
            if arr[i][j] in numbers:
                l = j
                # arr[i-1][l-1]       arr[i-1][l]
                # arr[i][l-1]         arr[i][l]
                # arr[i+1][l-1]       arr[i+1][l]
                if i - 1 >= 0:
                    if arr[i - 1][l] == "*":
                        gearLocations.append([i - 1, l])
                    if l - 1 >= 0 and arr[i - 1][l - 1] == "*":
                        gearLocations.append([i - 1, l - 1])
                if l - 1 >= 0 and arr[i][l - 1] == "*":
                    gearLocations.append([i, l - 1])
                if i + 1 < m:
                    if arr[i + 1][l] == "*":
                        gearLocations.append([i + 1, l])
                    if l - 1 >= 0 and arr[i + 1][l - 1] == "*":
                        gearLocations.append([i + 1, l - 1])
                j += 1
                while j < n and arr[i][j] in numbers:
                    # arr[i-1][j]
                    # arr[i][j]
                    # arr[i+1][j]
                    if i - 1 >= 0 and arr[i - 1][j] == "*":
                        gearLocations.append([i - 1, j])
                    if i + 1 < m and arr[i + 1][j] == "*":
                        gearLocations.append([i + 1, j])
                    j += 1

                r = j - 1
                # arr[i-1][r]       arr[i-1][r+1]
                # arr[i][r]         arr[i][r+1]
                # arr[i+1][r]       arr[i+1][r+1]
                if r + 1 < n and arr[i][r + 1] == "*":
                    gearLocations.append([i, r + 1])
                if i - 1 >= 0 and r + 1 < n and arr[i - 1][r + 1] == "*":
                    gearLocations.append([i - 1, r + 1])
                if i + 1 < m and r + 1 < n and arr[i + 1][r + 1] == "*":
                    gearLocations.append([i + 1, r + 1])

                num = int("".join(arr[i][l : r + 1]))
                for x, y in gearLocations:
                    if (x, y) not in gears:
                        gears[(x, y)] = []
                    gears[(x, y)].append(num)
            else:
                j += 1
    return process_gears(gears)


def process_gears(gears):
    # print(gears)
    tot = 0
    for k, v in gears.items():
        if len(v) == 2:
            # print(k)
            tot += v[0] * v[1]
    return tot


if __name__ == "__main__":
    file_path = "input.txt"
    ans = create_array(file_path)
    print(ans)
