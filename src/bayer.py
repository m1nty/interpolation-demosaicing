from PIL import Image
import numpy as np

def bayer(img_url):

    #Read Image
    original = np.asarray(Image.open(img_url))
    #Dimensions of Image
    height, width, _ = original.shape
    print("Picture Resolution is ", width, "x", height,"\n")

    print("Generating Bayer CFA Pattern Mosaic Data...")
    #De-Bayering Storage
    bayer_red = np.zeros((height,width, 3), dtype=np.uint8)
    bayer_blue = np.zeros((height,width, 3), dtype=np.uint8)
    bayer_green = np.zeros((height,width, 3), dtype=np.uint8)
    bayer_green1 = np.zeros((height,width, 3), dtype=np.uint8)
    bayer_green2 = np.zeros((height,width, 3), dtype=np.uint8)
    bayer_green = np.zeros((height,width, 3), dtype=np.uint8)

    #De-Bayered Image Compressed
    bayer_compressed =  np.zeros((height,width, 3), dtype=np.uint8)


    #Save Red Bayer Image
    bayer_red[::2, ::2, 0] = original[::2, ::2, 0]
    img_red = Image.fromarray(bayer_red, "RGB")
    img_red.save("../bayer_cfa_images/red_bayer.png")


    #Save Blue Bayer Image
    bayer_blue[1::2, 1::2, 2] = original[1::2, 1::2, 2]
    img_blue = Image.fromarray(bayer_blue, "RGB")
    img_blue.save("../bayer_cfa_images/blue_bayer.png")


    #Save Green Bayer Image
    #Alternating Pattern #1
    bayer_green1[::2, 1::2, 1] = original[::2, 1::2, 1]
    img_green1 = Image.fromarray(bayer_green1, "RGB")
    #Alternating Pattern #2
    bayer_green2[1::2, ::2, 1] = original[1::2, ::2, 1]
    img_green2 = Image.fromarray(bayer_green2, "RGB")
    #Combined Green Pattern
    bayer_green[1::2, ::2, 1] = original[1::2, ::2, 1]
    bayer_green[::2, 1::2, 1] = original[::2, 1::2, 1]
    img_green = Image.fromarray(bayer_green, "RGB")
    img_green.save("../bayer_cfa_images/green_bayer.png")


    #Bayer CFA RGB Compressed
    bayer_compressed[::2, ::2, 0] = bayer_red[::2, ::2, 0]
    bayer_compressed[1::2, 1::2, 2] = bayer_blue[1::2, 1::2, 2]
    bayer_compressed[::2, 1::2, 1] = bayer_green1[::2, 1::2, 1]
    bayer_compressed[1::2, ::2, 1] = bayer_green2[1::2, ::2, 1]
    Image.fromarray(bayer_compressed, "RGB").save("../bayer_cfa_images/compressed_bayer.png")

    return img_red, img_green1, img_green2, img_blue

