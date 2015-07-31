import os
def rename_files():
	files=os.listdir(r"C:/Users/801959/prank")
	#current_path=os.getcwd()
	#print files
	os.chdir(r"C:/Users/801959/prank")
	newfile=[]
	for file_name in files:
		#file_name.translate(None, '0123456789')
		#newfile.append(file_name.translate(None,'0123456789'))
        #print newfile
		os.rename(file_name,file_name.translate(None, "0123456789"))
	#os.chdir(current_path)
    
rename_files()