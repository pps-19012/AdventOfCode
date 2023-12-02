def possible_cubes(filename):
    counter = {}
    with open(filename, "r") as file:
        for line in file:
            if line[-1] == "\n":
                x = line[:-1].split(": ")
            else:
                x = line.split(": ")
            id = int(x[0][5:])
            counter[id] = {"blue": 0, "red": 0, "green": 0}
            data = x[1].split("; ")
            for i in range(len(data)):
                specific = data[i].split(", ")
                for i in range(len(specific)):
                    atomic_data = specific[i].split(" ")
                    val = int(atomic_data[0])
                    color = atomic_data[1]
                    counter[id][color] = max(counter[id][color], val)
    return find_power(counter)


def find_power(counter):
    tot = 0
    for k, v in counter.items():
        tot += v["red"] * v["green"] * v["blue"]
    return tot


if __name__ == "__main__":
    file_path = "input.txt"
    ans = possible_cubes(file_path)
    print(ans)
