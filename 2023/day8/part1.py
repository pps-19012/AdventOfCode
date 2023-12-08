def process_input(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            if line == "\n":
                continue
            data.append(line)
    instructions = data[0][:-1]
    network = {}
    for i in range(1, len(data)):
        pos, l, r = data[i][:3], data[i][7:10], data[i][12:15]
        network[pos] = (l, r)
    return (instructions, network)


def calc_steps(inst, network):
    curr = "AAA"
    i, n = 0, len(inst)
    steps = 0
    while True:
        if curr == "ZZZ":
            break
        curr_inst = inst[i]
        if curr_inst == "L":
            curr = network[curr][0]
        else:
            curr = network[curr][1]
        steps += 1
        i = (i + 1) % n
    return steps


if __name__ == "__main__":
    file_path = "input.txt"
    inst, network = process_input(file_path)
    ans = calc_steps(inst, network)
    print(ans)
