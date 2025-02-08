from data import rooms
import json
from datetime import datetime
date_format = '%Y-%m-%d'


print(rooms[101]['room_type'])
for i in rooms:
    print(rooms[i]['room_type'])



# Here is a method signature to get you started.

def book_room(room_number, name, check_in, check_out, email, phone, special_requests):
    room = rooms[room_number]
    checkInDate = datetime.strptime(check_in, date_format)
    checkOutDate = datetime.strptime(check_out, date_format)
    validDate = 1 #will be 0 and 1 instead of false and true

    for occupant in room['occupants']:
        occCheckIn = datetime.strptime(occupant['check-in'], date_format)
        occCheckOut = datetime.strptime(occupant['check-in'], date_format)

        #Checks if the requested date is valid
        if checkInDate >= occCheckIn:
            if checkInDate < occCheckOut:
                validDate = 0
        elif checkInDate  <= occCheckIn:
            if checkOutDate > occCheckIn:
                validDate = 0

    if validDate == 0:
        return {"error": "Room not found."}