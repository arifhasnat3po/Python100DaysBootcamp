import time
import random
import matplotlib.pyplot as plt

class SmartOfficeSystem:
    def __init__(self):
        # Initialize the system's attributes

        self.time_steps = []  # To store time steps
        self.rfid_status = []  # To store RFID status
        self.door_status = []  # To store door status
        self.window_status = []  # To store window status
        self.garage_status = []  # To store garage status
        self.coffee_fan_status = []  # To store coffee and fan status

    def update(self, time_step):
        # Update the system's attributes
        self.time_steps.append(time_step)
        
        # Simulate changes in system state
        # (You can add your own logic here for state changes)
        self.rfid_status.append(random.choice(["Valid", "Invalid", "Waiting"]))
        self.door_status.append(random.choice(["Locked", "Unlocked"]))
        self.window_status.append(random.choice(["Open", "Closed"]))
        self.garage_status.append(random.choice(["Open", "Closed"]))
        self.coffee_fan_status.append(random.choice(["On", "Off", "Low", "High"]))

    def plot_state(self):
        # Create a line plot to visualize the state changes
        plt.figure(figsize=(12, 6))
        plt.plot(self.time_steps, self.rfid_status, label="RFID Status")
        plt.plot(self.time_steps, self.door_status, label="Door Status")
        plt.plot(self.time_steps, self.window_status, label="Window Status")
        plt.plot(self.time_steps, self.garage_status, label="Garage Status")
        plt.plot(self.time_steps, self.coffee_fan_status, label="Coffee & Fan Status")

        plt.title("Smart Office System State Over Time")
        plt.xlabel("Time Step")
        plt.ylabel("Status")
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    smart_office_system = SmartOfficeSystem()
    
    # Simulate system updates over time
    for time_step in range(1, 21):
        smart_office_system.update(time_step)
    
    # Plot the system state changes
    smart_office_system.plot_state()
