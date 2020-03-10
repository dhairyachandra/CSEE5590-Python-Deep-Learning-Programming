import random

class Flight:
    # Flight class - Default constructor
    def __init__(self, airline_name, flight_number):
        self.airline_name = airline_name
        self.flight_number = flight_number

    # Displaying flight details
    def flight_details(self):
        print('Airlines : ', self.airline_name)
        print('Flight number : Boeing', self.flight_number)


class employee:
    # Employee class - Default constructor
    def __init__(self, e_id, e_name, e_age, e_gender):
        self.e_name = e_name
        self.e_age = e_age
        self.__e_id = e_id
        self.e_gender = e_gender

    # Displaying employee details
    def e_display(self):
        print("Name of employee: ", self.e_name)
        print('Employee ID: ', self.__e_id)
        print('Employee Age: ', self.e_age)
        print('Employee Gender: ', self.e_gender)


class Passenger:
    # Passenger class - for fetching details of the passenger
    def __init__(self):
        Passenger.__passport_number = input("Enter the passport number of the passenger: ")
        Passenger.name = input('Enter name of the passenger: ')
        Passenger.age = input('Enter age of passenger : ')
        Passenger.gender = input('Enter the gender: ')
        Passenger.class_type = input('Select business or economy class: ')


class Baggage:
    cabin_bag = 1
    bag_fare = 0

    # calculating cost for checked in bags more than 2
    def __init__(self, checked_bags):
        self.checked_bags = checked_bags
        if checked_bags > 2:
            for i in checked_bags:
                self.bag_fare += 100
        print("Number of checked bags allowed: ", checked_bags, "bag fare: $", self.bag_fare)


class Fare(Baggage):
    # Cost is fixed for purchasing at counter
    counter = 1150
    # Cost varies with ticket is purchased through online and fair is generated through random function
    online = random.randint(1110, 2200)
    total_fare = online

    def __init__(self):
        super().__init__(2)  # Super call
        x = input('Buy ticket through online or counter: ')
        if x == 'online':
            Fare.total_fare = self.online + self.bag_fare
        elif x == 'counter':
            Fare.total_fare = self.counter + self.bag_fare
        else:
            x = input('Enter correct transaction type:')
        print("Total Fare before class type: $", Fare.total_fare)


class Ticket(Passenger, Fare):  # Multiple inheritence
    def __init__(self):
        print("Passenger name:", Passenger.name)  # Accessing parent class variable
        if Passenger.class_type == "business":
            Fare.total_fare += 100
        else:
            pass
        print("Passenger class type:", Passenger.class_type)
        print("Total fare: $", Fare.total_fare)  # Displaying total fare


print("------------- Flight Details --------------")
f1 = Flight('Air India', 777)
f1.flight_details()
print("------------- Employee Details --------------")
e0 = employee('4588124', 'Dhairya Chandra', 22, 'Male')
e0.e_display()

print("------------- Book Ticket --------------")
p1 = Passenger()

fare1 = Fare()

print("------------- Passenger Details --------------")
t = Ticket()
