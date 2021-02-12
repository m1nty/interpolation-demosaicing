import numpy as np

def mse(original_image, interpolated_image):
    original_arr = np.asarray(original_image)
    interpolated_arr = np.asarray(interpolated_image)
    height, width = len(original_arr), len(original_arr[0])
    r_mse, b_mse, g_mse = 0, 0, 0

    for row in range(height):
        for col in range(width):
            r_mse += pow(float(original_arr[row,col,0]) - float(interpolated_arr[row,col,0]),2)
            b_mse += pow(float(original_arr[row, col, 2]) - float(interpolated_arr[row, col, 2]), 2)
            g_mse += pow(float(original_arr[row, col, 1]) - float(interpolated_arr[row, col, 1]), 2)
    r_mse/=height*width
    b_mse/=height*width
    g_mse/=height*width

    return (r_mse+b_mse+g_mse)/3

def mse1(original_image, interpolated_image):
    original_arr = np.asarray(original_image)
    interpolated_arr = np.asarray(interpolated_image)
    Y = np.square(np.subtract(original_arr,interpolated_arr)).mean()
    return Y