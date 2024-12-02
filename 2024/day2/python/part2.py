def process_input(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line)
    return data


def is_report_safe(arr):
    # safe = (
    #     is_report_safe_increasing(arr)
    #     or is_report_safe_decreasing(arr)
    #     or is_report_safe_increasing(arr[1:])
    #     or is_report_safe_decreasing(arr[1:])
    # )
    # return safe

    # this is brute force -> not cool.
    for i in range(len(arr)):
        new_arr = arr.copy()
        del new_arr[i]
        if is_simple_report_safe(new_arr):
            return True
    return False


def is_report_safe_increasing(arr):
    prev = arr[0]
    problem_damper = True
    for i in range(1, len(arr)):
        curr = arr[i]
        if curr > prev and 0 < (curr - prev) < 4:
            prev = curr
            continue
        else:
            if problem_damper:
                problem_damper = False
            else:
                return False
    return True


def is_report_safe_decreasing(arr):
    prev = arr[0]
    problem_damper = True
    for i in range(1, len(arr)):
        curr = arr[i]
        if curr < prev and 0 < (prev - curr) < 4:
            prev = curr
            continue
        else:
            if problem_damper:
                problem_damper = False
            else:
                return False
    return True


def is_simple_report_safe(arr):
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
        is_safe = is_report_safe(report)
        if is_safe:
            safe_reports += 1
        # print(report, ": ", is_safe)
    return safe_reports


if __name__ == "__main__":
    filename = "input1.txt"
    data = process_input(filename)
    print(safe_reports(data))
