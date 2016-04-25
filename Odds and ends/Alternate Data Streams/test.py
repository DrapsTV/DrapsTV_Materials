#Alternate Data Stream Program
import argparse
from pyads import ADS

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help="Specify File or Directory")
	parser.add_argument("-o", "--output", help="Print output to terminal"\
						, action="store_true")
	parser.add_argument("-a", "--add", help="Add stream of <file>"\
						, type=str)
	parser.add_argument("-e", "--extract", help="Extract All"\
						, action="store_true")
	parser.add_argument("-r", "--remove", help="Remove All"\
						, action="store_true")
	args = parser.parse_args()
	
	if args.file:
		handler = ADS(args.file)
		
		if args.add:
			handler.addStream(args.add)
			
		if handler.containStreams():
			for stream in handler.getStreams()[:]:
				if args.output:
					print(args.file+":"+stream)
				if args.extract:
					fh = open(stream,"wb")
					fh.write(handler.getStreamContent(stream))
					fh.close()
				if args.remove:
					handler.removeStream(stream)

	else:
		print(parser.usage)
		
Main()