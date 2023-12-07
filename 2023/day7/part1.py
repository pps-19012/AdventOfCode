from collections import Counter


def process_input(filename):
    data = {}
    with open(filename, "r") as file:
        for line in file:
            temp = line.split(" ")
            data[temp[0]] = int(temp[1])
    return data


# 7 ranks: 5, 4 + 1, 3 + 2, 3 + 1 + 1, 2 + 2 + 1, 2 + 1 + 1 + 1, distinct
#        : 7,     6,   5  ,     4    ,   3      ,      2       ,    1
def find_rank(hand):
    counter = Counter(hand)
    if len(counter) == 1:
        rank = 7
    elif len(counter) == 2:
        val = []
        for v in counter.values():
            val.append(v)
        val.sort()
        if val[1] == 4:
            rank = 6
        elif val[0] == 2 and val[1] == 3:
            rank = 5
    elif len(counter) == 3:
        val = []
        for v in counter.values():
            val.append(v)
        val.sort()
        if val[2] == 3:
            rank = 4
        if val[1] == 2 and val[2] == 2:
            rank = 3
    elif len(counter) == 4:
        rank = 2
    else:
        rank = 1
    return rank


def sort_rank(arr):
    new_arr = []
    for hand in arr:
        new_arr.append([encode(hand), hand])
    new_arr.sort()
    arr = []
    for i in range(len(new_arr)):
        arr.append(new_arr[i][1])
    return arr


def encode(hand_str):
    strength = {
        "2": "m",
        "3": "l",
        "4": "k",
        "5": "j",
        "6": "i",
        "7": "h",
        "8": "g",
        "9": "f",
        "T": "e",
        "J": "d",
        "Q": "c",
        "K": "b",
        "A": "a",
    }
    new = ""
    for i in hand_str:
        new += strength[i]
    return new


def total_winnings(order, n, data):
    tot, rank = 0, n
    for i in range(len(order) - 1, -1, -1):
        if len(order[i]) > 0:
            for j in order[i]:
                tot += data[j] * rank
                rank -= 1
    return tot


if __name__ == "__main__":
    file_path = "input.txt"
    data = process_input(file_path)
    n = len(data)
    order = [[] for _ in range(7)]
    for k, v in data.items():
        raw_rank = find_rank(k) - 1
        order[raw_rank].append(k)
    for i in range(len(order)):
        o = order[i]
        if len(o) > 1:
            order[i] = sort_rank(o)
    ans = total_winnings(order, n, data)
    print(ans)
