import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

filename = "sat_realtime_telemetry.csv"

f = open(filename, "r")

reader = csv.DictReader(f)


solar_x = []
solar_y = []
solar_z = []
battery = []
time = []


for col in reader:
    time.append(col["Satellite Date/Time UTC"])
    solar_x.append(col['Solar Panel Voltage X mV'])
    solar_y.append(col['Solar Panel Voltage Y mV'])
    solar_z.append(col['Solar Panel Voltage Z mV'])
    battery.append(col['Battery Voltage mV'])

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

plt.figure()
plt.plot(time, battery)
plt.title("Battery Voltage over Time")
plt.xlabel("Time")
plt.ylabel("Voltage (mV)")
plt.show()


