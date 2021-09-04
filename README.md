# Edge-Detector
Detecting Edges of an Image using Python openCV.
---
# Why Edge Detection
- Edges are defined as “ Sudden and Significant changes in the intensity” of an image. These changes happen between the boundaries of object in  an image.
- One can understand the shape of the objects in the image only when  the edges are detected . So , ideally to understand 
     an object and its shape it becomes inevitable for someone to detect the edges.
- There are many technical issues and challenges mapped to the segmentation , registration and object identification 
    techniques. Edges prove to be efficient with these above techniques at the fundamental levels.
 ---
# Steps in Edge Detection
- There are three steps followed in edge detection they are :
    - Image smoothening 
    - Edge point detection   and
    - Edge localization 
 ---
# Technique Used
- CANNY EDGE DETECTION :
   Canny edge detection technique, not just a plane edge detection technique. It has an additional feature where it suppresses the noise while detecting  the edges flawlessly.
- Steps used in it:
  - Conversion to grayscale
  - Gaussian Blur
  - Intensity Gradient Calculation
  - Non_Maximum suppression
  - Thresholding
  - Edge Tracking
  - Final cleansing
 ---
# Requirement of Rescale 
- for shaping the image to fixed dimensions
---
# How to Run
- Install Python.
- Install python openCv module using command "pip install opencv-python".
- run the python file in any python code editor.
# Applications
- MRI Scanning
- Satellite Image
- Finger Print
