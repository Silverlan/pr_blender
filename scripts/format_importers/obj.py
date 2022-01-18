import sys;
import bpy;
bpy.ops.import_scene.obj(
	filepath=sys.argv[0],
	filter_glob='*.obj;*.mtl',
	use_edges=True,
	use_smooth_groups=True,
	use_split_objects=True,
	use_split_groups=False,
	use_groups_as_vgroups=False,
	use_image_search=True,
	split_mode='ON',
	global_clamp_size=0.0,
	axis_forward='-Z',
	axis_up='Y'
)