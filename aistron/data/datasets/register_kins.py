'''
KITTI INStance dataset (KINS)
register kins dataset as a coco-like instance segmentation dataset
we just say kins without instance since the word instance is inside kins

'''

import os
from os.path import join
from detectron2.data.datasets import register_coco_instances


KINS2020_CATEGORIES = [
    {"color": [220, 20, 60], "isthing": 1, 'supercategory': 'Living Thing', 'id': 1, 'name': 'cyclist'}, 
    {"color": [119, 11, 32], "isthing": 1, 'supercategory': 'Living Thing', 'id': 2, 'name': 'pedestrian'}, 
    {"color": [0, 0, 142],   "isthing": 1, 'supercategory': 'Living Thing', 'id': 3, 'name': 'rider'}, 
    {"color": [0, 0, 230],   "isthing": 1, 'supercategory': 'vehicles',     'id': 4, 'name': 'car'}, 
    {"color": [106, 0, 228], "isthing": 1, 'supercategory': 'vehicles',     'id': 5, 'name': 'tram'}, 
    {"color": [0, 60, 100],  "isthing": 1, 'supercategory': 'vehicles',     'id': 6, 'name': 'truck'}, 
    {"color": [0, 80, 100],  "isthing": 1, 'supercategory': 'vehicles',     'id': 7, 'name': 'van'}, 
    {"color": [255, 255, 0], "isthing": 1, 'supercategory': 'vehicles',     'id': 8, 'name': 'misc'}
]


KINS_CATEGORIES = [
    {"color": [220, 20, 60], "isthing": 1, 'supercategory': 'Living Thing', 'id': 1, 'name': 'cyclist'}, 
    {"color": [119, 11, 32], "isthing": 1, 'supercategory': 'Living Thing', 'id': 2, 'name': 'pedestrian'}, 
    {"color": [0, 0, 142],   "isthing": 1, 'supercategory': 'vehicles', 'id': 4, 'name': 'car'}, 
    {"color": [0, 0, 230],   "isthing": 1, 'supercategory': 'vehicles', 'id': 5, 'name': 'tram'}, 
    {"color": [106, 0, 228], "isthing": 1, 'supercategory': 'vehicles', 'id': 6, 'name': 'truck'}, 
    {"color": [0, 60, 100],  "isthing": 1, 'supercategory': 'vehicles', 'id': 7, 'name': 'van'}, 
    {"color": [0, 80, 100],  "isthing": 1, 'supercategory': 'vehicles', 'id': 8, 'name': 'misc'}
]



def _get_kins_instances_meta(cat_list):
    thing_ids = [k["id"] for k in cat_list if k["isthing"] == 1]
    thing_colors = [k["color"] for k in cat_list if k["isthing"] == 1]
    # assert len(thing_ids) == 7, len(thing_ids)
    # Mapping from the incontiguous category id to an id in [0, 6]
    thing_dataset_id_to_contiguous_id = {k: i for i, k in enumerate(thing_ids)}
    thing_classes = [k["name"] for k in cat_list if k["isthing"] == 1]
    ret = {
        "thing_dataset_id_to_contiguous_id": thing_dataset_id_to_contiguous_id,
        "thing_classes": thing_classes,
        "thing_colors": thing_colors,
    }
    return ret


def register_kins(root):
    register_coco_instances("kins_train", _get_kins_instances_meta(KINS_CATEGORIES),
        join(root, "KINS/annotations/instances_train2017.json"),
        join(root, "KINS/train2017")
    )

    register_coco_instances("kins_val", _get_kins_instances_meta(KINS_CATEGORIES),
        join(root, "KINS/annotations/instances_val2017.json"),
        join(root, "KINS/val2017")
    )

def register_kins2020(root):
    register_coco_instances("kins2020_train", _get_kins_instances_meta(KINS2020_CATEGORIES),
        join(root, "KINS/annotations/update_train_2020.json"),
        join(root, "KINS/train2017")
    )

    register_coco_instances("kins2020_val", _get_kins_instances_meta(KINS2020_CATEGORIES),
        join(root, "KINS/annotations/update_test_2020.json"),
        join(root, "KINS/val2017")
    )


_root = os.getenv("AISTRON_DATASETS", "datasets")
register_kins(_root)
register_kins2020(_root)
