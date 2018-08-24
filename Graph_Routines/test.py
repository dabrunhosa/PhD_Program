import re

if __name__ == '__main__':
	str = '0 - 4.65656,5.83731,-3.62819,0.127878,0.0407093,0.00130146'
	with open('d002.txt','r') as f:
		str2 = f.read()
	num = "[-+]?[0-9]*\.?[0-9]+(?:e[-+][0-9]+)?"
	p1 = re.compile(num)
	num_comma= "(?:"+num+",?)"
	p2 = re.compile("("+num_comma+"\s*-\s*"+num_comma+"*)\s*\n?")
	p3 = re.compile(num+"\("+num+"\)\s+?-\s+?"+num+"\("+num+"\)")
	matching_lines = p2.findall(str2)
	matching_lines = [p1.findall(line) for line in matching_lines]

	matching_lines2 = p3.findall(str2)
	matching_lines2 = [p1.findall(line) for line in matching_lines2]
	print(matching_lines2)
	print(len(matching_lines2))



