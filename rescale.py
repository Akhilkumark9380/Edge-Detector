import cv2 as cv

def rescaleFrame(frame, scale=0.5):
    # Images, videos, Live Videos
    width = frame.shape[1] * scale
    height = frame.shape[0] * scale 
    dimension = (int(width),int(height))
    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)

def changeRes(width, height):
    # Live videos 
    capture.set(3,width)
    capture.set(4,height)




