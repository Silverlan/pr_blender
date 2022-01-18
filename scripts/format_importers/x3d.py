import sys;
import bpy;
bpy.ops.import_scene.x3d(
	filepath=sys.argv[0],
	filter_glob='*.x3d;*.wrl',
	axis_forward='Z',
	axis_up='Y'
)