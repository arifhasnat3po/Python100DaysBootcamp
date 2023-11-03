wind_speed = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1]

import matplotlib.pyplot as plt
import numpy as np

# Set the time range
time = np.arange(0, 7, 1)

# Set the temperature, CO2 levels, and wind speed
temperature = [18, 19, 20, 21, 22, 21, 20]
co2_levels = [400, 410, 420, 430, 440, 430, 420]
sunlight = [0.2, 0.3, 0.4, 0.5, 0.6, 0.5, 0.4]
wind_speed = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1]

# Create the plot
fig, axs = plt.subplots(2, 1, sharex=True)

# Plot the temperature
axs[0].plot(time, temperature, label="Temperature (°C)")
axs[0].set_ylabel("Temperature (°C)")
axs[0].legend()

# Plot the CO2 levels
axs[1].plot(time, co2_levels, label="CO2 levels (ppm)")
axs[1].set_xlabel("Time (minutes)")
axs[1].set_ylabel("CO2 levels (ppm)")
axs[1].legend()

# Create a secondary y-axis for sunlight and wind speed
ax2 = axs[0].twinx()

# Plot the sunlight
ax2.plot(time, sunlight, label="Sunlight (lux)", color='orange')

# Plot the wind speed
ax2.plot(time, wind_speed, label="Wind speed (m/s)", color='red')

# Update the legend
ax2.legend()

# Add conditions
axs[0].fill_between(time, 18, 22, color="lightgreen", alpha=0.5)
axs[0].text(3.5, 22.5, "Comfort range", ha="center", va="center")
ax2.fill_between(time, 1.0, 1.5, color="pink", alpha=0.5)
ax2.text(3.5, 1.25, "High wind speed", ha="center", va="center")

# Set the title
fig.suptitle("Temperature, CO2 levels, and wind speed in a corporate office over 7 minutes")

# Show the plot
plt.show()
