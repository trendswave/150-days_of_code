class Student:
    def __init__(self, name, major, energy_usage):
        self.name = name
        self.major = major
        self.energy_usage = energy_usage

    def calculate_carbon_footprint(self):
        carbon_footprint = self.energy_usage * 0.7
        return carbon_footprint

    def display_student_info(self):
        print("Name:", self.name)
        print("Major:", self.major)
        print("Energy Usage:", self.energy_usage, "kWh")


