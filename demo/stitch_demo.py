## Stitches demo and ground truth amodal masks together
import cv2 as cv
import os
import numpy as np

def main():

    inputAmodalFolder = "/home/winston/projects/AmodalSegmentation/data/datasets/coco/val2017"
    inputVisibleFolder = "/home/winston/projects/AmodalSegmentation/data/datasets/coco/val2017"
    inputDemoFolder = "/home/winston/projects/AmodalSegmentation/data/asbu_viz/coco_asbu_demo_test_asbu_amodal/demo"
    outputFolder = "/home/winston/projects/AmodalSegmentation/data/asbu_viz/coco_asbu_demo_test_asbu_amodal/stitched"

    files = os.listdir(inputDemoFolder)
    files.sort()

    ## Goes through the files
    for file in files:

        ## Reads images, stitches and saves them
        ## Format: Visible | Prediction | Amodal
        visible = cv.imread(os.path.join(inputVisibleFolder, file))
        demo = cv.imread(os.path.join(inputDemoFolder, file))
        amodal = cv.imread(os.path.join(inputAmodalFolder, file))
        stitched = np.concatenate([visible, demo, amodal], axis=1)

        cv.imwrite(os.path.join(outputFolder, file), stitched)

def stitchAll():
    
    inputFolder = "/home/winston/projects/AmodalSegmentation/data/asbu_viz/coco_asbu_demo_test_asbu/stitched"
    outputFolder = "/home/winston/projects/AmodalSegmentation/data/asbu_viz/coco_asbu_demo_test_asbu"

    files = os.listdir(inputFolder)
    files.sort()

    ## Goes through the files
    switch = False
    for file in files:

        if (not switch):
            fullStitch = cv.imread(os.path.join(inputFolder, file))
            switch = True

        else:
            newImage = cv.imread(os.path.join(inputFolder, file))
            fullStitch = np.concatenate([fullStitch, newImage], axis=0)

    ## Save image
    cv.imwrite(os.path.join(outputFolder, "__full_stitched.png"), fullStitch)

main()
stitchAll()
