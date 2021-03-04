import bpy
import glob
import os


def pos(g, nums):
    b = nums[g].split()
    c = []
    for i in b:
        try:
            c.append(float(i))
        except ValueError:
            continue
    return c


bpy.ops.object.delete(use_global=False, confirm=False)

path_to_file = os.path.join('C:\\','Users', 'MAX','Desktop','texel', 'obj', 'maxim.obj')
bpy.ops.import_scene.obj(filepath=path_to_file)

ob = bpy.context.scene.objects["maxim_maxim.011"]      # Get the object
bpy.ops.object.select_all(action='DESELECT') # Deselect all objects
bpy.context.view_layer.objects.active = ob   # Make the cube the active object 
ob.select_set(True)   
bpy.ops.id.get_selected_objects()
bpy.context.scene.arp_smart_sym = False

ing = glob.glob('/Users/MAX/Downloads/squares (*).txt')
p = str(len(ing) - 1)
fp = open('/Users/MAX/Downloads/squares (' + p + ').txt','r')
nums = fp.read().splitlines()



c = pos(0, nums)
print(c[1])
y = float(c[1])
x = float(c[0])
x = (x - 248) * 0.106
y = (490- y) * 0.13

bpy.ops.id.add_marker(body_part ="neck")
bpy.data.objects["neck_loc"].location.z = y - 3
bpy.ops.id.add_marker(body_part ="chin")
bpy.data.objects["chin_loc"].location.z = y - 1.5


c = pos(5, nums)
print(c[1])
y = float(c[1])
x = float(c[0])
x = (x - 248) * 0.106
y = (490 - y) * 0.13

bpy.ops.id.add_marker(body_part ="shoulder")
bpy.data.objects["shoulder_loc"].location.z = y
bpy.data.objects["shoulder_loc"].location.x = x
bpy.data.objects["shoulder_loc_sym"].location.z = y
bpy.data.objects["shoulder_loc_sym"].location.x = x * (-1)

c = pos(9, nums)
print(c[1])
y = float(c[1])
x = float(c[0])
x = (x - 246) * 0.106
y = (490 - y) * 0.13

bpy.ops.id.add_marker(body_part ="hand")
bpy.data.objects["hand_loc"].location.z = y
bpy.data.objects["hand_loc"].location.x = x
bpy.data.objects["hand_loc_sym"].location.z = y
bpy.data.objects["hand_loc_sym"].location.x = x * (-1)

c = pos(11, nums)
print(c[1])
y = float(c[1])
x = float(c[0])
x = (x - 248) * 0.106
y = (490 - y) * 0.13

bpy.ops.id.add_marker(body_part ="root")
bpy.data.objects["root_loc"].location.z = y
#bpy.data.objects["root_loc"].location.x = -1

c = pos(15, nums)
print(c[1])
y = float(c[1])
x = float(c[0])
x = (x - 260) * 0.106
y = (490 - y) * 0.13

bpy.ops.id.add_marker(body_part ="foot")
bpy.data.objects["foot_loc"].location.z = y
bpy.data.objects["foot_loc"].location.x = x
bpy.data.objects["foot_loc_sym"].location.z = y
bpy.data.objects["foot_loc_sym"].location.x = x * (-1)

bpy.context.scene.arp_fingers_to_detect = 'NONE'

bpy.ops.id.go_detect()

bpy.ops.arp.match_to_rig()
bpy.ops.object.posemode_toggle()

ob = bpy.context.scene.objects["maxim_maxim.011"]  
rig = bpy.context.scene.objects["rig"]    # Get the object
bpy.ops.object.select_all(action='DESELECT') # Deselect all objects
bpy.context.view_layer.objects.active = rig   # Make the cube the active object 

rig.select_set(True)
ob.select_set(True)

bpy.ops.arp.bind_to_rig()

bpy.ops.export_scene.obj(filepath="/Users/MAX/Desktop/texel/rig/rigged.obj")