import os
import random
def encode():
	files=os.listdir(r"C:/Users/801959/prank")
	#current_path=os.getcwd()
	#print files
	os.chdir(r"C:/Users/801959/prank")
	for file_name in files:
		os.rename(file_name,str(random.randrange(0,100))+file_name)
    
encode()