# Create a list of all the seats in the coach
seats = []
for i in range(1, 81):
    if i % 7 == 0 or i % 7 == 4:
        seats.append(('B', i))
    elif i % 7 == 1 or i % 7 == 5:
        seats.append(('M', i))
    else:
        seats.append(('W', i))

# Create a list of already booked seats
booked_seats = [(3, 5), (3, 6), (3, 7), (4, 1), (4, 2)]

# Function to check if seats are available in a row
def check_row(row, num_seats):
    for i in range(1, 8 - num_seats):
        if all([(row, j) not in booked_seats for j in range(i, i + num_seats)]):
            return [(row, j) for j in range(i, i + num_seats)]
    return None

# Function to check if nearby seats are available
def check_nearby(num_seats):
    for i in range(len(seats) - num_seats + 1):
        if all([seats[i+j] not in booked_seats for j in range(num_seats)]):
            return seats[i:i+num_seats]
    return None

# Function to reserve seats
def reserve_seats(num_seats):
    row_seats = None
    for row in range(1, 11):
        row_seats = check_row(row, num_seats)
        if row_seats is not None:
            break
    if row_seats is None:
        row_seats = check_nearby(num_seats)
    if row_seats is None:
        return None
    else:
        for seat in row_seats:
            booked_seats.append(seat)
        return row_seats

# Example usage of the functions
num_seats = 4
reserved_seats = reserve_seats(num_seats)
if reserved_seats is not None:
    print(f"Reserved seats: {reserved_seats}")
else:
    print("No seats available.")
