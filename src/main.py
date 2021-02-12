from bayer import bayer
from interpolation import interpolation
from mse import mse, mse1
from PIL import Image


#Specify Input Image
original_img_url = "../images/input.png" #Original Input is 1024 x 768 Resolution


#Bayer CFA Patterns Generated from camera simulation function to produce Bayer Mosaic data
#Bayer CFA Mosaic Data saved in folder ./bayer_cfa_images
r_img, g1_img, g2_img, b_img = bayer(original_img_url)

#Color Image reconstructed by Interpolating Bayer CFA Mosaic data.
#Interpolated images saved in folder ./interpolated_images
interpolated_img_url = interpolation(r_img, g1_img, g2_img, b_img)
interpolated_image = Image.open(interpolated_img_url)
interpolated_image.show()

#Calculate MSE between Original Image and Reconstructed Interpolated Image
original_image = Image.open(original_img_url)
# interpolated_image = Image.open("../interpolated_images/test.png")

print("Mean Squared Error  = ", mse(original_image, interpolated_image))
