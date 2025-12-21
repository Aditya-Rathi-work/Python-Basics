import numpy as np
import matplotlib.pyplot as plt

rpm = np.linspace(1000, 6000, 50)
torque = 200 - 0.05 * (rpm - 3000) **2
 
plt.plot(rpm, torque)
plt.title("Torque Curve")
plt.xlabel("RPM")
plt.ylabel("Torque (Nm)")
plt.show()
