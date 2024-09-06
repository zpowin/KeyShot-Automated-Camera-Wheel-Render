# -*- coding: utf-8 -*-
# VERSION 0.0.2
# HEADLESS COMPLIANT
# Renders specified cameras and rotates models as needed.

import os
import time

# Constants
RENDER_TIME = 60
OUTPUT_PATH = "D:\\0-KEYSHOT\\"
RENDER_WIDTH = 2560
RENDER_HEIGHT = 2560
CAMERA_PREFIX = "相机"


# Initialize transformation matrices
ROTATIONS = {
    "camera3": luxmath.Matrix().makeIdentity().rotateAroundAxis(luxmath.Vector((1, 0, 0)), -90),
    "camera4": luxmath.Matrix().makeIdentity().rotateAroundAxis(luxmath.Vector((1, 0, 0)), -70).rotateAroundAxis(luxmath.Vector((0, 0, 1)), -30)
}

# Helper function to manually clone a matrix
def clone_matrix(matrix):
    """Creates a deep copy of a matrix by copying its data."""
    return luxmath.Matrix(matrix.val())

# Create inverted transformation matrices
ROTATIONS_INVERT = {}

for key, matrix in ROTATIONS.items():
    # Clone matrix and invert it
    matrix_clone = clone_matrix(matrix)
    if matrix_clone.invert():  # invert() modifies the matrix in place and returns True/False
        ROTATIONS_INVERT[key] = matrix_clone
    else:
        print(f"Matrix inversion failed for {key}")

# Set rendering parameters
def set_render_options(render_time):
    opts = lux.getRenderOptions()
    opts.setMaxTimeRendering(render_time)
    opts.setAddToQueue(True)
    return opts

# Apply transformation on a node
def apply_transform(node, transform_matrix):
    """Applies a transform to a given node."""
    node.applyTransform(transform_matrix)

# Extract the non-ground plane node from the model
def extract_non_ground_plane_node(nodes):
    """Extracts the first non-ground plane node from a list of nodes."""
    for node in nodes:
        if node.getName() != "Ground plane":
            return node
    return None

# Render each camera with appropriate rotations
def render_cameras(root, output_path):
    """Renders images for each camera with the necessary model rotations."""
    opts = set_render_options(RENDER_TIME)
    types = (lux.NODE_TYPE_GROUP, lux.NODE_TYPE_OBJECT, lux.NODE_TYPE_MODEL)
    model_node = root.find("", types=types, depth=3)

    non_ground_plane_node = extract_non_ground_plane_node(model_node)
    if not non_ground_plane_node:
        raise ValueError("No valid non-ground plane node found.")

    file_name = non_ground_plane_node.getName()

    # Render each camera with appropriate rotations
    for i in range(4):
        local_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        camera_name = f"{CAMERA_PREFIX} {i + 1}"

        # Apply rotations only when needed
        if i == 2:  # Rotate for Camera 3
            apply_transform(non_ground_plane_node, ROTATIONS["camera3"])

        elif i == 3:  # Rotate for Camera 4
            # Reset Camera 3 rotation
            apply_transform(non_ground_plane_node, ROTATIONS_INVERT["camera3"])
            # Apply Camera 4 rotation
            apply_transform(non_ground_plane_node, ROTATIONS["camera4"])

        lux.setCamera(camera_name)
        lux.renderImage(
            f"{output_path}{file_name}-{local_time}-{i + 1}.jpg",
            width=RENDER_WIDTH,
            height=RENDER_HEIGHT,
            opts=opts
        )

    # Reset the model's rotation and camera
    apply_transform(non_ground_plane_node, ROTATIONS_INVERT["camera4"])
    lux.setCamera(f"{CAMERA_PREFIX} 1")
    lux.processQueue(root, OUTPUT_PATH)

# Execute the rendering process
root = lux.getSceneTree()
render_cameras(root, OUTPUT_PATH)
