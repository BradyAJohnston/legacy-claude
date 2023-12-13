import bpy
import numpy as np
from . import toy_model
from . import obj
from bpy.app.handlers import persistent
from .toy_model import timestep

@persistent
def _timestep(scene):
    temps = timestep()
    object = bpy.data.objects['a climate']
    obj.add_attribute(object, 'temps', temps, overwrite=True)

# @persistent 
# def _update_temps(scene):
#     global temperature_world
#     obj.add_attribute(object, 'tempse', temperature_world, overwrite=True)


def initialise_object(vals, temps):
    arr = np.zeros((len(vals.reshape(-1)), 3))
    
    object = obj.create_object(
        arr, 
        name = 'a climate'
    )
    obj.add_attribute(object, 'temps', temps)
    # Define the shape of the 3D ndarray

    # Create the 3D ndarray

class CL_OT_Initialise(bpy.types.Operator):
    bl_idname = "cl.initialise"
    bl_label = "test"
    
    def execute(self, context):
        initialise_object(
            vals = toy_model.temperature_world,
            temps = toy_model.temperature_world
            )
        
        return {"FINISHED"}
    