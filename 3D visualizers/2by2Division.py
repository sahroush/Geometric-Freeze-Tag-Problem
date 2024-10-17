import numpy as np
import pyvista as pv


points = np.array([
    [0, 0, 0],
    [1/2, 0, 0],
    [-1/2, 0, 0],
    [0, 1/2, 0],
    [0, -1/2, 0],
    [0, 0, 1/2],
    [0, 0, -1/2],
])


vertices = np.array([
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1]
])

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


mesh = pv.PolyData(vertices, faces)

# Plotter initialization
plotter = pv.Plotter()

# Function to draw a mesh with scaling and translation
def draw(mesh, plotter, r=1, col='cyan', x=0, y=0, z=0):
    mesh_scaled = pv.PolyData(mesh.points * r + [x, y, z], mesh.faces)
    plotter.add_mesh(mesh_scaled, color=col, opacity=0.6, show_edges=True, edge_color='red')

# Set scale and position parameters
r = 1/2
p = 1 - r


draw(mesh, plotter, r, 'cyan', 0, 0, p)
draw(mesh, plotter, r, 'yellow', 0, p, 0)
draw(mesh, plotter, r, 'red', p, 0, 0)
draw(mesh, plotter, r, 'cyan', 0, 0, -p)
draw(mesh, plotter, r, 'yellow', 0, -p, 0)
draw(mesh, plotter, r, 'red', -p, 0, 0)

# Adding the initial points as blue spheres
plotter.add_points(points, color='blue', point_size=10, render_points_as_spheres=True)

# Show the plot
plotter.show()
