'''
File: hex2ascii.py
Created Date: 2023-02-26 08:53:02 pm
Author: Mathieu Escouteloup
-----
Last Modified: 2023-02-26 08:53:32 pm
Modified By: Mathieu Escouteloup
-----
License: See LICENSE.md
Copyright (c) 2023 HerdWare
-----
Description: 
'''


import sys


hexname = sys.argv[1]
asciiname = sys.argv[2]

with open(hexname,'r') as f_hex:   
  with open(asciiname,'wb') as f_ascii:   
    for line in f_hex:   
      for word in line.split():         
        f_ascii.write(bytearray.fromhex(word))
