# quantities = [seeds, soil, fertilizer, water, light, temperature, humidity, location]


def process_input(filename):
    f = []
    with open(filename, "r") as file:
        for line in file:
            if line[-1] == "\n":
                f.append(line[:-1])
            else:
                f.append(line)

    maps = {
        "seed-to-soil map:": [],
        "soil-to-fertilizer map:": [],
        "fertilizer-to-water map:": [],
        "water-to-light map:": [],
        "light-to-temperature map:": [],
        "temperature-to-humidity map:": [],
        "humidity-to-location map:": [],
    }

    i = 0
    while i < len(f):
        if i == 0:
            x = f[i].split(": ")
            seeds = x[1].split(" ")
            for j in range(len(seeds)):
                seeds[j] = int(seeds[j])
            i += 1

        if f[i] in maps:
            arr = maps[f[i]]
            i += 1
            while i < len(f) and f[i] != "":
                data = process_line(f[i])
                arr.append(data)
                i += 1

        if i < len(f) and f[i] == "":
            i += 1

    for k, v in maps.items():
        v.sort()

    return (seeds, maps)


def lowest_location(seeds, maps):
    min_location = float("inf")
    for seed in seeds:
        curr_val = seed
        for k, v in maps.items():
            for x in v:
                if curr_val >= x[0] and curr_val <= x[0] + x[2] - 1:
                    curr_val = x[1] + curr_val - x[0]
                    break
            if k == "humidity-to-location map:":
                min_location = min(min_location, curr_val)
    return min_location


def process_line(line):
    x = line.strip()
    x = x.split(" ")
    for i in range(len(x)):
        x[i] = int(x[i])
    dest_start, source_start, range_len = x
    data = [source_start, dest_start, range_len]
    return data


if __name__ == "__main__":
    file_path = "input.txt"
    seeds, maps = process_input(file_path)
    ans = lowest_location(seeds, maps)
    print(ans)
