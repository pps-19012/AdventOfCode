import part1


def combine_data(time, dist):
    t, d = "", ""
    for val in time:
        t += str(val)
    for val in dist:
        d += str(val)
    return ([int(t)], [int(d)])


if __name__ == "__main__":
    file_path = "input.txt"
    time, dist = part1.process_input(file_path)
    t, d = combine_data(time, dist)
    ans = part1.calc_ways(t, d)
    print(ans)
