record_seconds = float(input())
distance_m = float(input())
time_seconds_m = float(input())

time = distance_m * time_seconds_m

if distance_m >= 15:
    delay = (distance_m // 15) * 12.5
else:
    delay = 0
total_time = time + delay

if total_time < record_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {total_time - record_seconds:.2f} seconds slower.')