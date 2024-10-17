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

# Define the faces as arrays of indices (using vertex indices)
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

# Plot the mesh and points
plotter = pv.Plotter()

def draw(r=1, col='cyan', x=0, y=0, z=0):
    mesh = pv.PolyData(vertices*r+[x,y,z], faces)
    plotter.add_mesh(mesh, color = col, opacity = 0.6, show_edges=True, edge_color='red')

r = 1/2
p = 1-r

draw()
# draw(r, 'cyan', 0, 0, p)
# draw(r, 'cyan', 0, 0, -p)
# draw(r, 'cyan', 0, p, 0)
# draw(r, 'cyan', 0, -p, 0)
# draw(r, 'cyan', p, 0, 0)
# draw(r, 'cyan', -p, 0, 0)
#draw(3*r, 'red', 0, 0, p)
#draw(r/2, 'purple', 1/4, 1/4, 1/4)
# draw(r, 'blue', 0, 0, 0)
# draw(r, 'purple', 0, p/2, p/2)
# draw(r, 'purple', 0, p/2, -p/2)
# draw(r, 'purple', 0, -p/2, p/2)
# draw(r, 'purple', 0, -p/2, -p/2)
# draw(r, 'purple', p/2, p/2, 0)
# draw(r, 'purple', p/2, -p/2, 0)
# draw(r, 'purple', -p/2, p/2, 0)
# draw(r, 'purple', -p/2, -p/2, 0)
# draw(r, 'purple', p/2, 0, p/2)
# draw(r, 'purple', p/2, 0, -p/2)
# draw(r, 'purple', -p/2, 0, p/2)
# draw(r, 'purple', -p/2, 0, -p/2)

plotter.add_points(np.array([[0,0,0]]), color='yellow', point_size=10, render_points_as_spheres=True)
plotter.add_points(points, color='blue', point_size=10, render_points_as_spheres=True)

# Show the plot
plotter.show()
