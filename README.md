# fhandler

<?xml version="1.0" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<link rev="made" href="mailto:" />
</head>

<body>



<ul id="index">
  <li><a href="#NAME">NAME</a></li>
  <li><a href="#SYNOPSIS">SYNOPSIS</a></li>
  <li><a href="#DESCRIPTION">DESCRIPTION</a></li>
  <li><a href="#OPTIONS">OPTIONS</a></li>
  <li><a href="#EXAMPLES">EXAMPLES</a></li>
  <li><a href="#REQUIREMENTS">REQUIREMENTS</a></li>
  <li><a href="#SEE-ALSO">SEE ALSO</a></li>
  <li><a href="#AUTHOR">AUTHOR</a></li>
  <li><a href="#COPYRIGHT">COPYRIGHT</a></li>
  <li><a href="#LICENSE">LICENSE</a></li>
</ul>

<h1 id="NAME">NAME</h1>

<p>fhandler - File handling assistant</p>

<h1 id="SYNOPSIS">SYNOPSIS</h1>

<pre><code>    python fhandler.py [-h] [--func FUNC]
                       [--flag FLAG] [--inplace] [--nopause]
                       [--cmt_symbs [CMT_SYMBS [CMT_SYMBS ...]]]
                       [--num_spaces NUM_SPACES] [--sep_from SEP_FROM]
                       [--sep_to SEP_TO] [--add_row_idx] [--ts_lev {d,dt,none}]
                       [--ts_pos {bef,aft}]
                       file [file ...]</code></pre>

<h1 id="DESCRIPTION">DESCRIPTION</h1>

<pre><code>    fhandler provides functions that can facilitate file handling.
    Currently available functions include:
        - adj_leading_spaces
        - sep2sep
        - tilder</code></pre>

<h1 id="OPTIONS">OPTIONS</h1>

<pre><code>    -h, --help
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

    --nopause
        Do not pause the shell at the end of the program.

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

    file ...
        Files to be handled</code></pre>

<h1 id="EXAMPLES">EXAMPLES</h1>

<pre><code>    --func adj_leading_spaces
        python fhandler.py ./samples/adj_leading_spaces/proglangs.tex --flag _inc --num_spaces=4
        python fhandler.py ./samples/adj_leading_spaces/proglangs.tex --flag _dec --num_spaces=-4

    --func sep2sep
        python fhandler.py ./samples/sep2sep/yields_mo99-veg0_20to50-wrcc-vhgt0p10to0p30.dat --func sep2sep --flag _s2t --sep_to tab
        python fhandler.py ./samples/sep2sep/yields_au196_1-veg0_20to50-wrcc-vhgt0p10to0p30.dat --func sep2sep --flag _s2c --sep_to ,

    --func tilder
        python fhandler.py ./samples/tilder/dummy.txt --func tilder
        python fhandler.py ./samples/tilder/dummy.txt --func tilder --ts_lev none</code></pre>

<h1 id="REQUIREMENTS">REQUIREMENTS</h1>

<p>Python 3</p>

<h1 id="SEE-ALSO">SEE ALSO</h1>

<p><a href="https://github.com/jangcom/dhandler">dhandler - Directory handling assistant</a></p>

<p><a href="https://github.com/jangcom/tilder">tilder - Back up files into respective subdirectories</a></p>

<h1 id="AUTHOR">AUTHOR</h1>

<p>Jaewoong Jang &lt;jangj@korea.ac.kr&gt;</p>

<h1 id="COPYRIGHT">COPYRIGHT</h1>

<p>Copyright (c) 2020 Jaewoong Jang</p>

<h1 id="LICENSE">LICENSE</h1>

<p>This software is available under the MIT license; the license information is found in &#39;LICENSE&#39;.</p>


</body>

</html>