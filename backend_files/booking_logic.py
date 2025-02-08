from data import rooms
import json
from datetime import datetime
date_format = '%Y-%m-%d'


print(rooms[101]['room_type'])
for i in rooms:
    print(rooms[i]['room_type'])



# Here is a method signature to get you started.

def book_room(room_number, name, check_in, check_out, email, phone, special_requests):
    roomExists = False

    for i in rooms:
        if i == room_number:
            roomExists = True
            break

    if not roomExists:
        return {"error": "Room not found."}

    room = rooms[room_number]
    checkInDate = datetime.strptime(check_in, date_format)
    checkOutDate = datetime.strptime(check_out, date_format)
    validDate = True

    #Checks if room is empty on requested check-in and check-out dates
    for occupant in room['occupants']:
        occCheckIn = datetime.strptime(occupant['check-in'], date_format)
        occCheckOut = datetime.strptime(occupant['check-in'], date_format)

        #Checks if the requested date is valid
        if checkInDate >= occCheckIn:
            if checkInDate < occCheckOut:
                validDate = False
        elif checkInDate  <= occCheckIn:
            if checkOutDate > occCheckIn:
                validDate = False

    if validDate == 0:
        return {"error" : "Room is occupied on requested date"}

    reservation = '{"name" : "' + name + '", "check_in": "' + check_in + '", "check_out": ' + check_out + '", "email": ' + email + '", "phone": ' + phone + '", "special_requests": "' + special_requests +'"'
    reservation_json = json.load(reservation)
    room['occupants'].append(reservation_json)