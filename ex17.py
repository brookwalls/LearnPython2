#from sys import argv
#from os.path import exists

#script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

#indata = open(from_file).read()

#print(f"Does the output file exists? {exists(to_file)}")

#open(to_file, 'w').write(indata)

#print "Alright, all done."

#out_file.close()
#in_file.close()
from sys import argv; open(argv[2], 'w').write(open(argv[1]).read())

#script, fr_file, to_file = argv

#open(argv[2], 'w').write(open(argv[1]).read())
