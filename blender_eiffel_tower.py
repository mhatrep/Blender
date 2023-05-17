import bpy
import math

def create_eiffel_tower(location=(0, 0, 0)):
    # Define the base of the tower
    bpy.ops.mesh.primitive_cone_add(vertices=4, radius1=8, depth=10, location=location)

    base = bpy.context.object

    # Create the middle part of the tower
    bpy.ops.mesh.primitive_cone_add(vertices=4, radius1=6, depth=20, location=(location[0], location[1], location[2] + 10))
    middle = bpy.context.object

    # Create the top part of the tower
    bpy.ops.mesh.primitive_cone_add(vertices=4, radius1=4, depth=30, location=(location[0], location[1], location[2] + 25))
    top = bpy.context.object

    # Join all parts together
    bpy.ops.object.select_all(action='DESELECT')
    base.select_set(True)
    middle.select_set(True)
    top.select_set(True)
    bpy.context.view_layer.objects.active = base
    bpy.ops.object.join()

if __name__ == "__main__":
    create_eiffel_tower()
