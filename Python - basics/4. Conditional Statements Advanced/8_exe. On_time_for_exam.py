exam_hour = int(input())
exam_minutes = int(input())
student_hour = int(input())
student_minutes = int(input())
exam_all_minutes = exam_hour * 60 + exam_minutes
student_all_minutes = student_hour * 60 + student_minutes
early_minutes = exam_all_minutes - student_all_minutes
late_minutes = student_all_minutes - exam_all_minutes

if exam_hour == student_hour and exam_minutes == student_minutes:
    print(f'On time')
elif 0 < early_minutes <= 30:
    print(f'On time\n{early_minutes} minutes before the start')

elif 30 < early_minutes < 60:
    print(f'Early\n{early_minutes} minutes before the start')

elif early_minutes >= 60:
    arrive_hour = early_minutes // 60
    arrive_minutes = early_minutes % 60
    if arrive_minutes < 10:
        print(f'Early\n{arrive_hour}:0{arrive_minutes} hours before the start')
    else:
        print(f'Early\n{arrive_hour}:{arrive_minutes} hours before the start')

elif late_minutes < 60:
    print(f'Late\n{late_minutes} minutes after the start')

elif late_minutes >= 60:
    arrive_hour = late_minutes // 60
    arrive_minutes = late_minutes % 60
    if arrive_minutes < 10:
        print(f'Late\n{arrive_hour}:0{arrive_minutes} hours after the start')
    else:
        print(f'Late\n{arrive_hour}:{arrive_minutes} hours after the start')