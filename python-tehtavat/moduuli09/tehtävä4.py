# Now a car race is being programmed. The distance traveled by the new car is automatically initialized to zero.
# At the beginning of the main program, make a list consisting of ten car objects created with the repetition structure.
# The top speed of each car is drawn between 100 km/h and 200 km/h.
# The registration code is generated as follows "ABC-1", "ABC-2", etc.
# Then the competition begins. During the competition, the following measures are taken every hour:
# The speed of each car is changed so that the speed change is drawn between -10 and +15 km/h.
# This is done by calling the accelerate method.
# All cars are told to move for one hour. This is done by calling the go method.
# The competition continues until one of the cars has traveled at least 10,000 kilometers.
# Finally, all the characteristics of each car are printed in a clear table.
import random

class Car:
    def __init__(self, license_plate, top_speed):
        self.license_plate = license_plate
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, change_of_speed):
        new_speed = self.current_speed + change_of_speed
        if self.current_speed > self.top_speed:
            self.current_speed = self.top_speed
        if change_of_speed < 0:
            self.current_speed += change_of_speed
        if self.current_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed
        # if self.current_speed > 0:
        #     print(f'The car accelerates to {self.current_speed} km/h')
        # else:
        #     print(f'The car decelerates to {self.current_speed} km/h')

    def move(self, hour):
        new_distance = (self.current_speed * hour)
        self.distance_traveled += new_distance
        # if hour > 1:
        #     print(f'Current traveled distance is {self.distance_traveled}km. Current speed is {self.current_speed}km/h. Hour elapsed is {hour} hours. The car traveled to {new_distance}km')
        # else:
        #     print(f'Current traveled distance is {self.distance_traveled}km. Current speed is {self.current_speed}km/h. Hour elapsed is {hour} hour. The car traveled to {new_distance}km')

cars = []
i = 1
for i in range(1, 11):
    car = Car(f'ABC-{i}', random.randint(100, 200))
    cars.append(car)
    i += 1



race = True
duration = 1

while race:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.move(1)
        if car.distance_traveled >= 10000:
            race = False

print('The result of the competition')
print('{:<15} {:<15} {:<15} {:<15}'.format('License plate', 'Top speed', 'Speed', 'Distance traveled'))
for car in cars:
    print("{:<15} {:<15} {:<15} {:<15}"
          .format(car.license_plate, car.top_speed, car.current_speed, car.distance_traveled))