# -*- coding: utf-8 -*-

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, 
	            help="path to input image to be OCR'd")
args = vars(ap.parse_args()) 
