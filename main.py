import datetime
import sys

sum_seconds = 0


def read_data_from_input():
    lines = []  # ['10.09', '11:00-15:20 [4:20]', '15:40-20:10 [3:10]', '(8)']
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return lines


def split_line(line):
    """result ['11:00', '15:20', '[]']"""
    result = []
    temp = line.split('-')
    result.append(temp[0])
    temp = temp[1].split(' ')
    result.append(temp[0])
    result.append(temp[1])
    return result


def convert_seconds_to_hours(seconds):
    """01:12 without seconds"""
    td = datetime.timedelta(seconds=seconds)
    return ':'.join(str(td).split(':')[:2])


def get_diff(start_time, end_time):
    """ in seconds """
    time_start = datetime.datetime.strptime(start_time, "%H:%M")
    time_end = datetime.datetime.strptime(end_time, "%H:%M")
    diff = time_end - time_start
    return diff.total_seconds()


def solve_hours(line):
    global sum_seconds
    temp = split_line(line)
    diff_in_seconds = get_diff(start_time=temp[0], end_time=temp[1])
    sum_seconds += diff_in_seconds
    diff_in_hours = convert_seconds_to_hours(seconds=diff_in_seconds)
    temp[2] = (f'[{diff_in_hours}]')
    return temp


def merge_result(temp):
    """['11:00',"12:00", '[xx]'] -> 11:00-12:00 [xx]"""
    result = f'{temp[0]}-{temp[1]} {temp[2]}'
    return result


def handle_data(lines):
    for i in range(1, len(lines)-1):
        line = lines[i]
        lines[i] = merge_result(solve_hours(line))
    sum_hours = convert_seconds_to_hours(sum_seconds)
    lines[-1] = f'({sum_hours})'


if __name__ == "__main__":
    sum_seconds = 0
    lines = read_data_from_input()
    handle_data(lines)
    print('\n'.join(lines))
