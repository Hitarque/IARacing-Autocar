# IARacing-Autocar
Esaip PA with SIGMA Nantes on IA-Racing Competition, on donkeycar framework


#This project is an Open-Source modification on the donkeycar project!
# What type of IA file use?
When you generate an IA with donkeycar, three files are created:
        -mypilot.png
        -mypilot.tflite
        -mypilot.h5
tflite and H5 are both IA, but H5is a lot more heavy than tflite. This can create, with h5, freeze during use, latency or others mistakes...
We advise to use .tflite format!

# How many image i have to take?
For us the optimum image number is between 10k and 20k, more it's useless and less can create error on the IA.

# What type of image processing?
The best is an image processing who modify the current image in a 2 color with a big contrast, the teams who dont use this type of image processing were subjected to light, people, colors, etc...

# How implement parts?
A parts is a function that take place on the main loop of the program. All the parts have a specific order of call and its very important!

In the manage.py you define the order of call for all the parts and you'r custom one.
for exemple:

        if cfg.TYPE_TRAITEMENT==1:  <== This part is a parameter to activate the image processing, for activate go see myconfig.py
            from donkeycar.parts.AutoCar_traitementcontour import AC_Imagecontour <== Importing the parts from the parts folder
            V.add(AC_Imagecontour(),inputs =['cam/image_array'], outputs=['cam/image_array','imageoriginal'],threaded=False) <== Define the methode, imput, outputs and if its  thraded.
            
            V.add= Vehicule add methode
            AC_Imagecontour() = name of the methode in the AC_Imagecontour.py file
            inputs=['cam/image_array'] = cam/image_array is the current main image displayed in the web viewer and save for the IA generation. in inputs you define all the parameters of run() parts in your parts execept self. 
            outputs=['cam/image_array','imageoriginal'] = it's all the return var from run() parts in your parts. In this case cam/image_array get the modified image and we create a new var imageoriginal who is the initial image without modification.
            threaded = a parts can be threaded for exemple: for specific captors or others, not a good idea for image processing, color detection or others

# Little tips
 - dont go too fast and make error, make sur yout IA doesnt make error, penality are hard!
 - prepare in myconfig.py, parameters to easy modification on your var in parts
 - use a line detector (FC 51 ir sensor for exemple) to auto correct when line crossing 

# usefull link:
 -Live of the competition : https://www.youtube.com/watch?v=lWOdJ5ZOY6o
 -Donkeycar doc : https://docs.donkeycar.com/
 -Donkeycar Discord : https://discord.com/invite/PN6kFeA

Good Luck and anjoy this project!
For question contact us by email at hfabre.ing2022@esaip.org
