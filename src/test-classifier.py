# Import the required modules
from skimage.transform import pyramid_gaussian
from skimage.io import imread
from skimage.feature import hog
from sklearn.externals import joblib
import glob
import os
import cv2
import argparse as ap
from nms import nms
from config import *

import ipdb;

if __name__ == "__main__":
    # Parse the command line arguments
    parser = ap.ArgumentParser()
    parser.add_argument('-p', "--postest", help="Path to the positive test directory", required=True)
    parser.add_argument('-n', "--negtest", help="Path to the negative test directory", required=True)
    args = vars(parser.parse_args())

    pos_test_path =  args["postest"]
    neg_test_path = args["negtest"]

    # Load the classifier
    clf = joblib.load(model_path)

    # List to store results
    detections = []
    pos_results = []
    neg_results = []


    for test_path in glob.glob(os.path.join(pos_test_path,"*")):
        im = imread(test_path, as_grey=True)
        fd = hog(im, orientations, pixels_per_cell, cells_per_block, block_norm, visualize, transform_sqrt, feature_vector)
        fd = fd.reshape(1,-1)
        pred = clf.predict(fd)
        pos_results.append((test_path, pred[0], clf.decision_function(fd)[0], ))
        if pred == 1:
            detections.append((test_path, clf.decision_function(fd)[0], ))

    
    for test_path in glob.glob(os.path.join(neg_test_path,"*")):
        im = imread(test_path, as_grey=True)
        fd = hog(im, orientations, pixels_per_cell, cells_per_block, block_norm, visualize, transform_sqrt, feature_vector)
        fd = fd.reshape(1,-1)
        pred = clf.predict(fd)
        neg_results.append((test_path, pred[0], clf.decision_function(fd)[0], ))
        if pred == 1:
            detections.append((test_path, clf.decision_function(fd)[0], ))

    print 'test results for positive pictures, format (file_name, detected, confidence score): '
    for record in pos_results:
        print record
    print '\n'
    print 'test results for negative pictures, format (file_name, detected, confidence score): '
    for record in neg_results:
        print record
    print '\n'
    print 'all detected pictures, format (file_name, confidence score): '
    for record in detections:
        print record
