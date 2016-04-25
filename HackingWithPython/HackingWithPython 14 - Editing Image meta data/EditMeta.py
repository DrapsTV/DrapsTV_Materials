from PIL import Image
from PIL.ExifTags import TAGS

def writeMetaData(imgname, tag, replace):
	try:
		metaData = {}
		imgFile = Image.open(imgname)
		imgData = imgFile.getdata()
		print "Getting meta data..."
		info = imgFile._getexif()
		if info:
			print "found meta data!"
			i = 0
			for (tag, value) in info.items():
				i = i + 1
				tagname = TAGS.get(tag, tag)
				#if tagname == tagToReplace:
					#info.items()[i][1] = replace

			print "Saving Change"
			outImg = Image.frombuffer("RGBX",len(imgData)+len(info),imgData+info)
			outImg.save(img)
		
	except:
		print "Failed"

def Main():
	img = "data3.jpg"
	tagToReplace = "Author"
	replace = "Draps"
	writeMetaData(img, tagToReplace, replace)

if __name__ == '__main__':
	Main()