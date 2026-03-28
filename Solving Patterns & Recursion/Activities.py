def maxMeetings(start, end):
    meetings = sorted(zip(start, end), key=lambda x: x[1])
    count = 0
    last_end_time = 0

    for start_time, end_time in meetings:
        if start_time >= last_end_time:
            count += 1
            last_end_time = end_time

    return count

start = [1, 3, 0, 5, 8, 5]
end   = [2, 4, 6, 7, 9, 9]

print(maxMeetings(start, end)) 