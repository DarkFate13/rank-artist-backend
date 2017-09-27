import subprocess
import optparse

def add_line_regex(lines, f):
	doc_no = -1
	
	for line in lines:
		if(len(line) < 10):
			continue
		if(line[:10] == "Data from:"):
			doc_no+=1
			print
			continue
			
		line = line.strip()
		line = line + ' @' + format(doc_no, '03d') + '$'
		
		print (line, file = f)

	print(len(lines), file = f)
	
	return doc_no
	
def pre_process_sum(mode):
	query = list(open('../query.txt', 'r'))[0]

	lines = list(open('../tmp_file/' + query + '.txt', 'r'))

	f = open('../tmp_file/formatted_file', 'w+')
	if(f.readline() != query):
		print(query, file = f)
		doc_no = add_line_regex(lines, f)
		
	if(mode == 0):
		subprocess.call("../scripts/gen_luhn.sh")
	if(mode == 1):
		subprocess.call("../scripts/text_sum.sh")
	
	return doc_no
	f.close() 

if __name__ == "__main__":
	parser = optparse.OptionParser()

	parser.add_option('-l', '--luhn',
		action="store_const", const=0, dest="verbose",
		help="Generates Luhn Summary")
	parser.add_option('-t', '--text',
		action="store_const", const=1, dest="verbose",
		help="Generates Text-Sum Summary")
	
	options, args = parser.parse_args()

	pre_process_sum(options.verbose)