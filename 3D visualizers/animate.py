from manim import *

class CrossPolytope3D(Scene):
    def construct(self):
        # Create a 3D axis for reference
        axes = ThreeDAxes()

        # Define the vertices of the cross-polytope (octahedron)
        vertices = [
            np.array([1, 0, 0]), np.array([-1, 0, 0]),   # ±x-axis
            np.array([0, 1, 0]), np.array([0, -1, 0]),   # ±y-axis
            np.array([0, 0, 1]), np.array([0, 0, -1])    # ±z-axis
        ]

        # Create the edges (lines connecting vertices)
        edges = [
            Line(vertices[0], vertices[2]), Line(vertices[0], vertices[4]), Line(vertices[0], vertices[3]), Line(vertices[0], vertices[5]),
            Line(vertices[1], vertices[2]), Line(vertices[1], vertices[4]), Line(vertices[1], vertices[3]), Line(vertices[1], vertices[5]),
            Line(vertices[2], vertices[4]), Line(vertices[2], vertices[5]), Line(vertices[3], vertices[4]), Line(vertices[3], vertices[5])
        ]

        # Add axes and octahedron edges to the scene
        self.add(axes)
        for edge in edges:
            self.add(edge)

        # Animate drawing a line between two points
        a = np.array([0, 0, 0])  # Start point at origin
        b = np.array([1, 1, 1])  # End point

        # Create the line between a and b
        line = Line(a, b, color=RED)
        
        # Camera angle for 3D rotation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Animate drawing the line
        self.play(Create(line), run_time=2)
        self.wait()

