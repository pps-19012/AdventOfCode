def find_sum(filename):
    tot = 0
    with open(filename, "r") as file:
        for line in file:
            tot += find_two_digit_num(line)
    return tot


def find_two_digit_num(line):
    l, r, n = 0, len(line) - 1, len(line)
    num = 0
    while l < n:
        if line[l].isnumeric():
            break
        l += 1
    while r >= 0:
        if line[r].isnumeric():
            break
        r -= 1
    num = 10 * int(line[l]) + int(line[r])
    return num


if __name__ == "__main__":
    file_path = "input.txt"
    ans = find_sum(file_path)
    print(ans)
