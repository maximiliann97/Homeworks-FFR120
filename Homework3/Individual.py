class Individual:
    def __init__(self, state: str, lattice: int):
        def update_state(self, state: str):
            if state == 'recovered':
                self.state = 'recovered'
            elif state == 'immune':
                self.state = 'immune'
            elif state == 'infected':
                self.state = 'infected'
            elif state == 'diseased':
                self.state = 'diseased'
            elif state == 'susceptible':
                self.state = 'susceptible'
            else:
                raise Exception('State not valid')
            




