import part1


def process_raw_seeds(raw_seeds):
    seeds = []
    n = len(raw_seeds)
    for i in range(0, n, 2):
        start, range_len = raw_seeds[i], raw_seeds[i + 1]
        seeds.append([start, range_len])
    return seeds


def lowest_location(seeds, maps):
    min_location = float("inf")
    for start, range_len in seeds:
        curr_range = [(start, start + range_len)]
        for k, v in maps.items():
            intersect = []
            for x in v:
                new_range = []
                source_start, dest_start, range_len = x
                source_end = source_start + range_len
                while curr_range:
                    start, end = curr_range.pop()
                    before = (start, min(end, source_start))
                    inter = (
                        max(start, source_start),
                        min(source_end, end),
                    )
                    after = (max(source_end, start), end)
                    if before[1] > before[0]:
                        new_range.append(before)
                    if after[1] > after[0]:
                        new_range.append(after)
                    if inter[1] > inter[0]:
                        intersect.append(
                            (
                                inter[0] - source_start + dest_start,
                                inter[1] - source_start + dest_start,
                            )
                        )
                curr_range = new_range
            curr_range = curr_range + intersect
        min_location = min(min_location, min(curr_range)[0])
    return min_location


if __name__ == "__main__":
    file_path = "input.txt"
    raw_seeds, maps = part1.process_input(file_path)
    seeds = process_raw_seeds(raw_seeds)
    ans = lowest_location(seeds, maps)
    print(ans)
