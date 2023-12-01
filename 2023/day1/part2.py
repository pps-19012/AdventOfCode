def find_sum(filename):
    tot = 0
    with open(filename, "r") as file:
        for line in file:
            tot += find_two_digit_num(line)
    return tot


def find_two_digit_num(line):
    digits_char = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    l, r, n = 0, len(line) - 1, len(line)
    l_found, r_found = False, False
    num = 0
    while l < n:
        if line[l].isnumeric():
            l_found = True
            first_digit = int(line[l])
            break
        for i in range(9):
            dig_len = len(digits_char[i])
            if l + dig_len - 1 <= n - 1 and line[l : l + dig_len] == digits_char[i]:
                l_found = True
                first_digit = i + 1
                break
        if l_found:
            break
        l += 1
    while r >= 0:
        if line[r].isnumeric():
            r_found = True
            second_digit = int(line[r])
            break
        for i in range(9):
            dig_len = len(digits_char[i])
            if r - dig_len + 1 >= 0 and line[r - dig_len + 1 : r + 1] == digits_char[i]:
                r_found = True
                second_digit = i + 1
                break
        if r_found:
            break
        r -= 1
    num = 10 * first_digit + second_digit
    return num


if __name__ == "__main__":
    file_path = "input.txt"
    ans = find_sum(file_path)
    print(ans)
