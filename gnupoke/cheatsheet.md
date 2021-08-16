# gnupoke1.3 Cheatsheet

## Options
set base to hexadecimal. default is 10
    .set obase 16

set to little endian
    .set endian little

set byte at offset 2 to value 5
     byte @ 2#B = 5;


## Commands
dump [:from OFFSET] [:size OFFSET]
copy
save
extract
scrabble

## Dotted Commands
.doc <TOPIC>
.info ios
.ios #0
.file #1
.quit


create a memory section and copy a file to it
    .mem scratch
    copy :from_ios 0 :from 0#B :size 64#B
    copy :to_ios 0 :from 0#B

    ::: concatenate operator

# Offset Suffixes
b                   bits
N                   nibbles
B                   bytes
[k|M|G][b|B]        kilo, mega, giga bits/bytes
[ki|Mi|Gi][b|B]     base-10 kilo, mega, giga bits/bytes


## Other
To search a binary file for a binary string and print offsets:

    grep --only-matching --byte-offset --binary --text --perl-regexp '\x50\x4b\x03\x04'

This command is useful for determining the offset at which to apply a map.