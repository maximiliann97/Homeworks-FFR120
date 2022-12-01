import YearsInPrison as yip
import matplotlib.pyplot as plt
import numpy as np

# Parameters
rounds = 10
M = np.linspace(0, rounds, 11).astype(int)
N = np.linspace(0, rounds, 11).astype(int)
R = 0.5
S = 1.5
P = 1

# Initialization
years_matrix = np.zeros([rounds+1, rounds+1])

for n in N:
    for m in M:
        years = yip.years(n, m, rounds, R, S, P)
        years_matrix[n, m] = years

print(years_matrix)
plt.imshow(years_matrix, origin='lower')
plt.title(f'Years i prison, R={R}, S={S}')
plt.ylabel('n')
plt.xlabel('m')

plt.colorbar()
plt.show()


# Plot 13.1a
# plt.axvline(x = 6, color = 'black', label = 'axvline - full height', linestyle='dashed')
# plt.scatter(N, years_array, clip_on=False)
# plt.ylabel('Years in prison')
# plt.xlabel('n')
# plt.xlim([N[0], N[len(N)-1]])
# plt.show()