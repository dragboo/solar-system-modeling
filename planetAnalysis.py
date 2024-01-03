import math
import numpy as np
import matplotlib.pyplot as plt


class Planet:
    def __init__(self, radius, year_length):
        self.radius = radius
        self.year_length = year_length

    def position(self,day):
        '''
        returns position of the planets on a given day
        '''
        angle = (2 * math.pi * day) / self.year_length
        x = round(self.radius * math.cos(angle), 10)
        y = round(self.radius * math.sin(angle), 10)
        return x,y
    
def distance(planet1, planet2, day):
    '''
    returns the distance between the planets on a given day
    '''
    x1, y1 = planet1.position(day)
    x2, y2 = planet2.position(day)
    return math.sqrt((x2 - x1)**2 + (y2-y1)**2)


# defining instances of the class for each planet
mercury = Planet(3.5, 88)
venus = Planet(6.7, 225)
earth = Planet(9.3, 365)
mars = Planet(14.2, 687)
jupiter = Planet(48.4, 4333)
saturn = Planet(88.9, 10759)
uranus = Planet(179, 30687)
neptune = Planet(288, 60190)

# Assigning names to the instances 
mercury.name = "Mercury"
venus.name = "Venus"
earth.name = "Earth"
mars.name = "Mars"
jupiter.name = "Jupiter"
saturn.name = "Saturn"
uranus.name = "Uranus"
neptune.name = "Neptune"

# Testing the position method
print(mercury.position(0))
print(mercury.position(22))

# Testing the distance function
d = distance(earth, mars, 732)
print(f"The distance betweeen Earth and Mars on day 732 is: {d}")

# Simulation for 1000 days

def simulate(noise_std = None):
    '''
    computes the distance between Earth to Mercury, Venus and Mars each day
    '''
    days = 1000
    distances_exact = {'Mercury': [], 'Venus': [], 'Mars': []}

    for day in range(days):
        distance_mercury = distance(earth, mercury, day)
        distance_venus = distance(earth, venus, day)
        distance_mars = distance(earth, mars, day)

        distances_exact["Mercury"].append(distance_mercury)
        distances_exact["Venus"].append(distance_venus)
        distances_exact["Mars"].append(distance_mars)
    
    # Applying noise to distances
    if noise_std is not None:
        distances_exact["Mercury"] += np.random.normal(0, noise_std, days)
        distances_exact["Venus"] += np.random.normal(0, noise_std, days)
        distances_exact["Mars"] += np.random.normal(0, noise_std, days)
    
    # Plotting time-series graph
    plt.figure(figsize=(10, 6))
    for planet in distances_exact.keys():
        plt.plot(distances_exact[planet], label=f'{planet}', alpha=0.5)
    
    # Plotting horizontal lines for the mean distnaces of each planet
    avg_mercury = np.mean(distances_exact["Mercury"])
    avg_venus = np.mean(distances_exact["Venus"])
    avg_mars = np.mean(distances_exact["Mars"])

    plt.axhline(y=avg_mercury, color='red', label=f"Mean Mercury: {avg_mercury: 2f}")
    plt.axhline(y=avg_venus, color='green', label=f"Mean Venus: {avg_venus: 2f}")
    plt.axhline(y=avg_mars, color='blue', label=f"Mean Mars: {avg_mars: 2f}")

    plt.title(f'Distance Simulation {"with Noise (STD ={})".format(noise_std) if noise_std is not None else "Noise-less"}')
    plt.xlabel('Day')
    plt.ylabel('Distance')
    plt.legend()
    plt.show()

# Running the noise-less simulation for 1000 days
simulate()

# Running simulations with nosie for different STD values with a step size of 3
for std in np.arange(0.5, 10.5, 3):
    simulate(noise_std=std)

# Simualtion for 1000 years

def simulate_noiseless(years):
    '''
    computing the average daily distances for all pairs of planets for 1000 years
    '''

    # Creating a list containing all eight planets 
    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    # Creating a 8x8 array showing avg distance between all pairs of planets
    avg_distance_matrix = np.zeros((len(planets), len(planets)))
    
    # Calculating average distances for all pairs of planets
    for i, planet1 in enumerate(planets):
        for j, planet2 in enumerate(planets):
            distances = [distance(planet1, planet2, day) for day in range(365 * years)]
            avg_distance_matrix[i,j] = np.mean(distances)

    # Verifying the array is symmetric and printing it in the form of a table
    assert np.allclose(avg_distance_matrix, avg_distance_matrix.T), "Array is not symmetric"
    print("Average Distance Matrix:")
    print(np.round(avg_distance_matrix, 2))

    # Finding the planet closest to Earth on average and printing it
    closest_planet_index = np.argmin(np.mean(avg_distance_matrix, axis=0))
    closest_planet = planets[closest_planet_index]
    print(f"\nPlanet closest to Earth on average: {closest_planet.name}")

# Running the noise-less simulation for 1000 years
simulate_noiseless(1000)
