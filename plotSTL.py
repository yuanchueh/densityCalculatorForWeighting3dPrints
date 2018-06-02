from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import math

# Further Documentation
# http://numpy-stl.readthedocs.io/en/latest/tests.html#tests-test-rotate-module
# https://w.wol.ph/2015/07/10/rendering-stl-files-matplotlib-numpy-stl/

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Load the STL files and add the vectors to the plot
# your_mesh = mesh.Mesh.from_file('/home/yuanchueh/Documents/git/densityCalculatorForWeighting3dPrints/Test/spine.stl')
your_mesh = mesh.Mesh.from_file('/home/yuanchueh/Documents/git/densityCalculatorForWeighting3dPrints/Test/prop.stl')
# your_mesh.rotate("x", 45)
your_mesh.rotate([0, 0, 0], math.radians(90))
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale to the mesh size
scale = your_mesh.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()
