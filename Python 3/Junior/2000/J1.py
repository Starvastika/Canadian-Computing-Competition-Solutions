start_day, total_days = map(int, input().split())
calendar = ['   '] * (start_day - 1)
calendar.extend(f'{day:>3}' for day in range(1, total_days + 1))
week_headers = ["Sun", "Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
weeks = [calendar[i:i + 7] for i in range(0, len(calendar), 7)]
print(' '.join(week_headers))
for week in weeks:
    print(' '.join(week))