def process_input(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line)
    return data


def is_report_safe(arr):
    if arr[0] > arr[-1]:
        for i in range(1, len(arr)):
            diff = arr[i - 1] - arr[i]
            if diff >= 1 and diff <= 3:
                continue
            else:
                return False
        return True
    elif arr[0] < arr[-1]:
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff >= 1 and diff <= 3:
                continue
            else:
                return False
        return True
    else:
        return False


def safe_reports(data):
    safe_reports = 0
    for line in data:
        report = list(map(int, line.split()))
        if is_report_safe(report):
            safe_reports += 1
    return safe_reports


if __name__ == "__main__":
    filename = "input1.txt"
    data = process_input(filename)
    print(safe_reports(data))
