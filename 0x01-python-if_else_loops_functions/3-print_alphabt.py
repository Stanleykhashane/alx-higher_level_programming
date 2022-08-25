#!/usr/bin/python3
#this is version 3 of the code and it uses .replace() function to remove q and e 
for ch in range(97,123):
  print("{:c}".format(ch).replace("q","").replace("e",""), end='')
