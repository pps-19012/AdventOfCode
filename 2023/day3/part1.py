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
    tot = 0
    m, n = len(arr), len(arr[0])
    for i in range(m):
        j = 0
        l, r = 0, 0
        while j < n:
            symbolFound = False
            if arr[i][j] in numbers:
                l = j
                # arr[i-1][l-1]       arr[i-1][l]
                # arr[i][l-1]         arr[i][l]
                # arr[i+1][l-1]       arr[i+1][l]
                if i - 1 >= 0:
                    if arr[i - 1][l] not in numbers and arr[i - 1][l] != ".":
                        symbolFound = True
                    if (
                        l - 1 >= 0
                        and arr[i - 1][l - 1] not in numbers
                        and arr[i - 1][l - 1] != "."
                    ):
                        symbolFound = True
                if l - 1 >= 0 and arr[i][l - 1] not in numbers and arr[i][l - 1] != ".":
                    symbolFound = True
                if i + 1 < m:
                    if arr[i + 1][l] not in numbers and arr[i + 1][l] != ".":
                        symbolFound = True
                    if (
                        l - 1 >= 0
                        and arr[i + 1][l - 1] not in numbers
                        and arr[i + 1][l - 1] != "."
                    ):
                        symbolFound = True
                j += 1
                while j < n and arr[i][j] in numbers:
                    # arr[i-1][j]
                    # arr[i][j]
                    # arr[i+1][j]
                    if i - 1 >= 0:
                        if arr[i - 1][j] not in numbers and arr[i - 1][j] != ".":
                            symbolFound = True
                    if i + 1 < m:
                        if arr[i + 1][j] not in numbers and arr[i + 1][j] != ".":
                            symbolFound = True
                    j += 1

                r = j - 1
                # arr[i-1][r]       arr[i-1][r+1]
                # arr[i][r]         arr[i][r+1]
                # arr[i+1][r]       arr[i+1][r+1]
                if i - 1 >= 0:
                    if arr[i - 1][r] not in numbers and arr[i - 1][r] != ".":
                        symbolFound = True
                    if (
                        r + 1 < n
                        and arr[i - 1][r + 1] not in numbers
                        and arr[i - 1][r + 1] != "."
                    ):
                        symbolFound = True
                if r + 1 < n and arr[i][r + 1] not in numbers and arr[i][r + 1] != ".":
                    symbolFound = True
                if i + 1 < m:
                    if arr[i + 1][r] not in numbers and arr[i + 1][r] != ".":
                        symbolFound = True
                    if (
                        r + 1 < n
                        and arr[i + 1][r + 1] not in numbers
                        and arr[i + 1][r + 1] != "."
                    ):
                        symbolFound = True
                if symbolFound:
                    num = "".join(arr[i][l : r + 1])
                    # print(int(num))
                    tot += int(num)
            else:
                j += 1
    return tot


if __name__ == "__main__":
    file_path = "input.txt"
    ans = create_array(file_path)
    print(ans)
