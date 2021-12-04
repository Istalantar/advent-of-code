from functions import my_input

content = my_input('input.txt')
test = 'FBFBBFFRLR'
tickets = []

for ticket in content:
    row = 64
    column = 4
    temp = 64
    seat_id = ''

    for i in range(7):
        temp /= 2
        if ticket[i] == 'B':
            row = int(row + temp)
        elif ticket[i] == 'F':
            row = int(row - temp)

    temp = 4
    for i in range(7, 10, 1):
        temp /= 2
        if ticket[i] == 'R':
            column = int(column + temp)
        elif ticket[i] == 'L':
            column = int(column - temp)

    seat_id = row * 8 + column
    tickets.append([row, column, seat_id])

seats = []
for y in range(128):
    for x in range(8):
        seats.append([y, x, y * 8 + x])

temp_seats = seats.copy()
for seat in tickets:
    if seat in temp_seats:
        seats.remove(seat)

for seat in temp_seats:
    if seat[0] == 0:
        seats.remove(seat)
    if seat[0] == 127:
        seats.remove(seat)

for seat in seats:
    print(seat)
