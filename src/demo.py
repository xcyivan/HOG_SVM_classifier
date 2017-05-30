#!/usr/bin/python
import os

# Extract the features
pos_path = "../data/train_pos"
neg_path = "../data/train_neg"
os.system("python ./extract-features.py -p {} -n {}".format(pos_path, neg_path))

# Perform training
pos_feat_path =  "../data/features/pos"
neg_feat_path =  "../data/features/neg"
os.system("python ./train-classifier.py -p {} -n {}".format(pos_feat_path, neg_feat_path))

# Perform testing 
pos_test_path = "../data/test_pos"
neg_test_path = "../data/test_neg"
os.system("python ./test-classifier.py -p {} -n {}".format(pos_test_path, neg_test_path))
