import sys

sys.path.append(r"C:\repos\po3\.env\Lib\site-packages")

import po3
import bpy
import numpy as np


for mesh in bpy.data.meshes:
    vertex_positions = np.zeros(3 * len(mesh.vertices), dtype=np.float32)
    mesh.vertices.foreach_get('co', vertex_positions)
    vertex_positions = vertex_positions.reshape((-1, 3))

    po3.axpy(2, vertex_positions)

    print(vertex_positions)

    