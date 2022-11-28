import numpy as np


class Individual:
    def __init__(self, state: str, lattice: int):
        if isinstance(lattice+1, int):
            self.position = np.random.randint(lattice, size=2)
        else:
            raise ValueError('Lattice not valid')

        if state == 'recovered':
            self.state = 'recovered'
        elif state == 'infected':
            self.state = 'infected'
        elif state == 'diseased':
            self.state = 'diseased'
        elif state == 'susceptible':
            self.state = 'susceptible'
        else:
            raise TypeError('State not valid')

    def update_state(self, state: str):
        if state == 'recovered':
            self.state = 'recovered'
        elif state == 'infected':
            self.state = 'infected'
        elif state == 'diseased':
            self.state = 'diseased'
        elif state == 'susceptible':
            self.state = 'susceptible'
        else:
            raise TypeError('State not valid')

    def move(self, direction, lattice):
        if direction == 'up' and self.position[1] < lattice:
            self.position[1] += 1
        if direction == 'down' and self.position[1] > 0:
            self.position[1] -= 1
        if direction == 'right' and self.position[0] < lattice:
            self.position[0] += 1
        if direction == 'left' and self.position[0] > 0:
            self.position[0] -= 1

    def update_position(self, position: np.ndarray):
        if isinstance(position, np.ndarray):
            self.position = position
        else:
            raise TypeError('Has to be ndarray')



