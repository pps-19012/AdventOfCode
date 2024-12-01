import collections


def process_input(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line)
    return data


def get_list(data):
    l1, l2 = [], []
    for l in data:
        l, r = l.split()
        l1.append(int(l))
        l2.append(int(r))
    return (l1, l2)


def get_similarity(left, right):
    l = collections.Counter(left)
    r = collections.Counter(right)

    tot_score = 0
    for k, v in l.items():
        tot_score += k * v * r[k]
    return tot_score


if __name__ == "__main__":
    filename = "input1.txt"
    data = process_input(filename)
    l1, l2 = get_list(data)
    print(get_similarity(l1, l2))
