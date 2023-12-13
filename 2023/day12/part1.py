def process_input(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            x, y = line.split(" ")
            num = [int(i) for i in y.split(",")]
            data.append((x, num))
    return data


def calc_arrangements(config, nums):
    if config == "":
        if nums == ():
            return 1
        else:
            return 0
    if nums == ():
        if "#" in config:
            return 0
        else:
            return 1

    res = 0
    if config[0] in ".?":
        res += calc_arrangements(config[1:], nums)

    if config[0] in "#?":
        if (
            nums[0] <= len(config)
            and "." not in config[: nums[0]]
            and (nums[0] == len(config) or config[nums[0]] != "#")
        ):
            res += calc_arrangements(config[nums[0] + 1 :], nums[1:])
    return res


if __name__ == "__main__":
    file_path = "input.txt"
    data = process_input(file_path)
    tot = 0
    for config, nums in data:
        tot += calc_arrangements(config, tuple(nums))
    print(tot)
