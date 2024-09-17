'''
Lunar Trailblazer App Technical Question 2 Code
Richard Hoffmann - Caltech Undergrad
9/17/24
'''

import matplotlib.pyplot as plt
import csv

# Reading dataset
filename = "sat_realtime_telemetry.csv"
f = open(filename, "r")
reader = csv.DictReader(f)

# lists to store columns containing relevant data
time = []
solar_x = []
solar_y = []
solar_z = []
battery = []
system_current = []
bc_temp_1 = []
bc_temp_2 = []
sun_sensor_x = []
sun_sensor_y = []
sun_sensor_z = []

# reading dataset and extracting relevant columns
for col in reader:
    time.append(col["Satellite Date/Time UTC"])
    solar_x.append(col['Solar Panel Voltage X mV'])
    solar_y.append(col['Solar Panel Voltage Y mV'])
    solar_z.append(col['Solar Panel Voltage Z mV'])
    battery.append(col['Battery Voltage mV'])
    system_current.append(col['Total System Current mA'])
    bc_temp_1.append(col['Boost Converter Temp 1 C'])
    bc_temp_2.append(col['Boost Converter Temp 1 C'])
    sun_sensor_x.append(col['Sun Sensor X+'])
    sun_sensor_y.append(col['Sun Sensor Y+'])
    sun_sensor_z.append(col['Sun Sensor Z+'])

# plotting total solar panel voltage over time
plt.figure()
plt.plot(time, solar_x, label="X")
plt.plot(time, solar_y, label="Y")
plt.plot(time, solar_z, label="Z")
plt.legend()
plt.title("Total Solar Panel Voltage over Time")
plt.xlabel("Time")
plt.ylabel("Voltage (mV)")
plt.show()

# plotting y-axis solar panel voltage over time
plt.plot(time, solar_y)
plt.title("Solar Panel Voltage Y over Time")
plt.xlabel("Time")
plt.ylabel("Voltage (mV)")

# plotting battery voltage over time
plt.figure()
plt.plot(time, battery)
plt.title("Battery Voltage over Time")
plt.xlabel("Time")
plt.ylabel("Voltage (mV)")
plt.show()

# plotting system current over time
plt.figure()
plt.plot(time, system_current)
plt.title("Total System Current over Time")
plt.xlabel("Time")
plt.ylabel("Current (mA)")
plt.show()

# plotting boost converter temperature over time
# confirming if plots coincide with each other
plt.figure()
plt.plot(time, bc_temp_1, label='Converter 1')
plt.plot(time, bc_temp_2, label='Converter 2')
plt.title("Boost Converter Temperature over Time")
plt.xlabel("Time")
plt.ylabel("Temperature (C)")
plt.legend()
plt.show()

# plotting sun sensor temperature over time
plt.figure()
plt.plot(time, sun_sensor_x, label='X+')
plt.plot(time, sun_sensor_y, label='Y+')
plt.plot(time, sun_sensor_z, label='Z+')
plt.title("Sun Sensor Data over Time")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()

