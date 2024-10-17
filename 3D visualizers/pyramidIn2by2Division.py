import numpy as np
import pyvista as pv

# Define the first set of points
points = np.array([
    [0, 0, 0],
    [1/2, 1/2, 0],
    [1/2, 0, 1/2],
    [0, 1/2, 1/2]
])

# Define the first set of vertices and faces
vertices_1 = np.array([
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1]
])

faces_1 = np.hstack([
    [3, 0, 2, 4],
    [3, 0, 3, 4],
    [3, 0, 2, 5],
    [3, 0, 3, 5],
    [3, 1, 2, 4],
    [3, 1, 3, 4],
    [3, 1, 2, 5],
    [3, 1, 3, 5],
])

# Define the second set of vertices and faces (tetrahedron-like)
vertices_2 = np.array([
    [0, 0, 0],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1],
])

faces_2 = np.hstack([
    [3, 0, 1, 2],
    [3, 1, 2, 3],
    [3, 0, 2, 3],
    [3, 0, 1, 3]
])

# Create a PolyData object for both meshes
mesh_1 = pv.PolyData(vertices_1, faces_1)
mesh_2 = pv.PolyData(vertices_2, faces_2)

# Plotter initialization
plotter = pv.Plotter()

# Function to draw a mesh with scaling and translation
def draw(mesh, plotter, r=1, col='cyan', x=0, y=0, z=0):
    mesh_scaled = pv.PolyData(mesh.points * r + [x, y, z], mesh.faces)
    plotter.add_mesh(mesh_scaled, color=col, opacity=0.6, show_edges=True, edge_color='red')

# Set scale and position parameters
r = 1/2
p = 1 - r

# Drawing the first mesh with different translations
draw(mesh_1, plotter, r, 'cyan', 0, 0, p)
draw(mesh_1, plotter, r, 'cyan', 0, p, 0)
draw(mesh_1, plotter, r, 'cyan', p, 0, 0)
draw(mesh_1, plotter, r, 'cyan', 0, 0, -p)
draw(mesh_1, plotter, r, 'cyan', 0, -p, 0)
draw(mesh_1, plotter, r, 'cyan', -p, 0, 0)

# Drawing the second mesh (tetrahedron-like) in the center
draw(mesh_2, plotter, r, 'purple', 0, 0, 0)

# Adding the initial points as blue spheres
plotter.add_points(points, color='blue', point_size=10, render_points_as_spheres=True)

# Show the plot
plotter.show()
