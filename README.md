# IARacing-Autocar
ESAIP Engineering School Applicative Project with SIGMA Nantes for IA-Racing Competition, with donkeycar framework


#This project is an Open-Source modification on the donkeycar project!
# What type of IA model file is used?
When you generate an IA (model) with donkeycar, three files are created:
        - mypilot.png
        - mypilot.tflite
        - mypilot.h5

tflite and H5 are both model files, but H5is a lot more heavy than tflite. This can create, with h5, freeze during use, latency or others mistakes...

We strongly advise to use .tflite format!

# How many image do I have to take?
For us the optimum image number is between 10k and 20k, more it's useless and less can create error on the model.

# What type of image processing?
The best is an image processing who modify the current image to a 2 color image with a big contrast, the teams whose cars didn't use this type of image processing were affected by light, people, colors, etc...

# How to implement parts?
A parts is a function that take place on the main loop of the program. All the parts have a specific order of call and its very important!

In the manage.py you define the order of call for all the parts and your custom one.

For example:

        if cfg.TYPE_TRAITEMENT==1:  <== This part is a parameter to activate the image processing, for activate go see myconfig.py
            from donkeycar.parts.AutoCar_traitementcontour import AC_Imagecontour <== Importing the parts from the parts folder
            V.add(AC_Imagecontour(),inputs =['cam/image_array'], outputs=['cam/image_array','imageoriginal'],threaded=False) <== Define the methode, imput, outputs and if its  thraded.
            
            V.add= Vehicule add methode
            AC_Imagecontour() = name of the methode in the AC_Imagecontour.py file
            inputs=['cam/image_array'] = cam/image_array is the current main image displayed in the web viewer and save for the IA generation. in inputs you define all the parameters of run() parts in your parts execept self. 
            outputs=['cam/image_array','imageoriginal'] = it's all the return var from run() parts in your parts. In this case cam/image_array get the modified image and we create a new var imageoriginal who is the initial image without modification.
            threaded = a parts can be threaded for exemple: for specific captors or others, not a good idea for image processing, color detection or others

# Little tips
 - Dont go too fast and make errors, penalties hit hard!
 - Prepare in myconfig.py, parameters for easy modifications on the fly
 - Use a line detector (FC 51 ir sensor for example) to auto correct when line crossing 

# Useful links:
 - Live of the competition :    https://www.youtube.com/watch?v=lWOdJ5ZOY6o
 - Donkeycar doc :              https://docs.donkeycar.com/
 - Donkeycar Discord :          https://discord.com/invite/PN6kFeA

Good Luck and enjoy this project!

For any questions, contact us by email (use school emails)
