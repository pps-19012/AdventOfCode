import math


def process_input(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            temp = line.split(" ")
            for i in range(len(temp)):
                temp[i] = int(temp[i])
            data.append(temp)
    return data


def extrapolate(data):
    tot = 0
    for eq in data:
        tot += find_next_term(eq)
    return tot


def find_next_term(eq):
    curr = eq
    rec = []
    while True:
        all_zero = True
        new = []
        for i in range(1, len(curr)):
            diff = curr[i] - curr[i - 1]
            if i == 1:
                rec.append((curr[i - 1]))
            if diff != 0:
                all_zero = False
            new.append(diff)
        if all_zero:
            break
        curr = new
    prev = 0
    for i in range(len(rec) - 1, -1, -1):
        prev = rec[i] - prev
    return prev


if __name__ == "__main__":
    file_path = "input.txt"
    data = process_input(file_path)
    ans = extrapolate(data)
    print(ans)
