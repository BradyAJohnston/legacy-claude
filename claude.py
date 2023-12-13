import bpy
from bpy.app.handlers import persistent
from .toy_model import timestep

@persistent
def _timestep(scene):
    timestep()

