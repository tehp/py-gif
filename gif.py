import imageio
import sys
import getopt
import os
from os import walk

name = '' # Name of input folder

images = []
f = []
p = '' + name + '/' # Input folder location path
out = '/' + name + '.gif' # Output folder location path

print("reading dir: " + p)

try:
    os.remove(p + '.DS_Store')
except OSError:
    print("No .DS_Store, skipping...")


for (dirpath, dirnames, filenames) in walk(p):
    f.extend(filenames)
    break

f.sort()
print(f)

for filename in f:
    images.append(imageio.imread(p + filename))

imageio.mimsave(
    out, images, duration=1.3)

print("output to: " + out)
