'''
File: elf2hex.py
Created Date: 2023-02-26 08:53:02 pm
Author: Mathieu Escouteloup
-----
Last Modified: 2023-02-26 08:53:10 pm
Modified By: Mathieu Escouteloup
-----
License: See LICENSE.md
Copyright (c) 2023 HerdWare
-----
Description: 
'''


import click
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import NoteSection, SymbolTableSection, Section
from elftools.elf.segments import Segment

@click.command()
@click.option('--input',                    help='Path to input file')
@click.option('--wide',   default=16,       help='Number of bytes per line')
@click.option('--output', default='f.hex',  help='Path to output file')
@click.option('--word',   default=1,        help='Number of bytes per word')



def read_elf_file(input, wide, output, word):
    e = ELFFile(open(input, 'rb'))
    acc2 = [bytearray(), bytearray()]
    accumulator = bytearray()
    for seg in e.iter_segments():
        accumulator = extend_with_segment(accumulator, seg)

    whole_string = gen_string(accumulator, wide, word)

    # write to output file
    with open(output, "w") as hex_file:
        hex_file.write(whole_string)
    

def extend_with_segment(accumulator, segment):
    start_addr = segment['p_paddr']
    size = segment['p_memsz']
    end_addr = start_addr + size

    data = segment.data()    

    while len(accumulator) < end_addr:
        accumulator += bytearray(1)
    
    for add in range(start_addr, end_addr):
        if (len(data) > (add-start_addr)):
            accumulator[add] = data[add-start_addr]
    
    return accumulator

def gen_string(byte_data, wide, word):
    str_word = ""
    str_out = ""

    bcount = 1
    bdata = bytes(byte_data)

    for b in bdata:
        s = "%02x" % b

        # Word string
        if (word == 1):
            str_word = s
        elif ((bcount % word) == 1):
            str_word = s
        else:
            str_word = s + str_word

        # Output string
        if ((bcount % word) == 0):
            str_out += str_word

            if ((bcount % wide) == 0):
               str_out += '\n'
            else:
               str_out += ' ' 

        # Next byte
        bcount = bcount + 1

    return str_out

if __name__ == '__main__':
    read_elf_file()
    