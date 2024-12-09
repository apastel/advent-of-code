from typing import List
from advent.load import read_input

reports = [[int(level) for level in line.split(" ")] for line in read_input()]


def is_report_safe(report: List[int]):
    for idx, level in enumerate(report):
        if idx == len(report) - 1:
            return True
        else:
            next_level = report[idx + 1]
            difference = level - next_level
            if abs(difference) < 1 or abs(difference) > 3:
                return False
            if idx > 0:
                prev_level = report[idx - 1]
                prev_difference = prev_level - level
                if difference * prev_difference < 0:
                    return False


safe_reports = 0
for report in reports:
    if is_report_safe(report):
        safe_reports += 1
    else:
        for idx, _ in enumerate(report):
            modified_report = report[:idx] + report[idx+1:]
            if is_report_safe(modified_report):
                safe_reports += 1
                break

print(safe_reports)
