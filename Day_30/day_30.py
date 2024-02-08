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


# Create a student object
student1 = Student("Johnson", "Environmental Science", 150)

# Display student information
student1.display_student_info()

# Calculate and display the carbon footprint
carbon_footprint = student1.calculate_carbon_footprint()
print("Carbon Footprint:", carbon_footprint, "kgCO2e")
