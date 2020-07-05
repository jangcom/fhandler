@echo off
set inpath=./samples/tilder
set inp1=%inpath%/dummy.txt
set inp2=%inpath%/shiba.txt

python fhandler.py %inp1% --func tilder
python fhandler.py %inp1% --func tilder --ts_lev none
python fhandler.py %inp1% --func tilder --ts_lev dt
python fhandler.py %inp1% --func tilder --ts_lev d --ts_pos bef
python fhandler.py %inp1% --func tilder --ts_lev dt --ts_pos bef

echo on
rem Multiple files at once
python fhandler.py %inp1% %inp2% --func tilder
