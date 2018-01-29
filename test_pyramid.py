# import library
from img_lib_afif.object_detection.helpers import pyramid
import argparse
import cv2

# konstruksi argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke gambar")
ap.add_argument("-s", "--scale", type=float, default=1.5, help="faktor scale")
args = vars(ap.parse_args())

# load citra
image = cv2.imread(args['image'])

# loop pada semua layer
for (i, layer) in enumerate(pyramid(image, scale=args['scale'])):
	cv2.imshow("Layer {}".format(i + 1), layer)
	cv2.waitKey(0)