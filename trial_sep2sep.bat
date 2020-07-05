@echo off
set inpath=./samples/sep2sep
set inp1=%inpath%/yields_mo99-veg0_20to50-wrcc-vhgt0p10to0p30.dat
set inp2=%inpath%/yields_au196_1-veg0_20to50-wrcc-vhgt0p10to0p30.dat
echo on

rem space to tab
python fhandler.py %inp1% --func sep2sep --flag _s2t --sep_to tab

rem tab to comma
python fhandler.py %inpath%/yields_mo99-veg0_20to50-wrcc-vhgt0p10to0p30_s2t.dat --func sep2sep --flag _t2c --sep_from tab --sep_to ,

rem space to comma
python fhandler.py %inp1% --func sep2sep --flag _s2c --sep_to ,

rem comma to space
python fhandler.py %inpath%/yields_mo99-veg0_20to50-wrcc-vhgt0p10to0p30_s2c.dat --func sep2sep --flag _c2s --sep_from , --sep_to space

rem Row index added
python fhandler.py %inp2% --func sep2sep --flag _idxed --add_row_idx

rem Multiple files at once
python fhandler.py %inp1% %inp2% --func sep2sep --flag _s2t
