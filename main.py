import sys
sys.path.append('.')

import os
import numpy as np
import base64
import io

from PIL import Image
from flask import Flask, request, jsonify
from facesdk import getMachineCode
from facesdk import setActivation
from facesdk import faceDetection
from facesdk import initSDK
from facebox import FaceBox

livenessThreshold = 0.7
yawThreshold = 10
pitchThreshold = 10
rollThreshold = 10
occlusionThreshold = 0.9
eyeClosureThreshold = 0.8
mouthOpeningThreshold = 0.5
borderRate = 0.05
smallFaceThreshold = 100
lowQualityThreshold = 0.3
hightQualityThreshold = 0.7
luminanceDarkThreshold = 50
luminanceLightThreshold = 200

maxFaceCount = 10

licensePath = "license.txt"
license = ""

machineCode = getMachineCode()
print("machineCode: ", machineCode.decode('utf-8'))

try:
    with open(licensePath, 'r') as file:
        license = file.read()
except IOError as exc:
    print("failed to open license.txt: ", exc.errno)
print("license: ", license)
