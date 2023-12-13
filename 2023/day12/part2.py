import part1 as p1

memo = {}


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

    if (config, nums) not in memo:
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
        memo[(config, nums)] = res
    return memo[(config, nums)]


if __name__ == "__main__":
    file_path = "input.txt"
    data = p1.process_input(file_path)
    tot = 0
    for config, nums in data:
        config = "?".join([config] * 5)
        nums *= 5
        tot += calc_arrangements(config, tuple(nums))
    print(tot)
