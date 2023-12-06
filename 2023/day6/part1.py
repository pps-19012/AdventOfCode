import math


def process_input(filename):
    time, distance = [], []
    with open(filename, "r") as file:
        for line in file:
            line = line.split("\n")[0]
            if line[0] == "T":
                curr = time
            else:
                curr = distance
            title, val = line.split(":")
            val = val.split(" ")
            for v in val:
                if v != "":
                    curr.append(int(v))
    return (time, distance)


def calc_ways(time, distance):
    n = len(time)
    pos = []
    for i in range(n):
        t, d = time[i], distance[i]
        root_1 = (t - math.sqrt(t * t - 4 * d)) / 2
        root_2 = (t + math.sqrt(t * t - 4 * d)) / 2
        pos_r = [math.ceil(root_1), math.floor(root_2)]
        if pos_r[0] == root_1:
            pos_r[0] += 1
        if pos_r[1] == root_2:
            pos_r[1] -= 1
        pos.append(pos_r)
    ways = 1
    for u, v in pos:
        temp_ways = v - u + 1
        if temp_ways >= 1:
            ways = ways * temp_ways
    return ways


if __name__ == "__main__":
    file_path = "input.txt"
    t, d = process_input(file_path)
    ans = calc_ways(t, d)
    print(ans)
