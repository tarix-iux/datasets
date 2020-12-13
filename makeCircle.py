import numpy as np


class make_circle():

    def __init__(self, n_samples=10, noise=0, ex_diameter=5.2, int_diameter=2.2):
        self.N_samples = n_samples
        self.Noise = noise
        self.H = (ex_diameter, int_diameter)
        self.Data_x = []
        self.Target = []

    def make_data(self):

        #circulo externo
        for _ in range(self.N_samples):
            X = np.random.choice(np.linspace(-self.H[0], self.H[0], 1000))
            y = np.sqrt(self.H[0]**2 - X**2) * np.random.choice([-1, 1])
            y += y*np.random.choice(np.linspace(0, self.Noise, 10))
            X += X*np.random.choice(np.linspace(0, self.Noise, 10))
            self.Data_x.append([X, y])
            self.Target.append(1)

        #circulo interno
        for _ in range(self.N_samples):
            X = np.random.choice(np.linspace(-self.H[1], self.H[1], 1000))
            y = np.sqrt(self.H[1]**2 - X**2) * np.random.choice([-1, 1])
            y += y*np.random.choice(np.linspace(0, self.Noise, 10))
            X += X*np.random.choice(np.linspace(0, self.Noise, 10))            
            self.Data_x.append([X, y])
            self.Target.append(0)

        
    def get_data(self):

        return np.array(self.Data_x), np.array(self.Target)