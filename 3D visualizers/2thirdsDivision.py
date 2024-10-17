import numpy as np
import pyvista as pv

# Define points and vertices
points = np.array([
    [0, 0, 0],
    [0, 0, 1/3],
    [0, 0, -1/3],
    [0, 1/3, 0],
    [0, -1/3, 0],
    [1/3, 0, 0],
    [-1/3, 0, 0],
])

vertices = np.array([
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1]
])

# Define faces using vertex indices
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
def draw(mesh, plotter, r=1, color='cyan', x=0, y=0, z=0):
    mesh_scaled = pv.PolyData(vertices * r + [x, y, z], faces)
    plotter.add_mesh(mesh_scaled, color=color, opacity=0.6, show_edges=True, edge_color='red')

# Initialize the plotter
plotter = pv.Plotter()

r = 2/3
p = 1 - r

# Draw the mesh in different positions and colors
draw(mesh, plotter, r, 'cyan', 0, 0, p)
draw(mesh, plotter, r, 'cyan', 0, 0, -p)
draw(mesh, plotter, r, 'red', 0, p, 0)
draw(mesh, plotter, r, 'yellow', 0, -p, 0)
draw(mesh, plotter, r, 'purple', p, 0, 0)
draw(mesh, plotter, r, 'blue', -p, 0, 0)

# Add points to the plot
plotter.add_points(points, color='blue', point_size=10, render_points_as_spheres=True)

# Show the plot
plotter.show()

