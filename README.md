# FTP-Codes-CD5B

This repository contains various tools and scripts related to solving and visualizing the **Freeze-Tag Problem (FTP)**. The project includes 3D visualizers, calculation utilities, and reference GIFs that show some working examples.

## Project Structure

### 1. 3D visualizers
This folder contains Python scripts for visualizing various geometric structures in 3D used in our woek:

- **2by2Division.py**: Visualizes the division of a cross-polytope into parts with half its diameter.
- **2thirdsDivision.py**: Implements a 2/3 division visualization of a cross-polytope.
- **pyramid.py**: Generates a 3D pyramid visualization to evaluate its subdivisions (not used).
- **pyramidIn2by2Division.py**: Visualizes a pyramid with a 2 by 2 division overlay, used for analyzing solution strategies.
- **unitBall.py**: Simulates a unit ball in $l_1$.

### 2. Calculations/
This folder contains utilities for calculating geometric properties and makespan calculations related to FTP:

- **GeodesicToEuclideanRatioCalculator.ipynb**: Our calculations for finding the ratio between geodesic and Euclidean distances.
- **MakespanCalculator.cpp**: This code calculates the makespan, the total time needed to unfreeze all robots in the FTP setup under various normes in different dimensions.

