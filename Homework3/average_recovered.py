import numpy as np
import matplotlib.pyplot as plt

# Initialize
alpha_unicode = "\u03B1"
gamma_unicode = "\u03B3"
beta_unicode = "\u03B2"
mu_unicode = "\u03BC"
Beta = np.linspace(0.1, 0.9, 9)
Gamma = [0.01, 0.02]

# Load
gamma_1 = np.load('R_inf_gamma=0.01_1.npy') + np.load('R_inf_gamma=0.01_2.npy') + np.load('R_inf_gamma=0.01_3.npy') + \
          np.load('R_inf_gamma=0.01_4.npy') + np.load('R_inf_gamma=0.01_5.npy')

gamma_2 = np.load('R_inf_gamma=0.02_1.npy') + np.load('R_inf_gamma=0.02_2.npy') + np.load('R_inf_gamma=0.02_1.npy') +\
          np.load('R_inf_gamma=0.02_4.npy') + np.load('R_inf_gamma=0.02_5.npy')
average_1 = gamma_1/5
average_2 = gamma_2/5

beta_gamma_1 = Beta/Gamma[0]
beta_gamma_2 = Beta/Gamma[1]

"""
# Function of beta
plt.plot(Beta, average_1, "o", color="blue", markersize=4)
plt.plot(Beta, average_2, "o", color="green", markersize=4)
plt.legend([f"{gamma_unicode}={Gamma[0]}", f"{gamma_unicode}={Gamma[1]}"])
plt.xlabel(f'{beta_unicode}')
plt.title(f"Final number of recovered agents as a function of the infection rate {beta_unicode} averaged over 5 iterations")
plt.show()
"""
"""
# Function of Beta / gamma
plt.plot(beta_gamma_1, average_1, "o", color="blue", markersize=4)
plt.plot(beta_gamma_2, average_2, "o", color="green", markersize=4)
plt.legend([f"{gamma_unicode}={Gamma[0]}", f"{gamma_unicode}={Gamma[1]}"])
plt.xlabel(f'{beta_unicode}/{gamma_unicode}')
plt.title(f"Final number of recovered agents as a function of {beta_unicode}/{gamma_unicode} averaged over 5 iterations")
plt.show()
"""

# Phase diagram
# y_max = np.max(beta_gamma_1)
# y_min = np.min(beta_gamma_1)
# x_max = np.max(Beta)
# x_min = np.min(Beta)
# plt.imshow(average_1, extent=[x_min, x_max, y_min, y_max])
# plt.show()