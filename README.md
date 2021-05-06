# Interpolation for Color Demosaicing of Digital Cameras #


## Setup Instructions for Python3 and Dependencies

1.	This project was completed in Python 3. As a reference, the version of Python used to make this project was Python 3.8.5. To download Python 3 follow this link. Make sure to add Python to PATH. https://www.python.org/downloads/ 

2.	PIP is a very common package-management system for Python. PIP will need to be installed to download the libraries necessary to run the Project. If Python 3 was installed from the link above, PIP is already installed. Otherwise install from here: https://pip.pypa.io/en/stable/installing/ 

3.	Either use GitHub to clone the repository on your machine or download the zip folder that was included in the submission folder in Avenue called Project 1. To learn how to quickly clone the project from GitHub, follow the instructions here: https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository 

4.	Once the repository is cloned or downloaded, open a Command Line or Terminal and navigate to where you cloned or downloaded the folder to. Once you are in the Project 1 Folder, proceed to the next step. To learn how to navigate in Terminal or Command Line, visit the links below. Alternatively, open the Project 1 Folder with your preferred Integrated Development Environment (IDE) such as PyCharm, or Visual Studio Code. 
CMD:https://www.howtogeek.com/659411/how-to-change-directories-in-command-prompt-on-windows-10/    Terminal:https://www.macworld.com/article/2042378/master-the-command-line-navigating-files-and-folders.html 

5.	There were two libraries utilized in this Project. 

      `NumPy==1.20.1`
      
      `Pillow==8.1.0`
        
      These dependencies can be installed in 3 different ways:
      
      1. A requirements.txt file was created which holds the dependencies for this project. In the Command Line or Terminal, while in the Project 1 folder, run the following command shown below:  

          `pip3 install -r requirements.txt`
      
      2. Or, instead of installing from the requirements.txt file, install both packages manually. In the Command Line or Terminal, while in the Project 1 folder, run the following commands shown below:  

          `pip3 install numpy==1.20.1`

          `pip3 install pillow==8.1.0`

          `Note: If you have multiple versions of python and multiple packages at different paths use:`
          
            `python3 -mpip install numpy==1.20.1`

            `python3 -mpip install pillow==8.1.0`
      
      3. Or, use your IDE Package Manager to install these packages. By going in to the IDE Settings, there is a Packages section to search and install them. Use Google to find how to do this for your preferred IDE.

Now that Python3 and the dependencies are installed, the code is now ready to run. Continue to the next section to learn how to use the Program. 

 
## Repository Structure Breakdown

This section is a breakdown of the Repository for a new user of the program to understand and navigate through it. The next section will discuss how to run the actual program. The Project 1 Folder will have the structure as shown in the picture below.

