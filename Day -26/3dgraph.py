import time
import random
import matplotlib.pyplot as plt
import pandas as pd

class SmartOfficeSystem:
    def __init__(self):
        # Initialize the system's attributes
        self.time_steps = []  # To store time steps
        self.rfid_status = []  # To store RFID status
        self.door_status = []  # To store door status
        self.window_status = []  # To store window status
        self.garage_status = []  # To store garage status
        self.coffee_status = []  # To store coffee status
        self.fan_status = []  # To store fan status

    def update(self, time_step):
        # Update the system's attributes
        self.time_steps.append(time_step)
        
        # Simulate changes in system state
        self.rfid_status.append(random.choice(["Valid", "Invalid", "Waiting"]))
        self.door_status.append(random.choice(["Locked", "Unlocked"]))
        self.window_status.append(random.choice(["Closed", "Open"]))
        self.garage_status.append(random.choice(["Closed", "Open"]))
        self.coffee_status.append(random.choice(["Off", "On"]))
        self.fan_status.append(random.choice(["Low", "High"]))

    def plot_state(self):
        # Create a bar chart
        
        plt.style.use('seaborn-whitegrid')
        
        # Simulated time
        time_simulated = self.time_steps
        
        # Convert status to numerical values for plotting
        status_mapping = {"Valid": 1, "Invalid": 2, "Waiting": 3, "Locked": 4, "Unlocked": 5, "Closed": 6, "Open": 7, "Off": 8, "On": 9, "Low": 10, "High": 11}
        rfid_numeric = [status_mapping[status] for status in self.rfid_status]
        door_numeric = [status_mapping[status] for status in self.door_status]
        window_numeric = [status_mapping[status] for status in self.window_status]
        garage_numeric = [status_mapping[status] for status in self.garage_status]
        coffee_numeric = [status_mapping[status] for status in self.coffee_status]
        fan_numeric = [status_mapping[status] for status in self.fan_status]
        
        # Create a DataFrame for easy data manipulation
        data = pd.DataFrame({
            'Time Step': time_simulated,
            'RFID': rfid_numeric,
            'Door': door_numeric,
            'Window': window_numeric,
            'Garage': garage_numeric,
            'Coffee': coffee_numeric,
            'Fan': fan_numeric
        })

        # Create a bar chart
        fig, ax = plt.subplots(figsize=(12, 6))
        width = 0.15
        colors = ['b', 'g', 'r', 'c', 'm', 'y']
        
        for i, component in enumerate(data.columns[1:]):
            ax.bar(data['Time Step'] + (i - 2) * width, data[component], width=width, label=component, color=colors[i])

        ax.set_xlabel('Time Step')
        ax.set_ylabel('Component Status')
        ax.set_title("Smart Office System State Over Time (Bar Chart)")
        ax.legend()
        
        plt.grid(visible=False)
        plt.show()

if __name__ == "__main__":
    smart_office_system = SmartOfficeSystem()
    
    # Simulate system updates over time
    for time_step in range(1, 21):
        smart_office_system.update(time_step)
    
    # Plot the system state in a bar chart resembling an Excel graph
    smart_office_system.plot_state()
