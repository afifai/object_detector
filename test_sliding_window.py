# import lib
from img_lib_afif.object_detection.helpers import sliding_window, pyramid
import argparse
import time
import cv2

# konstruksi argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke citra")
ap.add_argument("-w", "--width", type=int, help="width citra")
ap.add_argument("-t", "--height", type=int, help="height citra")
ap.add_argument("-s", "--scale", type=float, default=1.5, help="scale")
args = vars(ap.parse_args())

# load input
image = cv2.imread(args['image'])
(winW, winH) = (args['width'], args['height'])

for layer in pyramid(image, scale=args['scale']):
	# loop sliding window pada setiap layer
	for (x, y, window) in sliding_window(layer, stepSize=32, windowSize=(winW, winH)):
		# jika window tidak sesuai dengan ukuran, abaikan
		if window.shape[0] != winH or window.shape[1] != winW:
			continue

		# BAGIAN INI AKAN MEMPROSES SETIAP WINDOW, EKSTRAK HOG
		# METODE MACHINE LEARNING, DLL

		#belum ada metode apapun, gambar windownya
		clone = layer.copy()
		cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
		cv2.imshow("Window", clone)

		#pause
		cv2.waitKey(1)
		time.sleep(0.025)