import numpy as np
import matplotlib.pyplot as plt
alpha_unicode = "\u03B1"
gamma_unicode = "\u03B3"
beta_unicode = "\u03B2"
mu_unicode = "\u03BC"
Beta = np.linspace(0, 1, 20)
Gamma = [0.01, 0.02]
beta_gamma_1 = Beta/Gamma[0]
beta_gamma_2 = Beta/Gamma[1]

average_1 = np.load('2022-11-28-09-38-12R_inf_gamma=0.01.npy')
average_2 = np.load('2022-11-28-09-44-56R_inf_gamma=0.02.npy')

# Function of Beta / gamma
plt.plot(beta_gamma_1, average_1, "o", color="blue", markersize=4)
plt.plot(beta_gamma_2, average_2, "o", color="green", markersize=4)
plt.legend([f"{gamma_unicode}={Gamma[0]}", f"{gamma_unicode}={Gamma[1]}"])
plt.xlabel(f'{beta_unicode}/{gamma_unicode}')
plt.title(f"Final number of recovered agents as a function of {beta_unicode}/{gamma_unicode} averaged over 5 iterations")
plt.show()