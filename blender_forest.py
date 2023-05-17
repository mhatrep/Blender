import bpy
import random
import bmesh

# Define the sizes
ground_size = 10
tree_height = 3
tree_variation = 1.5
number_of_trees = 500

# Colors for the trees
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1)]

# Create the ground plane
bpy.ops.mesh.primitive_plane_add(size=ground_size)
ground = bpy.context.object

# Create a new material for the ground
bpy.ops.material.new()
ground_material = bpy.data.materials[-1]  # Get the last created material
ground_material.name = "Ground"  # Rename the material
ground_material.use_nodes = True
nodes = ground_material.node_tree.nodes

# Set color to green
color_node = nodes.new(type='ShaderNodeRGB')
color_node.outputs['Color'].default_value = (0, 1, 0, 1)
bsdf_node = nodes.get('Principled BSDF')
material_output_node = nodes.get('Material Output')
ground_material.node_tree.links.new(bsdf_node.inputs['Base Color'], color_node.outputs['Color'])

# Assign the material to the ground
ground.data.materials.append(ground_material)

# Function to create a low-poly tree
def create_tree(location, color):
    mesh = bpy.data.meshes.new(name="TreeMesh")
    obj = bpy.data.objects.new("Tree", mesh)
    bpy.context.collection.objects.link(obj)
    bm = bmesh.new()

    # Generate a low-poly tree
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=True, segments=4, radius1=0.1, radius2=0, depth=tree_height + random.uniform(-tree_variation, tree_variation))

    bm.to_mesh(mesh)
    bm.free()

    # Set the tree's location
    obj.location = location

    # Create a new material for the tree
    bpy.ops.material.new()
    tree_material = bpy.data.materials[-1]  # Get the last created material
    tree_material.name = "TreeMat"  # Rename the material
    tree_material.use_nodes = True
    nodes = tree_material.node_tree.nodes

    # Set the color of the tree
    color_node = nodes.new(type='ShaderNodeRGB')
    color_node.outputs['Color'].default_value = color + (1,)
    bsdf_node = nodes.get('Principled BSDF')
    material_output_node = nodes.get('Material Output')
    tree_material.node_tree.links.new(bsdf_node.inputs['Base Color'], color_node.outputs['Color'])

    # Assign the material to the tree
    obj.data.materials.append(tree_material)

# Create the trees
for _ in range(number_of_trees):
    tree_location = (random.uniform(-ground_size/2, ground_size/2), random.uniform(-ground_size/2, ground_size/2), 0)
    tree_color = random.choice(colors)
    create_tree(tree_location, tree_color)
