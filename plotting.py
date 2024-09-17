import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

filename = "sat_realtime_telemetry.csv"

f = open(filename, "r")

reader = csv.DictReader(f)


solar_x = []
solar_y = []
time = []


for col in reader:
    time.append(col["Satellite Date/Time UTC"])
    solar_x.append(col['Solar Panel Voltage X mV'])
    solar_y.append(col['Solar Panel Voltage Y mV'])

plt.figure()
plt.plot(time, solar_x, label=None)
plt.title("Solar Panel Voltage X over Time")
plt.xlabel("Time")
plt.ylabel("Voltage (mV)")
plt.show()

plt.figure()
plt.plot(time, solar_y)
plt.title("Solar Panel Voltage Y over Time")
plt.xlabel("Time")
plt.ylabel("Voltage (mV)")

plt.show()