![image](https://user-images.githubusercontent.com/64797254/107813849-f6be5200-6d3e-11eb-8a51-4e0fef3efcba.png)

 
Below is a quick breakdown of what each folder is used for.
Project 1
  - `src`
    - This folder is where all the source code is written for this Project. There are in total 5 files written in this as shown below. A brief breakdown of the purpose of each file is included below as well. 
    
      ![image](https://user-images.githubusercontent.com/64797254/107813942-1b1a2e80-6d3f-11eb-8b61-c15cd9e04cc0.png)
 
    
    
      - `main.py`
        - This file is the starting point of the entire program. This is the only function that has to be run to use the Project. The main function uses an image specified from the images folder below as an input. This will later be talked about in more detail, in the next section. 
      - `bayer.py`
        - This file is the camera simulation program which generates the Bayer CFA Pattern Mosaic Data. It generates 4 images used as data for the interpolation part of the program. The 4 images are the Red Bayer Patter, Blue Bayer Pattern, Green Bayer Pattern  and the Combined Bayer Pattern of the RGB layers. 
      - `bicubic.py`
        - This file is a helper function for the interpolation algorithm. It returns the result of a bicubic interpolation. The input is 16 Color Intensity values along with the corresponding (x,y) values of the interested pixel. 
      - `interpolation.py`
        - This is where the interpolation algorithm is written. The red, blue, green Bayer Pattern Mosaic data are passed to this function as an input. The return is the individual Red, Blue Green Interpolated Layers and also the full Reconstructed colored RGB image.
      - `mse.py`
        - This is where the Mean Squared Error of the original and reconstructed images is calculated. The input is the two images, and the output is the numerical value. 

  - `images`
    - This folder is where all the original RGB images are kept, which provide the input to the program. There are some test images inside already as shown below. Add any additional input test images into this folder. 
      
      ![image](https://user-images.githubusercontent.com/64797254/107818316-6c2d2100-6d45-11eb-8a92-817061e0e7c5.png)

  - `bayer_cfa_images`
	  - This folder is the output of `bayer.py` which is the camera simulation program which generates the Bayer CFA Pattern Mosaic Data
    - As the image below shows the RGB Bayer Patterns are created along with the combined Bayer Pattern Image. 
      
      ![image](https://user-images.githubusercontent.com/64797254/107814718-59fcb400-6d40-11eb-95ba-950993ce0530.png)

  - `interpolated_images`
    - This folder is the output of `interpolation.py`, which is where interpolation algorithm is written to reconstruct the image using the Bayer Mosaic data. As shown below in the image, 4 images are returned. The red, blue and green interpolated images and also the final reconstructed image from the bayer mosaic data. 
      
      ![image](https://user-images.githubusercontent.com/64797254/107814756-6719a300-6d40-11eb-9fdb-a660a2432f7d.png)

  - `venv` 
      - Virtual Environment Configuration. Just Ignore this folder.  
    
    
    
## How to Run the Program

All the user needs to do is specify the input image, and run `main.py`. Simple instructions on how to do this are given below:

1.	By default, the program assumes the input image is called “`input.png`” and that it is stored in the `images` folder. The input image can be provided in two easy ways:

      1. Re-name the image you want to input to “`input.png`” and make sure it is stored in the `images` folder. 

      2. Or, open `main.py` and edit `line 8` as shown below. Make sure the input images you want to test are all stored in the `image` folder. Then simply just change the name to whatever the image is called in the string for the `original_img_url` variable. 
      
          `original_img_url = "../images/input.png"`

 
2.	To run the program now, either run `main.py` in your IDE or navigate to the `src` folder in Command Line or Terminal, and execute the following command: `python3 main.py`

    While the program is executing, things will be printed to console to indicate the status of what is happening. You should see the following text in the Python Console or Terminal/Command Line:
    
    ![image](https://user-images.githubusercontent.com/64797254/107819924-f1b1d080-6d47-11eb-88e7-a3f9fdef0052.png)
 

3.	The reconstructed interpolated image will automatically open. To view the Bayer CFA Pattern Mosaic Data, open the `bayer_cfa_images` folder to view those results. To view the interpolated red, green and blue layers of the Bayer data, open the `interpolated_images` folder to view those results. Refer back to the Repository Break Down Section if more detail is needed on how the Program works. 

4.	The Mean Squared Error will be printed in the console as shown in the screenshot above. 

5.	Repeat from Step 1 with a new Input Image. Enjoy!

Note: If any errors come up about modules not being imported, please refer back to the Setup section and install all packages correctly. 



# Example

### Original Image
![image](https://user-images.githubusercontent.com/64797254/107816823-50c11680-6d43-11eb-8a0a-7d61d6f21863.png)

### Red Bayer CFA Mosaic Pattern
![image](https://user-images.githubusercontent.com/64797254/107817029-89f98680-6d43-11eb-963d-5dd4a9c997eb.png)

### Blue Bayer CFA Mosaic Pattern
![image](https://user-images.githubusercontent.com/64797254/107817255-e2308880-6d43-11eb-9d5d-54e5b3bfe632.png)

### Green Bayer CFA Mosaic Pattern
![image](https://user-images.githubusercontent.com/64797254/107817298-ed83b400-6d43-11eb-9a4a-1920c140acca.png)

### Combined RGB Bayer CFA Mosaic Pattern
![image](https://user-images.githubusercontent.com/64797254/107817321-f8d6df80-6d43-11eb-8ea4-59fe00138544.png)

### Red Interpolated Mosaic Layer
![image](https://user-images.githubusercontent.com/64797254/107817356-05f3ce80-6d44-11eb-9a87-57cfc8090b89.png)

### Blue Interpolated Mosaic Layer
![image](https://user-images.githubusercontent.com/64797254/107817401-1146fa00-6d44-11eb-85ea-4574a43fddd1.png)

### Green Interpolated Mosaic Layer
![image](https://user-images.githubusercontent.com/64797254/107817408-13a95400-6d44-11eb-88dd-d6c5277db5bd.png)

### Final Interpolated Reconstructed RGB Image
![image](https://user-images.githubusercontent.com/64797254/107817419-160bae00-6d44-11eb-875f-44793afd7239.png)
