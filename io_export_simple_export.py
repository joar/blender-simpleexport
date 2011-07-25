import bpy

from bpy_extras.io_utils import ExportHelper

"""
Add-on info, used by the blender add-on manager
"""

bl_info = {
    "name": "Simple exporter",
    "description": "A very basic export plugin for blender",
    "author": "Joar Wandborg",
    "version": (1,0),
    "blender": (2, 5, 8),
    "api": 31236,
    "location": "View3D > Add > Mesh",
    "warning": '', # used for warning icon and text in addons panel
    "wiki_url": "http://wandborg.se/nothing-here",
    "tracker_url": "http://wandborg.se/nothing-here",
    "category": "Import-Export"}


class SimpleExport(bpy.types.Operator, ExportHelper):
    bl_idname = 'simpleexport.txt'
    bl_label = 'Simple Export (.txt)'

    filename_ext = '.txt'

    def execute(self, context):
        """
        blender callback hook
        """
        self.filepath = bpy.path.ensure_ext(self.filepath, self.filename_ext)
        print(self.filepath)

        exported = self.main(context)
        if exported:
            print('Finished export')

        return {'FINISHED'}

    def invoke(self, context, event):
        """
        blender callback hook
        """
        wm = context.window_manager
        
        # This looks weird, but I guess it makes sense.
        if True:
            # File selector
            wm.fileselect_add(self) # will run self.execute()
            return {'RUNNING_MODAL'}
        elif True:
            # search the enum
            wm.invoke_search_popup(self)
            return {'RUNNING_MODAL'}
        elif False:
            # Redo popup
            return wm.invoke_props_popup(self, event) #
        elif False:
            return self.execute(context)
        
    def main(self, context):
        """
        This is the worker function where we get all the data and output it
        """
        print(context)
        print(self.filepath)

        fd = open(self.filepath, 'w')

        """
        Fetch data from blender, just like you to in 
        the blender "Python Console", and output it to a file
        """
        for i in bpy.data.objects:
            fd.write(
                str(i) + '\n')
        return

"""
blender add-on hook implementations
"""

def menu_func(self, context):
    self.layout.operator(SimpleExport.bl_idname, text = 'Simple export (.txt)')

def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_export.append(menu_func)

def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_export.remove(menu_func)

if __name__ == '__main__':
    register()
