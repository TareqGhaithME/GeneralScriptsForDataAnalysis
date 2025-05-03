import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importDATA
data = pd.read_csv("Data/0.1noWaxData.csv")

#FFT,note that its magnitude and shifted aswell
freq = np.arange(0,40,1)
fxt = np.fft.fft(data['AmpZ'])
mag = np.fft.fftshift(np.abs(fxt))

#Plotting
plt.plot(freq, mag)
plt.title("Plot of XT")
plt.show()
