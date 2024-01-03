# solar-system-modeling

In this Python program, a simplified modeling of the solar system is implemented. The script defines a "Planet" class that represents planets with specific properties such as radius and year length. The positions of planets on a given day and the Euclidean distance between two planets on a specific day are calculated using trigonometry.

**Simulation** <br />

The script simulates the solar system for 1000 days, computing the distance between Earth and Mercury, Venus, and Mars each day. Two cases are considered: <br />
(1) distances are stored exactly, and <br />
(2) a noisy version of distances is stored. <br />

In addition, the script simulates the solar system for 1000 years, computes the average daily distances for all pairs of planets, and creates an 8x8 array showing the average distance between each pair of planets. <br />

The code provides answers to questions related to distances, functions, time-series generation, and the 8x8 matrix. It offers visualizations of time-series plots with average distances, considering noise and noise-less scenarios. 

**Libraries Used:** 

math
numpy
matplotlib.pyplot
