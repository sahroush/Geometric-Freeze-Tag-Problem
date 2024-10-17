import numpy as np
import pyvista as pv

# Define the points and vertices
points = np.array([
    [0, 0, 1],
    [0, 0, -1],
    [0, 1, 0],
    [0, -1, 0],
    [1, 0, 0],
    [-1, 0, 0],
])

vertices = np.array([
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1]
])

# Define the faces as arrays of indices
faces = np.hstack([
    [3, 0, 2, 4],
    [3, 0, 3, 4],
    [3, 0, 2, 5],
    [3, 0, 3, 5],
    [3, 1, 2, 4],
    [3, 1, 3, 4],
    [3, 1, 2, 5],
    [3, 1, 3, 5],
])

# Create a PolyData object
mesh = pv.PolyData(vertices, faces)

# Plotting function
def draw(r=1, color='cyan', x=0, y=0, z=0):
    mesh_scaled = pv.PolyData(vertices * r + [x, y, z], faces)
    plotter.add_mesh(mesh_scaled, color=color, opacity=0.6, show_edges=True, edge_color='red')

# Initialize the plotter
plotter = pv.Plotter()

# Example draw call
draw()

# Add points to the plot
plotter.add_points(np.array([[0, 0, 0]]), color='yellow', point_size=10, render_points_as_spheres=True)
plotter.add_points(points, color='blue', point_size=10, render_points_as_spheres=True)

# Show the plot
plotter.show()

