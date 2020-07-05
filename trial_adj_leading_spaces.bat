@echo off
set inpath=./samples/adj_leading_spaces
set inp1=%inpath%/proglangs.tex

rem File by file
python fhandler.py %inp1% --func adj_leading_spaces --flag _inc --num_spaces=4
python fhandler.py %inp1% --func adj_leading_spaces --flag _dec --num_spaces=-4
python fhandler.py %inp1% --func adj_leading_spaces --flag _inc_dec --num_spaces=4
python fhandler.py %inpath%/proglangs_inc_dec.tex --func adj_leading_spaces --inplace --num_spaces=-4

rem Multiple files at once
echo on
python fhandler.py %inpath%/proglangs_inc.tex %inpath%/proglangs_dec.tex
