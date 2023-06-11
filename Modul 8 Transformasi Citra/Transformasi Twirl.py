import matplotlib.pyplot as plt
from skimage import data
import cv2
from skimage.transform import swirl
image = cv2.imread('Saitama.jpg')
# Ubah format gambar dari BGR (default OpenCV) ke RGB (default matplotlib)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Lakukan proses swirl pada gambar
swirled = swirl(image_rgb, rotation=0, strength=10, radius=120)

fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3), sharex=True, sharey=True)
ax0.imshow(image_rgb)
ax0.axis('off')
ax1.imshow(swirled)
ax1.axis('off')
plt.show()