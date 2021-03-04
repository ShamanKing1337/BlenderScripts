import bpy
import os

nameFile = input("Name of ply file: ")

bpy.ops.object.delete(use_global=False, confirm=False)
path_to_file = os.path.join('C:\\','Users', 'MAX','Desktop','texel', nameFile + '.ply')
bpy.ops.import_mesh.ply(filepath = path_to_file)
bpy.ops.object.modifier_add(type='DECIMATE')
bpy.context.object.modifiers["Decimate"].ratio = 0.2
bpy.ops.object.modifier_apply (modifier='Decimate')
bpy.ops.transform.resize(value=(0.0289535, 0.0289535, 0.0289535), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.context.object.rotation_euler[0] = 1.5708
bpy.context.object.location[2] = 27


materialP = bpy.data.materials.new(name= "popa")
materialP.use_nodes = True

m_out = materialP.node_tree.nodes.get('Principled BSDF')



vertex = materialP.node_tree.nodes.new("ShaderNodeAttribute")

vertex.attribute_name = "Col"

materialP.node_tree.links.new(vertex.outputs[0], m_out.inputs[0])

bpy.context.object.active_material = materialP

bpy.ops.image.new()


bpy.ops.object.editmode_toggle()
kek = bpy.ops.uv.smart_project()
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.uv.select_all(action='SELECT')




img = materialP.node_tree.nodes.new("ShaderNodeTexImage")

images = bpy.data.images.new("Sprite", width=1024, height=1024)

images.filepath_raw = ("/Users/MAX/Desktop/texel/obj/" + nameFile + ".png")
images.file_format = 'PNG'

img.image = images




            
my_areas = bpy.context.workspace.screens[0].areas
my_shading = 'MATERIAL'  # 'WIREFRAME' 'SOLID' 'MATERIAL' 'RENDERED'


for area in my_areas:
    for space in area.spaces:
        if space.type == 'VIEW_3D':
            space.shading.type = my_shading
            

bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.bake_type = 'DIFFUSE'
bpy.context.scene.render.bake.use_pass_direct = False
bpy.context.scene.render.bake.use_pass_indirect = False
bpy.ops.object.bake(type='DIFFUSE')

materialP.node_tree.links.new(img.outputs[0], m_out.inputs[0])


images.save()


bpy.ops.export_scene.obj(filepath="/Users/MAX/Desktop/texel/obj/" + nameFile + ".obj")