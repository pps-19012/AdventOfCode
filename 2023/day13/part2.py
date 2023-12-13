import part1 as p1


def prev_ans(data):
    prev = {}
    for d in data:
        prev[tuple(d[0])] = p1.find_ref_point(d[0])
        prev[tuple(d[1])] = p1.find_ref_point(d[1])
    return prev


def valid_diff(arr1, arr2):
    n = len(arr1)
    diff = 0
    for i in range(n):
        if arr1[i] != arr2[i]:
            diff += 1
    if diff > 1:
        return False
    return True


def new_ref_point(arr, prev):
    # print(arr, prev)
    n = len(arr)
    for i in range(1, n):
        isMirror = True
        first = True
        for j in range(i):
            l = i - j - 1
            r = i + j
            # print("l:", l, "r:", r)
            if l >= 0 and r < n and arr[l] != arr[r]:
                # print(valid_diff(arr[l], arr[r]))
                if valid_diff(arr[l], arr[r]):
                    if first:
                        first = False
                else:
                    isMirror = False
            if not isMirror or l < 0 or r >= n:
                break
        if isMirror:
            if i != prev:
                # print("mirror:", i)
                return i
    # print("no mirror")
    return 0


if __name__ == "__main__":
    file_path = "input.txt"
    data = p1.process_input(file_path)
    prev = prev_ans(data)
    # print(prev)
    r, c = 0, 0
    for d in data:
        r += new_ref_point(d[0], prev[tuple(d[0])])
        c += new_ref_point(d[1], prev[tuple(d[1])])
    print(100 * r + c)
