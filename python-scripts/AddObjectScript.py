bl_info = {
    "name": "Object Adder",
    "author": "Me :)",
    "version": (1, 0),
    "blender": (4, 1, 0),
    "location": "View 3D > Tool",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh"
}

import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Object adder"
    
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        layout.scale_y = 1.4
        row.label(text = "Add an object", icon = "CUBE")
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon="CUBE")
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon = "SPHERE")
        row.operator("object.text_add")
       
       
class PanelA(bpy.types.Panel):
    bl_label = "Scale"
    bl_idname = "PT_Panel_A"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Object adder"
    bl_parent_id = "PT_TestPanel"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        obj = context.object
        layout = self.layout
        row = layout.row()
        row.label(text = "Select an object to scale", icon = "FONT_DATA")
        row.operator("transform.resize")
        row = layout.row()
        col = layout.column()
        col.prop(obj, "scale")
        layout.scale_y = 1.4
        

class PanelB(bpy.types.Panel):
    bl_label = "Specials"
    bl_idname = "PT_Panel_B"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Object adder"
    bl_parent_id = "PT_TestPanel"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text = "Select special operation", icon = "FONT_DATA")
        row.operator("object.shade_smooth")
        row.operator("object.subdivision_set")
        row.operator("object.modifier_add")
        
        
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)
    
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)
    
if __name__ == "__main__":
    register()