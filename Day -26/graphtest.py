import time
import random
import matplotlib.pyplot as plt

class SmartOfficeSystem:
    def __init__(self):
        # Initialize the system's attributes

        self.time_steps = []  # To store time steps
        self.rfid_status = []  # To store RFID status
        self.door_status = []  # To store door status
        self.window_status = []  # To store general window status
        self.fire_window_status = []  # To store window status related to fire
        self.smoke_window_status = []  # To store window status related to smoke
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
        self.fire_window_status.append(random.choice(["Open", "Closed"]))
        self.smoke_window_status.append(random.choice(["Open", "Closed"]))
        self.garage_status.append(random.choice(["Open", "Closed"]))
        self.coffee_fan_status.append(random.choice(["On", "Off", "Low", "High"]))

    def plot_state(self):
        # Create a line plot to visualize the state changes
        plt.figure(figsize=(12, 6))
        plt.plot(self.time_steps, self.rfid_status, label="RFID Status")
        plt.plot(self.time_steps, self.door_status, label="Door Status")
        
        plt.title("RFID and Door Status Over Time")
        plt.xlabel("Time Step")
        plt.ylabel("Status")
        plt.legend()
        plt.grid()
        plt.show()
        
        # Create a separate plot for window status related to fire and smoke
        plt.figure(figsize=(12, 6))
        plt.plot(self.time_steps, self.fire_window_status, label="Fire Window Status")
        plt.plot(self.time_steps, self.smoke_window_status, label="Smoke Window Status")

        plt.title("Fire and Smoke Window Status Over Time")
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
