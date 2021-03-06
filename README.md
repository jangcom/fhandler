# fhandler - File handling assistant

## SYNOPSIS

    python fhandler.py [-h] [--func FUNC]
                       [--flag FLAG] [--inplace]
                       [--cmt_symbs [CMT_SYMBS [CMT_SYMBS ...]]]
                       [--num_spaces NUM_SPACES]
                       [--sep_from SEP_FROM] [--sep_to SEP_TO] [--add_row_idx]
                       [--ts_lev {d,dt,none}] [--ts_pos {bef,aft}] [--nopause]
                       file [file ...]

## DESCRIPTION

    fhandler provides methods that can facilitate file handling.
    Currently available methods include:
        - adj_leading_spaces
        - sep2sep
        - tilder

## OPTIONS

    -h, --help
        Help message

    --func FUNC
        adj_leading_spaces (default)
            Adjust the leading spaces of input files.
        sep2sep
            Change a data separator to a designated one.
        tilder
            Back up files into respective subdirectories.

    --flag FLAG
        A filename flag to be appended to the output file

    --inplace
        Changes will be made directly to the input files.

    --cmt_symbs [CMT_SYMBS [CMT_SYMBS ...]]
        Comment symbols of the input files

    --num_spaces NUM_SPACES
        [adj_leading_spaces] Number of leading spaces to be adjusted

    --sep_from SEP_FROM
        [sep2sep] Old data separator

    --sep_to SEP_TO
        [sep2sep] New data separator

    --add_row_idx
        [sep2sep] Prepend indices to data rows.

    --ts_lev {d,dt,none}
        [tilder] Timestamp level

    --ts_pos {bef,aft}
        [tilder] Timestamp position relative to the input filename

    --nopause
        Do not pause the shell at the end of the program.

    file ...
        Files to be handled

## EXAMPLES

    --func adj_leading_spaces
        python fhandler.py ./samples/adj_leading_spaces/proglangs.tex --flag _inc --num_spaces=4
        python fhandler.py ./samples/adj_leading_spaces/proglangs.tex --flag _dec --num_spaces=-4

    --func sep2sep
        python fhandler.py ./samples/sep2sep/yields_mo99-veg0_20to50-wrcc-vhgt0p10to0p30.dat --func sep2sep --flag _s2t --sep_to tab
        python fhandler.py ./samples/sep2sep/yields_au196_1-veg0_20to50-wrcc-vhgt0p10to0p30.dat --func sep2sep --flag _s2c --sep_to ,

    --func tilder
        python fhandler.py ./samples/tilder/dummy.txt --func tilder
        python fhandler.py ./samples/tilder/dummy.txt --func tilder --ts_lev none

## REQUIREMENTS

Python 3

## SEE ALSO

- [dhandler - Directory handling assistant](https://github.com/jangcom/dhandler)

- [tilder - Back up files into respective subdirectories](https://github.com/jangcom/tilder)

## AUTHOR

Jaewoong Jang <<jangj@korea.ac.kr>>

## COPYRIGHT

Copyright (c) 2020 Jaewoong Jang

## LICENSE

This software is available under the MIT license;
the license information is found in "LICENSE".
