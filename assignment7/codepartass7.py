import random
# Tasks 1, 2, and 3: Building the Car class
class Car:
    # task 1: The initialize
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0      
        self.travelled_distance = 0  

    # Task 2:The accelerate Mthod
    def accelerate(self, change_in_speed):

        self.current_speed = self.current_speed + change_in_speed

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

    # Task 3: The drive Method
    def drive(self, hours):
        distance_driven = self.current_speed * hours

        self.travelled_distance = self.travelled_distance + distance_driven


# Task 4: The Main Program (The Race)
if __name__ == "__main__":

    cars_list = []
    
    for number in range(1, 11):
        reg_number = "ABC-" + str(number)
        random_max_speed = random.randint(150, 200)

        new_car = Car(reg_number, random_max_speed)
        cars_list.append(new_car)

    race_is_finished = False
    
    while race_is_finished == False:
        
        for car in cars_list:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)

            car.drive(1)
            
       
            if car.travelled_distance >= 10000:
                race_is_finished = True

    print("No sung bat dau cuoc dua")
    print(f"{'Reg Number':<12} | {'Max Speed':<10} | {'Current Speed':<15} | {'Distance'}")
    print("Bang thong so")
    
    for car in cars_list:
        print(f"{car.registration_number:<12} | {car.max_speed:<6} km/h | {car.current_speed:<9} km/h | {car.travelled_distance} km")
    print("Het cuoc dua")