import cv2
import numpy as np
from google.colab.patches import cv2_imshow

def add_random_noise(image, intensity=25):
    noisy_image = image.copy()
    noise = np.random.randint(-intensity, intensity + 1, noisy_image.shape)
    noisy_image = np.clip(noisy_image + noise, 0, 255).astype(np.uint8)
    return noisy_image

original_image = cv2.imread('testimg.jpeg')

if original_image is None:
    raise Exception("Image not loaded properly. Check the file path.")

noisy_image = add_random_noise(original_image, intensity=25)

cv2_imshow(original_image)
cv2_imshow(noisy_image)
