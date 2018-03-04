class vehicle:
    def __init__(self, brand, model, kilometers, general_service_date):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.general_service_date = general_service_date

    def get_full_type(self):
        return self.brand + " " + self.model

def list_all_vehicle(vehicles):
    for index, car in enumerate(vehicles):
        print "ID: " + str(index)
        print car.brand
        print car.model
        print car.kilometers
        print car.general_service_date

def edit_kilometers(vehicles):
    print "Select the number of the car you'd like to edit: "

    for index, car in enumerate(vehicles):
        print str(index) + ") " + car.get_full_type()
        print""

    selected_id = raw_input("What vehicle would you like to edit? (enter ID number): ")
    selected_vehicle = vehicles[int(selected_id)]

    new_kilometers = raw_input("Please enter new kilometers for %s: " % selected_vehicle.get_full_type())
    selected_vehicle.kilometers = new_kilometers

    print""
    print "Kilometers are updated."


def edit_general_service_date(vehicles):
    print "Select the number of the car you'd like to edit: "

    for index, car in enumerate(vehicles):
        print str(index) + ") " + car.get_full_type()
        print""

    selected_id = raw_input("What vehicle would you like to edit? (enter ID number): ")
    selected_vehicle = vehicles[int(selected_id)]

    new_general_service_date = raw_input("Please enter new general service date for %s: " % selected_vehicle.get_full_type())
    selected_vehicle.general_service_date = new_general_service_date

    print""
    print "General service date is updated."


def add_new_vehicle(vehicles):
    brand = raw_input("Please enter the brand of the new vehicle: ")
    model = raw_input("Please enter the model of the new vehicle: ")
    kilometers = raw_input("Please enter kilometers of the new vehicle: ")
    general_service_date = raw_input("Please enter the general service date of the new vehicle: ")

    new = vehicle(brand = brand, model = model, kilometers = kilometers, general_service_date = general_service_date)
    vehicles.append(new)

    print ""
    print new.get_full_type() + " was successfully added to your contact list."

def main():
    print "Welcome to your vehicle manager!"

    toyota = vehicle(brand = "Toyota", model = "Yaris", kilometers ="2352", general_service_date = "22.03.2015.")
    ford = vehicle(brand="Ford", model="Focus", kilometers="1325", general_service_date="15.08.2017.")
    honda = vehicle(brand="Honda", model="Civic", kilometers="653", general_service_date="02.12.2020.")
    mazda = vehicle(brand="Mazda", model="CX-5", kilometers="3654", general_service_date="06.05.2019.")
    vehicles = [toyota,ford,honda,mazda]

    while True:
        print ""  # empty line
        print "Please choose one of these options:"
        print "a) See all your vehicles"
        print "b) Add a new vehicle"
        print "c) Edit the kilometers"
        print "d) Edit the general service date"
        print "e) Quit the program."
        print ""  # empty line

        selection = raw_input("Enter your selection (a, b, c, d, or e,): ")
        print ""  # empty line

        if selection.lower() == "a":
            list_all_vehicle(vehicles)
        elif selection.lower() == "b":
            add_new_vehicle(vehicles)
        elif selection.lower() == "c":
            edit_kilometers(vehicles)
        elif selection.lower() == "d":
            edit_general_service_date(vehicles)
        elif selection.lower() == "e":
            print "Thank you for using Vehicle Manager. Goodbye!"
            break
        else:
            print "Sorry, I didn't understand your selection. Please try again."
            continue

if __name__ == "__main__":
    main()