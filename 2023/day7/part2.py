import part1 as p1
from collections import Counter


# rank7: 5 = 5, 4 + 1J, 3 + 2J, 2 + 3J, 1 + 4J
# rank6: 4 = 4 + 1, 3 + 1J + 1, 2 + 2J + 1, 1 + 3J + 1,
# rank5: 3 + 2 = 3 + 2, 2 + 2 + 1J
# rank4: 3 = 3, 1 + 2J + 1 + 1, 2 + 1J + 1 + 1
# rank3: 2 + 2 = 2 + 2 + 1
# rank2: 2 = 2 + 1 + 1 + 1, 1 + 1J + 1 + 1 + 1
# rank1: 1 = 1 + 1 + 1 + 1 + 1
def find_rank(hand):
    counter = Counter(hand)
    count_of_j = counter["J"]
    val = []
    for k, v in counter.items():
        if k != "J":
            val.append(v)
    val.sort()
    if len(counter) == 1:
        rank = 7
    elif len(counter) == 2:
        if count_of_j == 0:
            if val[1] == 4:
                rank = 6
            elif val[0] == 2 and val[1] == 3:
                rank = 5
        else:
            rank = 7
    elif len(counter) == 3:
        if count_of_j == 0:
            if val[2] == 3:
                rank = 4
            if val[1] == 2 and val[2] == 2:
                rank = 3
        else:
            if (
                (count_of_j == 3)
                or (count_of_j == 2 and val[-1] == 2)
                or (count_of_j == 1 and val[-1] == 3)
            ):
                rank = 6
            elif count_of_j == 1 and val[1] == 2:
                rank = 5

    elif len(counter) == 4:
        if count_of_j == 0:
            rank = 2
        else:
            if (count_of_j == 2 and val[-1] == 1) or (count_of_j == 1 and val[-1] == 2):
                rank = 4
    else:
        if count_of_j == 0:
            rank = 1
        else:
            rank = 2
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
        "J": "n",
        "2": "m",
        "3": "l",
        "4": "k",
        "5": "j",
        "6": "i",
        "7": "h",
        "8": "g",
        "9": "f",
        "T": "e",
        "Q": "c",
        "K": "b",
        "A": "a",
    }
    new = ""
    for i in hand_str:
        new += strength[i]
    return new


if __name__ == "__main__":
    file_path = "input.txt"
    data = p1.process_input(file_path)
    n = len(data)
    order = [[] for _ in range(7)]
    for k, v in data.items():
        raw_rank = find_rank(k) - 1
        order[raw_rank].append(k)
    for i in range(len(order)):
        o = order[i]
        if len(o) > 1:
            order[i] = sort_rank(o)
    ans = p1.total_winnings(order, n, data)
    print(ans)
