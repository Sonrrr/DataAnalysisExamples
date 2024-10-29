import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

num_points = 1000
x = np.linspace(0, 10, num_points)
signal = np.sin(x)
noise = np.random.normal(0, 0.5, num_points)
noisy_signal = signal + noise

filtered_signal = savgol_filter(noisy_signal, window_length=301, polyorder=4)

signal_power = np.mean(signal**2)
noise_power = np.mean((filtered_signal - signal)**2)
snr = 10 * np.log10(signal_power / noise_power) 

print(f"Sinyal-Gürültü Oranı (SNR): {snr:.2f} dB")

plt.figure(figsize=(10, 6))
plt.plot(x, signal, label="Orijinal Sinyal")
plt.plot(x, noisy_signal, label="Gürültülü Sinyal", color='orange', alpha=0.6)
plt.plot(x, filtered_signal, label="Filtrelenmiş Sinyal", color='blue')
plt.legend()
plt.xlabel("Zaman")
plt.ylabel("Genlik")
plt.title("Orijinal, Gürültülü ve Filtrelenmiş Sinyal")
plt.show()
