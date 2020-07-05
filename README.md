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

<pre><code>    python fhandler.py [-h] [--func FUNC] [--flag FLAG]
                       [--inplace] [--num_spaces NUM_SPACES]
                       [--cmt_symbs [CMT_SYMBS [CMT_SYMBS ...]]]
                       file [file ...]</code></pre>

<h1 id="DESCRIPTION">DESCRIPTION</h1>

<pre><code>    fhandler provides functions that can facilitate file handling.</code></pre>

<h1 id="OPTIONS">OPTIONS</h1>

<pre><code>    -h, --help
        Help message

    --func FUNC
        adj_leading_spaces (default)
            Adjust the leading spaces of input files.

    --flag FLAG
        A filename flag to be appended to the output file

    --inplace
        Changes will be made directly to the input files.

    --num_spaces NUM_SPACES
        [adj_leading_spaces] Number of leading spaces to be adjusted

    --cmt_symbs [CMT_SYMBS [CMT_SYMBS ...]]
        [adj_leading_spaces] Comment symbols of the input files

    file ...
        Files to be handled</code></pre>

<h1 id="EXAMPLES">EXAMPLES</h1>

<pre><code>    python fhandler.py ./samples/proglangs.tex --func adj_leading_spaces --flag _inc --num_space=4
    python fhandler.py ./samples/proglangs.tex --func adj_leading_spaces --flag _dec --num_space=-4</code></pre>

<h1 id="REQUIREMENTS">REQUIREMENTS</h1>

<p>Python 3</p>

<h1 id="SEE-ALSO">SEE ALSO</h1>

<p><a href="https://github.com/jangcom/dhandler">dhandler - Directory handling assistant</a></p>

<h1 id="AUTHOR">AUTHOR</h1>

<p>Jaewoong Jang &lt;jangj@korea.ac.kr&gt;</p>

<h1 id="COPYRIGHT">COPYRIGHT</h1>

<p>Copyright (c) 2020 Jaewoong Jang</p>

<h1 id="LICENSE">LICENSE</h1>

<p>This software is available under the MIT license; the license information is found in &#39;LICENSE&#39;.</p>


</body>

</html>
