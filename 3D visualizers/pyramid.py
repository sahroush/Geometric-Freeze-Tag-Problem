import numpy as np
import pyvista as pv

# Define the vertices of the first mesh
vertices = np.array([
    [0, 0, 0],
    [1, 1, 0],
    [1, 0, 1],  
    [0, 1, 1],
])

# Define the faces for the first mesh
faces = np.hstack([
    [3, 0, 1, 2],
    [3, 1, 2, 3],
    [3, 0, 2, 3],
    [3, 0, 1, 3]
])

mesh = pv.PolyData(vertices, faces)

plotter = pv.Plotter()

def draw(r=1, col='cyan', x=0, y=0, z=0):
    mesh = pv.PolyData(vertices * r + [x, y, z], faces)
    plotter.add_mesh(mesh, color=col, opacity=0.6, show_edges=True, edge_color='red')

r = 1/2
p = 1 - r

draw()
draw(r, 'red', 0, 0, 0)
draw(r, 'red', 0, 1/2, 1/2)
draw(r, 'red', 1/2, 0, 1/2)
draw(r, 'red', 1/2, 1/2, 0)

points = np.array([
    [1/2, 1/2, 1/2]
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

draw(r, 'purple', 1/2, 1/2, 1/2)

plotter.add_points(points, color='blue', point_size=10, render_points_as_spheres=True)

plotter.show()

