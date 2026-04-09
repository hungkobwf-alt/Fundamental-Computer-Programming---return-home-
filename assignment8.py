
# Task 1: The Elevator Class
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moving UP. Now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moving DOWN. Now at floor {self.current_floor}")

    def go_to_floor(self, target_floor):

        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print("Invalid floor requested!")
            return

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()


# Task 2 & 3: The Building Class
class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        
        for i in range(num_elevators):
            new_elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(new_elevator)

    def run_elevator(self, elevator_number, destination_floor):
        index = elevator_number - 1 
        
        print(f"\n--- Running Elevator {elevator_number} to floor {destination_floor} ---")
        chosen_elevator = self.elevators[index]
        chosen_elevator.go_to_floor(destination_floor)

    # Task 3: Fire Alarm
    def fire_alarm(self):
        print("\n!!! FIRE ALARM TRIGGERED !!! Moving all elevators to the bottom floor.")
        
        for i in range(len(self.elevators)):
            elevator_number = i + 1
            print(f"\n--- Evacuating Elevator {elevator_number} ---")
            self.elevators[i].go_to_floor(self.bottom_floor)

# Main program 
if __name__ == "__main__":
    # Task 1 Test: Create one standalone elevator
    print("=== TESTING STANDALONE ELEVATOR ===")
    my_elevator = Elevator(1, 10)
    print("Going to floor 5...")
    my_elevator.go_to_floor(5)
    print("Going back to bottom...")
    my_elevator.go_to_floor(1)

    # Task 2 & 3 test: create a building
    print("\n=== TESTING BUILDING AND FIRE ALARM ===")
    my_building = Building(1, 7, 3) 

    my_building.run_elevator(1, 5)

    my_building.run_elevator(2, 7)

    my_building.fire_alarm()


    import random

# Car Class
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0       
        self.travelled_distance = 0  

    def accelerate(self, change_in_speed):
        self.current_speed += change_in_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


# # Task 4: The cả race Class

class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n--- {self.name} Status ---")
        print("---------------------------------------------------------")
        print(f"{'Reg Number':<12} | {'Max Speed':<10} | {'Current Speed':<15} | {'Distance'}")
        print("---------------------------------------------------------")
        for car in self.car_list:
            print(f"{car.registration_number:<12} | {car.max_speed:<6} km/h | {car.current_speed:<9} km/h | {car.travelled_distance} km")
        print("---------------------------------------------------------\n")

    def race_finished(self):
        # Check if ANY car has travelled the race distance or more
        for car in self.car_list:
            if car.travelled_distance >= self.distance:
                return True # Race is over!
        
        return False # No one has crossed the finish line yet


# Main Program
if __name__ == "__main__":

    participating_cars = []
    for number in range(1, 11): 
        reg_number = "ABC-" + str(number)
        random_max_speed = random.randint(150, 200)
        new_car = Car(reg_number, random_max_speed)
        participating_cars.append(new_car)

    derby_race = Race("Grand Demolition Derby", 8000, participating_cars)

    hours_passed = 0
    
    while derby_race.race_finished() == False:
        derby_race.hour_passes()
        hours_passed += 1
        
        if hours_passed % 10 == 0:
            print(f"Update: Hour {hours_passed}")
            derby_race.print_status()

    print("\n!!! THE RACE IS FINISHED !!!")
    print(f"Total time: {hours_passed} hours")
    derby_race.print_status()