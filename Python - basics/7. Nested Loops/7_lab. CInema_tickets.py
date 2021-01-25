# JUDGE Runtime error, but with correct answers.
movie = input()
free_seats = int(input())
type_ticket = input()
total_tickets = 0
standard_tickets = 0
student_tickets = 0
kid_tickets = 0

while type_ticket != 'Finish':
    busy_seats = 0

    while type_ticket != 'End' and busy_seats < free_seats:

        busy_seats += 1

        if type_ticket == 'standard':
            standard_tickets += 1
        elif type_ticket == 'student':
            student_tickets += 1
        elif type_ticket == 'kid':
            kid_tickets += 1

        type_ticket = input()

    total_tickets = standard_tickets + student_tickets + kid_tickets
    print(f'{movie} - {(busy_seats / free_seats) * 100:.2f}% full.')

    if type_ticket != 'Finish':
        movie = input()
        free_seats = int(input())
        type_ticket = input()
# if type_ticket == 'Finish':
print(f'Total tickets: {total_tickets}')
print(f'{(student_tickets / total_tickets) * 100:.2f}% student tickets.')
print(f'{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.')
print(f'{(kid_tickets / total_tickets) * 100:.2f}% kids tickets.')

# For JUDGE - 100 Points
counter_standard = 0
counter_kid = 0
counter_student = 0

while True:
    film = input()
    if film == "Finish":
        break

    capacity = int(input())
    tickets_sold = 0

    while capacity > tickets_sold:
        ticket_type = input()
        if ticket_type == "End":
            break

        tickets_sold += 1

        if ticket_type == "standard":
            counter_standard += 1
        elif ticket_type == "kid":
            counter_kid += 1
        elif ticket_type == "student":
            counter_student += 1

    print(f"{film} - {tickets_sold / capacity * 100:.2f}% full.")

ticket_counter = counter_standard + counter_kid + counter_student
print(f"Total tickets: {ticket_counter}")
print(f"{counter_student / ticket_counter * 100:.2f}% student tickets.")
print(f"{counter_standard / ticket_counter * 100:.2f}% standard tickets.")
print(f"{counter_kid / ticket_counter * 100:.2f}% kids tickets.")

# Variant 3

movie = input()
total_tickets = 0
standard_tickets = 0
student_tickets = 0
kid_tickets = 0

while movie != 'Finish':
    free_seats = int(input())
    busy_seats = 0

    for i in range(free_seats):
        ticket = input()

        if ticket == 'kid':
            kid_tickets += 1
        elif ticket == 'student':
            student_tickets += 1
        elif ticket == 'standard':
            standard_tickets += 1
        elif ticket == 'End':
            break
        total_tickets += 1
        busy_seats += 1

    percent_room = (busy_seats / free_seats) * 100
    total_tickets = standard_tickets + student_tickets + kid_tickets
    print(f'{movie} - {percent_room:.2f}% full.')

    movie = input()

print(f'Total tickets: {total_tickets}')
print(f'{(student_tickets / total_tickets) * 100:.2f}% student tickets.')
print(f'{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.')
print(f'{(kid_tickets / total_tickets) * 100:.2f}% kids tickets.')