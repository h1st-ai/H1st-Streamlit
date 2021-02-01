from fastapi.datastructures import UploadFile
import numpy as np
import cv2


def preprocess_drawn_image(file: UploadFile, shape: tuple=(28, 28)):
    # Load image
    npimg = np.fromfile(file.file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_GRAYSCALE)

    # Resize image
    img = cv2.resize(img, shape)

    # Reshape image
    input_img = np.expand_dims(np.expand_dims(img, axis=0), axis=3)

    return input_img