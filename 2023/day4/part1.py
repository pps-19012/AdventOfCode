def process_input(filename):
    data = {}
    with open(filename, "r") as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            id_str, rem = line.split(": ")
            id = int(id_str[5:])
            win_str, have_str = rem.split(" | ")
            win_str, have_str = win_str.strip(), have_str.strip()
            win = win_str.replace("  ", " ").split(" ")
            have = have_str.replace("  ", " ").split(" ")
            for i in range(len(win)):
                win[i] = int(win[i])
            for i in range(len(have)):
                have[i] = int(have[i])
            win.sort()
            have.sort()
            data[id] = {"win": win, "have": have}
    return process_points(data)


def process_points(data):
    total_points = 0
    for k, v in data.items():
        curr_points = 0
        win = data[k]["win"]
        have = data[k]["have"]
        for elem in win:
            if bin_search(have, elem):
                curr_points += 1
        if curr_points > 0:
            total_points += 2 ** (curr_points - 1)
    return total_points


def bin_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            return True
    return False


if __name__ == "__main__":
    file_path = "input.txt"
    ans = process_input(file_path)
    print(ans)
