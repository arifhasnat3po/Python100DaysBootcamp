import random
import pandas as pd
import plotly.express as px

class SmartOfficeSystem:
    def __init__(self):
        # Initialize the system's attributes
        self.time_steps = []  # To store time steps
        self.rfid_status = []  # To store RFID conditions
        self.door_status = []  # To store door conditions
        self.window_status = []  # To store window conditions
        self.garage_status = []  # To store garage conditions
        self.coffee_status = []  # To store coffee conditions
        self.fan_status = []  # To store fan conditions

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
        # Create an area chart
        
        # Simulated time
        time_simulated = self.time_steps
        
        # Convert conditions to numerical values for plotting
        condition_mapping = {"Valid": 1, "Invalid": 2, "Waiting": 3, "Locked": 4, "Unlocked": 5, "Closed": 6, "Open": 7, "Off": 8, "On": 9, "Low": 10, "High": 11}
        rfid_numeric = [condition_mapping[condition] for condition in self.rfid_status]
        door_numeric = [condition_mapping[condition] for condition in self.door_status]
        window_numeric = [condition_mapping[condition] for condition in self.window_status]
        garage_numeric = [condition_mapping[condition] for condition in self.garage_status]
        coffee_numeric = [condition_mapping[condition] for condition in self.coffee_status]
        fan_numeric = [condition_mapping[condition] for condition in self.fan_status]
        
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

        # Create an area chart using Plotly Express
        fig = px.area(data, x='Time Step', y=data.columns[1:], color_discrete_sequence=px.colors.qualitative.Set1)
        fig.update_layout(
            title='Smart Office System State Over Time',
            xaxis_title='Time Step',
            yaxis_title='Conditions',  # Change 'Status' to 'Conditions'
            legend_title='Components',
            showlegend=True
        )
        
        # Show the area chart
        fig.show()

if __name__ == "__main__":
    smart_office_system = SmartOfficeSystem()
    
    # Simulate system updates over time
    for time_step in range(1, 21):
        smart_office_system.update(time_step)
    
    # Plot the system state in an area chart
    smart_office_system.plot_state()
