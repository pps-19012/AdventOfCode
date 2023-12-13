def process_input(filename):
    data = []
    temp = []
    with open(filename, "r") as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            if line == "":
                data.append(temp)
                temp = []
                continue
            temp.append(line)
        data.append(temp)

    for k in range(len(data)):
        d = data[k]
        m, n = len(d), len(d[0])
        temp = []
        for j in range(n):
            t = []
            for i in range(m):
                t.append(d[i][j])
            temp.append("".join(t))
        data[k] = [d, temp]
    return data


def find_ref_point(arr):
    n = len(arr)
    for i in range(1, n):
        isMirror = True
        for j in range(i):
            opp = 2 * i - j - 1
            # print("j:", j, " | opp:", opp)
            if opp < n and arr[j] != arr[opp]:
                # print(arr[j], " ===> ", arr[opp])
                isMirror = False
            if not isMirror:
                break
        if isMirror:
            # print("mirror:", i - 1)
            return i
    # print("no mirror")
    return 0


if __name__ == "__main__":
    file_path = "input.txt"
    data = process_input(file_path)
    r, c = 0, 0
    for d in data:
        r += find_ref_point(d[0])
        c += find_ref_point(d[1])
    print(100 * r + c)
