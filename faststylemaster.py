#Training folder 'fast-style-transfer-master' is saved on the desktop. 
#Rain Princess checkpoint is already saved in the 'fast-style-transfer-master'. 
#Save your image to that folder as .jpg file with a simple name. 

#Open the terminal 
conda create -n style-transfer python=2.7.9
source activate style-transfer
pip install tensorflow
conda install scipy pillow

#Enter the conda environment in the terminal 
ls 
cd desktop 
source activate style-transfer 

#where <path_toinput_file> is the jpg file you want to change such as amanda.jpg 
#where the ./output_image.jpg is the name of the new file you are saving 
#python evaluate.py --checkpoint ./rain-princess.ckpt --in-path <path_to_input_file> --out-path ./output_image.jpg
python evaluate.py --checkpoint ./rain-princess.ckpt --in-path amanda.jpg --out-path ./output_image.jpg
