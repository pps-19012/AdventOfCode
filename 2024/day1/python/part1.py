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


def tot_distance(left, right):
    left.sort()
    right.sort()
    n = len(left)

    tot_dist = 0
    for i in range(n):
        tot_dist += abs(left[i] - right[i])
    return tot_dist


if __name__ == "__main__":
    filename = "input1.txt"
    data = process_input(filename)
    l1, l2 = get_list(data)
    print(tot_distance(l1, l2))
