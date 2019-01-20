import bpy
def create_group(group_name):
    if group_name in bpy.data.groups:
        group=bpy.data.groups[group_name]
    else:
        group= bpy.data.groups.new(group_name)
    return group
def create_and_link_cross(group):
    bpy.ops.mesh.primitive_cube_add(location=(0,0,1))
    bpy.ops.mesh.primitive_cube_add(location=(0,0,5))
    bpy.ops.mesh.primitive_cube_add(location=(0,-2,3))
    bpy.ops.mesh.primitive_cube_add(location=(0,2,3))
    bpy.ops.mesh.primitive_cube_add(location=(2,0,3))
    bpy.ops.mesh.primitive_cube_add(location=(-2,0,3))
    bpy.ops.mesh.primitive_cube_add(location=(0,0,3))
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.join()
    group.objects.link(bpy.context.object)
#bpy.ops.transform.translate(value=(1, 1, 1))
    bpy.ops.transform.resize(value=(1,1,1))
def f1(i):
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.resize(value=(1/(5**i),1/(5**i),1/(5**i)))
    bpy.ops.transform.translate(value=(cross.dimensions[0]*-1,cross.dimensions[1]*2,cross.dimensions[2]*0))
def f2():
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value=(cross.dimensions[0]*1,cross.dimensions[1]*2 ,cross.dimensions[2]*0))
def f3():
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value=(cross.dimensions[0]*2,cross.dimensions[1]*1 ,cross.dimensions[2]*0))
def f4():
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value=(cross.dimensions[0]*2,cross.dimensions[1]*-1 ,cross.dimensions[2]*0))
def f5():
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value=(cross.dimensions[0]*1,cross.dimensions[1]*-2 ,cross.dimensions[2]*0))
def f6():
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value=(cross.dimensions[0]*-1,cross.dimensions[1]*-2 ,cross.dimensions[2]*0))
def f7():
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value=(cross.dimensions[0]*-2,cross.dimensions[1]*-1 ,cross.dimensions[2]*0))
def f8():
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value=(cross.dimensions[0]*-2,cross.dimensions[1]*1 ,cross.dimensions[2]*0))
def duplicate(i):
    bpy.ops.object.select_all(action='TOGGLE')
    cross.select = True
    f1(i)
    f2()
    f3()
    f3()
    f5()
    f5()
    f7()
    f8()
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.join()
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.remove_doubles()
    bpy.ops.object.editmode_toggle()
group_name = "chess"
group = create_group(group_name)
create_and_link_cross(group)
cross = bpy.context.active_object
#f1(1)
duplicate(1)
#cross = group.objects[0]
#f2()
#cross = group.objects[0]
#f1(1)
#duplicate(1)
#cross = group.objects[0]
#duplicate(1)
