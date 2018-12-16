import os
import re
def rename_files():
	os.chdir('/home/anusha/Downloads/anusha1/')
	
	print os.getcwd()
	file_list=os.listdir("/home/anusha/Downloads/anusha1/")
	print(file_list)
		
	for filename in file_list:
		print filename
		renamed = re.search('([a-zA-Z])+.*',filename)
		renamed = renamed.group()
		print "rnamed", renamed
		os.rename(filename, renamed)

rename_files()
