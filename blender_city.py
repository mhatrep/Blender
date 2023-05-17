import bpy
import random

# Clear all mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Parameters
city_size = 10
building_min_height = 1.0
building_max_height = 10.0

# Function to create a random color material
def create_random_color_material(name):
    material = bpy.data.materials.new(name=name)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    color = nodes.get('Principled BSDF')
    if color:
        color.inputs[0].default_value = (random.random(), random.random(), random.random(), 1)

    return material

# Create buildings
for i in range(city_size):
    for j in range(city_size):
        building_height = random.uniform(building_min_height, building_max_height)
        
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(i*2, j*2, building_height/2))
        
        building = bpy.context.object
        building.dimensions.z = building_height

        # Assign random color to the building
        material = create_random_color_material(f"Material_{i}_{j}")
        if building.data.materials:
            # Assign to first material slot
            building.data.materials[0] = material
        else:
            # No slots
            building.data.materials.append(material)
