# -*- coding: utf-8 -*-

from PIL import Image
import pytesseract
import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, 
	            help="path to input image to be OCR'd")
# helpは引数に何を渡すかを示唆してる
ap.add_argument("-p", "--preprocess", type=str, default="thresh", 
	            help="type of preprocessing to be done")

# print(vars(ap))
"""
ArgumentParser(prog='parse_argTest.py', usage=None, description=None,
 formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error',
  add_help=True)
"""

args = vars(ap.parse_args()) 
"""
varsはap.parse_args()の__dict__ attributeをreturnしてる　→なんの為に？
parse_args()の役割がよくわかってないから、vars()の使い方もわかってない？
"""

# print(args)
"""
usage: parse_argTest.py [-h] -i IMAGE [-p PREPROCESS]
parse_argTest.py: error: the following arguments are required: -i/--image
"""

