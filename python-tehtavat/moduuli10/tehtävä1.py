# Write an Elevator class that receives the lowest and highest floor number as its initializer parameters.
# The elevator has the methods move_to_floor, floor_up and floor_down. The new elevator is always on the lowest floor.
# For example, if you make a method call to the created elevator h to h.move_floor(5),
# the method calls either the floor_up or floor_down method as many times as the elevator ends up on the fifth floor.
# The last-mentioned methods drive the elevator up or down one floor
# and indicate which floor the elevator is on afterward.
# Test the class by creating an elevator in the main program
# and telling it to go to the floor you want and then back to the lowest floor.
class Elevator:
    def __init__(self, lowest_floor, highest_floor):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = lowest_floor

    def move_to_floor(self, floor):
        while floor > self.current_floor:
            self.move_up()
        while floor < self.current_floor:
            self.move_down()

    def move_up(self):
        if self.current_floor < self.highest_floor:
            self.current_floor += 1
            print(f'The elevator is now in floor {self.current_floor}')

    def move_down(self):
        if self.current_floor > self.lowest_floor:
            self.current_floor -= 1
            print(f'The elevator is now in floor {self.current_floor}')


elevator1 = Elevator(0, 20)
elevator1.move_to_floor(5)
elevator1.move_to_floor(elevator1.lowest_floor)
