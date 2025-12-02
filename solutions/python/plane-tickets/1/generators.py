"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seats = ['A','B','C','D']

    for i in range(number):
        yield seats[i%4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    seats = generate_seat_letters(number)
    seat_number = 0
    for i in range(number):
        seat_alphabet = next(seats)
        if seat_alphabet == 'A' :
            seat_number += 1
        if seat_number == 13 :
            seat_number += 1

        yield f"{seat_number}{seat_alphabet}"
        

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seats = generate_seats(len(passengers))
    values = []
    for i in range(len(passengers)):
        values.append(next(seats))

    seat_assign_dict = dict(zip(passengers,values))

    return seat_assign_dict

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seats in seat_numbers:
        seat_code = f"{seats}{flight_id}"
        ticket_id = seat_code.ljust(12,'0')
        yield ticket_id