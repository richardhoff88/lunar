import matplotlib.pyplot as plt
import csv

filename = "sat_realtime_telemetry.csv"

f = open(filename, "r")

reader = csv.DictReader(f)

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

# plt.figure()
# plt.plot(time, solar_x, label="X")
# plt.plot(time, solar_y, label="Y")
# plt.plot(time, solar_z, label="Z")
# plt.legend()
# plt.title("Total Solar Panel Voltage over Time")
# plt.xlabel("Time")
# plt.ylabel("Voltage (mV)")
# plt.show()

# plt.plot(time, solar_y)
# plt.title("Solar Panel Voltage Y over Time")
# plt.xlabel("Time")
# plt.ylabel("Voltage (mV)")

# plt.figure()
# plt.plot(time, battery)
# plt.title("Battery Voltage over Time")
# plt.xlabel("Time")
# plt.ylabel("Voltage (mV)")
# plt.show()

# plt.figure()
# plt.plot(time, system_current)
# plt.title("Total System Current over Time")
# plt.xlabel("Time")
# plt.ylabel("Current (mA)")
# plt.show()

# plt.figure()
# plt.plot(time, bc_temp_1, label='Converter 1')
# plt.plot(time, bc_temp_2, label='Converter 2')
# plt.title("Boost Converter Temperature over Time")
# plt.xlabel("Time")
# plt.ylabel("Temperature (C)")
# plt.legend()
# plt.show()


plt.figure()
plt.plot(time, sun_sensor_x, label='X+')
plt.plot(time, sun_sensor_y, label='Y+')
plt.plot(time, sun_sensor_z, label='Z+')
plt.title("Sun Sensor Data over Time")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()

