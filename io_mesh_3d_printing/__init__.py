

bl_info = {
    "name": "3D Printer Integration",
    "author": "Aeva Palecek",
    "description": "3D printing for a better world.",
    "category": "Import-Export",
}


from tempfile import mkstemp
from subprocess import Popen
import bpy


class ExportTest(bpy.types.Operator):
    bl_idname = "export_to_printer.stl"
    bl_label = "Export to 3D Printer"
    bl_options = {'PRESET'}

    def execute(self, context):
        #bpy.ops.export_mesh.stl(
        #    filepath="", check_existing=True, filter_glob="*.stl", 
        #    ascii=False, use_mesh_modifiers=True, 
        #    axis_forward='Y', axis_up='Z', global_scale=1)

        export_path = mkstemp(suffix=".stl")[1]
        bpy.ops.export_mesh.stl(filepath=export_path, check_existing=False)
        print("exported temporary stl to {0}".format(export_path))
        proc = Popen(("vpp", export_path))
        return {"FINISHED"}
        
    


def menu_func(self, context):
    self.layout.operator(ExportTest.bl_idname, text="to Printer")

def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_export.append(menu_func)
    
def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_export.remove(menu_func)

if __name__ == "__main__":
    register()
