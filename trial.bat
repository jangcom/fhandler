@echo off
rem File by file
python fhandler.py ./samples/proglangs.tex --func adj_leading_spaces --flag _inc --num_space=4
python fhandler.py ./samples/proglangs.tex --func adj_leading_spaces --flag _dec --num_space=-4
python fhandler.py ./samples/proglangs.tex --func adj_leading_spaces --flag _inc_dec --num_space=4
python fhandler.py ./samples/proglangs_inc_dec.tex --func adj_leading_spaces --inplace --num_space=-4

rem Multiple files at once
echo on
set inpath=./samples/
python fhandler.py %inpath%/proglangs_inc.tex %inpath%/proglangs_dec.tex
