import part1 as p1

if __name__ == "__main__":
    file_path = "input.txt"
    data = p1.process_input(file_path)
    times = 1000000
    locations = p1.process_data(data, times)
    ans = p1.find_dist(locations)
    print(ans)
