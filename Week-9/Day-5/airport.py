# Instructions : Air Management System
# Your goal is to build an airplanes traffic management system.



# Details
# Your program should rely on four classes: Airline, Airplane, Flight and Airport.

# Consider every plane can fly only once per day.



# The Airline Class
# Attributes:

# id (str) A two letters code
# name (str)
# planes : A list of Airplanes belonging to this airline (see below the Airplane class)
# This class has no methods



# The Airplane Class
# Attributes:

# id (int)
# current_location : The Airport where the airplane is currently located (see below the Airport class)
# company : The airline this airplane belongs to (see above the Airline class)
# next_flights : The list of Flights. Every future flights of the airplane, this list should always be sorted by datetime. (see below the Flight class)


# Methods:

# fly(self, destination)
# location_on_date(self, date): Returns where the plane will be on this date
# available_on_date(self, date, location) : Returns True if the plane can fly from this location on this date (it can fly if it is in this location on this date and if it doesn’t already have a flight planned).


# The Flight Class
# Attributes:

# date (datetime.Date)
# destination : The destination airport. (see below the Airport class)
# origin : The departure airport. (see below the Airport class)
# plane : The plane used during this flight. (see above the Airplane class)
# id (str) : The ID is an encoded string composed of the destination, the airlines code and the date.
# Methods:

# Those methods are here only to update the rest of the system, for example, to change the location of the plane when it reaches its destination:

# take_off(self)
# land(self)


# The Airport Class
# Attributes:

# city (str) The code of the city where the airport is located
# planes : The list of every plane that is currently in this airport. (see above the Airplane class)
# scheduled_departures : The list of flight - Every future flight from this airport, sorted by date. (see above the Flight class)
# scheduled_arrivals : The list of flight - Every future flight that will arrive to this airport, sorted by date. (see above the Flight class)


# Methods:

# schedule_flight(self, destination, datetime) :
# finds an available airplane from an airline, that serves the departure and the destination
# schedule the airplane for the flight
# info(self, start_date, end_date) : Displays every scheduled flight from start_date to end_date.


# You are free to add any class/method/attribute to your code, be sure to document everything you write.

# Write a small code to test your program.

class Airline():
    def __init__(self, id, name:str, planes:list =[]):
        while True:
            if id.isalpha() and len(id) == 2:
                self.id = id
                break
            else:
                id = input('Please enter a valid 2 letter id code')
        self.name = name
        self.planes = planes

class Airport():
    def __init__(self) -> None:
        pass


class Airplane():
    id = 0
    def __init__(self, current_location:Airport, company:Airline, next_flight:list=[]):
        Airplane.id += 1
        self.id = Airplane.id
        self.current_location = current_location
        self.company = company
        self.next_flight = next_flight

    def fly(self, destination):
        pass

    def location_on_date(self, date):
        #Returns where the plane will be on this date
        pass

    def available_on_date(self, date, location):
        #Returns True if the plane can fly from this location on this date (it can fly if it is in this location on this date and if it doesn’t already have a flight planned)
        pass

class Flight():
    def __init__(self, date, destination:Airport, origin:Airport, plane:Airplane):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = str(self.destination) + str(plane.company) + str(self.date)

    def take_off(self):
        pass

    def land(self):
        pass
# The Flight Class
# Attributes:

# date (datetime.Date)
# destination : The destination airport. (see below the Airport class)
# origin : The departure airport. (see below the Airport class)
# plane : The plane used during this flight. (see above the Airplane class)
# id (str) : The ID is an encoded string composed of the destination, the airlines code and the date.
# Methods:

# Those methods are here only to update the rest of the system, for example, to change the location of the plane when it reaches its destination:

# take_off(self)
# land(self)
