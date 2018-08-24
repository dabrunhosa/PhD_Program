

list_of_files = ['file1.txt','test3.txt']
str_files = []
for file_name in list_of_files:
	str_files.append(open(file_name,'r').read())

all_match = True
for s in range(1,len(str_files)):
	print('loop')
	if not(str_files[s-1] in str_files[s]):
		all_match = False

print(all_match)
