import part1 as p1
import math


def find_start(network):
    starts = []
    for k in network.keys():
        if k[-1] == "A":
            starts.append(k)
    return starts


def calc_steps(starts, inst, network):
    all_steps = []
    for curr in starts:
        i, n = 0, len(inst)
        steps = 0
        while True:
            if curr[-1] == "Z":
                break
            curr_inst = inst[i]
            if curr_inst == "L":
                curr = network[curr][0]
            else:
                curr = network[curr][1]
            steps += 1
            i = (i + 1) % n
        all_steps.append(steps)
    ans = 1
    for steps in all_steps:
        ans = math.lcm(ans, steps)
    return ans


if __name__ == "__main__":
    file_path = "input.txt"
    inst, network = p1.process_input(file_path)
    start_pos = find_start(network)
    ans = calc_steps(start_pos, inst, network)
    print(ans)
