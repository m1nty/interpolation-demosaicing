import numpy as np
from PIL import Image

from bicubic import bicubic

def interpolation(r_img, g1_img, g2_img, b_img):

    print("Interpolating Red Layer...")
    #Red Layer Bayer CFA Pattern Image Interpolation
    original = np.asarray(r_img)
    red_arr = original.copy()
    height, width = len(red_arr), len(red_arr[0])
    padded = np.pad(red_arr[::,::,0], 3,"reflect")

    for row in range(1, height, 2):
        for col in range(1, width, 2):
            sub_block = padded[row:row+7, col:col+7]
            # Centripetal Catmull-Rom Spline Correction
            p = sub_block[::2, ::2].tolist()
            red_arr[row,col,0] = bicubic(p, 0.5, 0.5)
            red_arr[row-1,col,0] = bicubic(p, 0, 0.5)
            red_arr[row,col-1,0] = bicubic(p, 0.5, 0)
    Image.fromarray(red_arr, "RGB").save("../interpolated_images/red_layer.png")

    print("Interpolating Blue Layer...")
    # Blue Layer Bayer CFA Pattern Image Interpolation
    original = np.asarray(b_img)
    blue_arr = original.copy()
    height, width = len(blue_arr), len(blue_arr[0])
    padded = np.pad(blue_arr[::,::,2], 3,"reflect")

    for row in range(0, height-1, 2):
        for col in range(0, width-1, 2):
            sub_block = padded[row:row+7, col:col+7]
            p = sub_block[::2, ::2].tolist()
            # Centripetal Catmull-Rom Spline Correction
            blue_arr[row,col,2] = bicubic(p, 0.5, 0.5)
            blue_arr[row+1,col,2] = bicubic(p, 1, 0.5)
            blue_arr[row,col+1,2] = bicubic(p, 0.5, 1)
    Image.fromarray(blue_arr, "RGB").save("../interpolated_images/blue_layer.png")

    print("Interpolating Green Layer...\n")
    # Green Layer 1 Bayer CFA Pattern Image Interpolation
    original = np.asarray(g1_img)
    green1_arr = original.copy()
    height, width = len(green1_arr), len(green1_arr[0])
    padded = np.pad(green1_arr[::,::,1], 3,"reflect")

    for row in range(1, height, 2):
        for col in range(0, width-1, 2):
            sub_block = padded[row:row+7, col:col+7]
            p = sub_block[::2, ::2].tolist()
            # Centripetal Catmull-Rom Spline Correction
            green1_arr[row,col,1] = bicubic(p, 0.5, 0.5)
            green1_arr[row-1,col,1] = bicubic(p, 0, 0.5)
            green1_arr[row,col+1,1] = bicubic(p, 0.5, 1)

    # Green Layer 2 Bayer CFA Pattern Image Interpolation
    original = np.asarray(g2_img)
    green2_arr = original.copy()
    height, width = len(green2_arr), len(green2_arr[0])
    padded = np.pad(green2_arr[::,::,1], 3,"reflect")

    for row in range(0, height-1, 2):
        for col in range(1, width, 2):
            sub_block = padded[row:row+7, col:col+7]
            p = sub_block[::2, ::2].tolist()
            # Centripetal Catmull-Rom Spline Correction
            green2_arr[row,col,1] = bicubic(p, 0.5, 0.5)
            green2_arr[row+1,col,1] = bicubic(p, 1, 0.5)
            green2_arr[row,col-1,1] = bicubic(p, 0.5, 0)

    #Take average of 2 Green Channels
    final_green_arr = np.zeros_like(green1_arr)
    for row in range(height):
        for col in range(width):
            final_green_arr[row,col,1] = (green1_arr[row,col,1]/2 + green2_arr[row,col,1]/2)
    Image.fromarray((final_green_arr), "RGB").save("../interpolated_images/green_layer.png")

    #Creating Final Interpolated Image
    combined_arr = final_green_arr.copy()
    combined_arr[::, ::, 0] = red_arr[::, ::, 0]
    combined_arr[::, ::, 2] = blue_arr[::, ::, 2]
    interpolated_image = Image.fromarray((combined_arr), "RGB")
    interpolated_image_url = "../interpolated_images/interpolated_image.png"
    interpolated_image.save(interpolated_image_url)

    print("Reconstructed Color Image Successfully.")

    return interpolated_image_url
