from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?

input = open(from_file, 'r')
indata = input.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exits? %r" % exists(to_file)
print" Read, hit return to continue, CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()

