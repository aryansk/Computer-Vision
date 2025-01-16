
import numpy as np
import matplotlib.pyplot as plt

triangle = np.array([[0, 0], [1, 0], [0.5, 1]])

def plot_triangle(triangle, title):
    plt.figure()
    plt.plot([triangle[0, 0], triangle[1, 0]], [triangle[0, 1], triangle[1, 1]], 'r-')
    plt.plot([triangle[1, 0], triangle[2, 0]], [triangle[1, 1], triangle[2, 1]], 'g-')
    plt.plot([triangle[2, 0], triangle[0, 0]], [triangle[2, 1], triangle[0, 1]], 'b-')
    plt.fill(triangle[:, 0], triangle[:, 1], 'y', alpha=0.3)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.grid(True)
    plt.title(title)
    plt.show()

def translate(triangle, tx, ty):
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])
    triangle_h = np.hstack((triangle, np.ones((triangle.shape[0], 1))))  # Homogeneous coords
    transformed = triangle_h.dot(translation_matrix.T)[:, :-1]  # Apply transform and return to 2D
    return transformed

def scale(triangle, sx, sy):
    scaling_matrix = np.array([[sx, 0],
                               [0, sy]])
    transformed = triangle.dot(scaling_matrix.T)
    return transformed

def rotate(triangle, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                [np.sin(theta), np.cos(theta)]])
    transformed = triangle.dot(rotation_matrix.T)
    return transformed

def reflect(triangle, axis='x'):
    if axis == 'x':
        reflection_matrix = np.array([[1, 0], [0, -1]])
    elif axis == 'y':
        reflection_matrix = np.array([[-1, 0], [0, 1]])
    transformed = triangle.dot(reflection_matrix.T)
    return transformed

def shear(triangle, shx, shy):
    shearing_matrix = np.array([[1, shx], [shy, 1]])
    transformed = triangle.dot(shearing_matrix.T)
    return transformed

translated_triangle = translate(triangle, 2, 3)
scaled_triangle = scale(triangle, 2, 2)
rotated_triangle = rotate(triangle, 45)
reflected_triangle = reflect(triangle, axis='x')
sheared_triangle = shear(triangle, 1, 0)

plot_triangle(triangle, "Original Triangle")
plot_triangle(translated_triangle, "Translated Triangle (tx=2, ty=3)")
plot_triangle(scaled_triangle, "Scaled Triangle (sx=2, sy=2)")
plot_triangle(rotated_triangle, "Rotated Triangle (45 degrees)")
plot_triangle(reflected_triangle, "Reflected Triangle (x-axis)")
plot_triangle(sheared_triangle, "Sheared Triangle (shx=1)")