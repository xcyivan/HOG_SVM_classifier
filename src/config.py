'''
Set the config variable.
'''

import ConfigParser as cp
import json

config = cp.RawConfigParser()
config.read('./config.cfg')

min_wdw_sz = json.loads(config.get("hog","min_wdw_sz"))
step_size = json.loads(config.get("hog", "step_size"))
orientations = config.getint("hog", "orientations")
pixels_per_cell = json.loads(config.get("hog", "pixels_per_cell"))
cells_per_block = json.loads(config.get("hog", "cells_per_block"))
block_norm = config.get("hog", "block_norm")
visualize = config.getboolean("hog", "visualize")
transform_sqrt = config.getboolean("hog", "transform_sqrt")
feature_vector = config.getboolean("hog", "feature_vector")
pos_feat_ph = config.get("paths", "pos_feat_ph")
neg_feat_ph = config.get("paths", "neg_feat_ph")
model_path = config.get("paths", "model_path")
threshold = config.getfloat("nms", "threshold")
