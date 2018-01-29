import imutils

def pyramid(image, scale=1.5, minSize=(30, 30)):
	# yield gambar asli
	yield image

	# looping
	while True:
		# hitung dimensi baru dan resize
		w = int(image.shape[1] / scale)
		image = imutils.resize(image, width=w)

		# jika hasil resize sudah lebih kecil dari ukuran minimum
		# stop looping
		if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
			break

		# yield image selanjutnya
		yield image

def sliding_window(image, stepSize, windowSize):
	# slide window
	for y in range(0, image.shape[0], stepSize):
		for x in range(0, image.shape[1], stepSize):
			# yield window
			yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])