import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", action="store", dest="input")
parser.add_argument("--output", action="store", dest="output")
parser.add_argument("--fan", action="store", dest="fan")
args = parser.parse_args()

print("Input File: %s" % args.input)
print("Output File: %s" % args.output)
print("Fan Channel: %s" % args.fan)

fh_in = open(args.input, "r")
fh_out = open(args.output, "w")

for line in fh_in:
	if re.match("M106", line):
		line_parts = line.split(" ")
		line_parts.insert(1, args.fan)
		for part in line_parts:
			fh_out.write(part+" ")
	else:
		fh_out.write(line)

fh_in.close()
fh_out.close()