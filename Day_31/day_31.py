class SolarPowerSystem:
    def __init__(self, location, energy_demand):
        self.location = location
        self.energy_demand = energy_demand

    def calculate_solar_capacity(self):
        solar_capacity = self.energy_demand / 5  # Assuming 5 hours of sunlight per day
        return solar_capacity

    def optimize_system(self):
        # optimization and considerations 
        #Coming soon

        # Example optimization calculation
        solar_capacity = self.calculate_solar_capacity()
        optimized_capacity = solar_capacity * 1.2  # Add a safety margin of 20%

        return optimized_capacity

# Create a solar power system object
system1 = SolarPowerSystem("City A", 1000)  # Example energy demand of 1000 kWh

# Calculate the solar capacity
solar_capacity = system1.calculate_solar_capacity()
print("Required Solar Capacity:", solar_capacity, "kW")

# Optimize the system
optimized_capacity = system1.optimize_system()
print("Optimized Solar Capacity:", optimized_capacity, "kW")