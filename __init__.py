# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name"        : "claude",
    "author"      : "Brady Johnston",
    "description" : "climate sims bruh",
    "blender"     : (4, 0, 0),
    "version"     : (0, 0, 1),
    "location"    : "Scene Properties -> Molecular Nodes",
    "warning"     : ""
}

import bpy
from . import claude
from .toy_model import temperature_world

def register():
    bpy.utils.register_class(claude.CL_OT_Initialise)
    bpy.app.handlers.frame_change_pre.append(
        claude._timestep
    )

def unregister():
    bpy.utils.unregister_class(claude.CL_OT_Initialise)
    bpy.app.handlers.frame_change_pre.remove(
        claude._timestep
    )

if __name__ == "__main__":
    register()