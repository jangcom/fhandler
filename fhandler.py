#!/usr/bin/env python3
"""File handling assistant

Classes
-------
FHandler()
    A collection of methods that can facilitate file handling
"""

__version__ = '1.00'
__author__ = 'Jaewoong Jang'

import os
import sys
import re
from datetime import datetime
import shutil
import argparse


class FHandler():
    """A collection of methods that can facilitate file handling

    This class provides methods that can automate some mundane,
    repetitive file handling tasks, such as changing data limiters
    and backing up files.

    Attributes
    ----------
    border_len : int
        The number of symbols of a border line
    borders : dict
        Storage for border lines of different symbols
    funcs : dict
        Storage for the objects of file handling methods

    Methods
    -------
    read_argv()
        Read in sys.argv using the argparse module.
    disp_func_run(msg, border_symb='-')
        Display a message that a function will be run.
    yn_prompt(msg='Continue? (y/n)> ')
        Invoke a y/n prompt.
    exam_exists(files, action='exit', border_symb='*')
        Examine if the designated files exist.
    warn_inplace(inplace, border_symb='*')
        Warn of the inplace toggle.
    adj_leading_spaces(args, encoding='utf-8')
        Adjust the leading spaces of input files.
    sep2sep(args, encoding='utf-8')
        Change a data separator to a designated one.
    tilder(args)
        Back up files into respective subdirectories.

    Notes
    -----
    When a file handling method is newly defined, add the name and
    object of the method as a key-value pair to the funcs attribute;
    a user selects which file handling method to use via the command
    line argument --func, which will then be used as a key of the
    funcs attribute.
    """

    def __init__(self):
        """Bind the objects of file handling methods to a dict."""
        self.border_len = 60
        self.borders = {s: s * self.border_len for s in ['-', '=', '+', '*']}
        self.funcs = {
            'adj_leading_spaces': self.adj_leading_spaces,
            'sep2sep': self.sep2sep,
            'tilder': self.tilder,
            # ... Add new file handling methods here.
        }

    def read_argv(self):
        """Read in sys.argv using the argparse module.

        Returns
        -------
        argparse.Namespace
            An object of argparse.Namespace
        """
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('--func',
                            default='adj_leading_spaces',
                            choices=self.funcs.keys(),
                            help='file handling function')
        parser.add_argument('--flag',
                            default='_new',
                            help=('filename flag'
                                  + 'to be appended to the output file'))
        parser.add_argument('--inplace',
                            action='store_true',
                            help=('changes will be made'
                                  + ' directly to the input files'))
        parser.add_argument('--cmt_symbs',
                            default=['#', '%'],
                            nargs='*',
                            help='comment symbols of the input files')
        parser.add_argument('--num_spaces',
                            type=int,
                            default=-4,
                            help=('[adj_leading_spaces]'
                                  + ' number of leading spaces'
                                  + ' to be adjusted'))
        parser.add_argument('--sep_from',
                            default='space',
                            help='[sep2sep] old data separator')
        parser.add_argument('--sep_to',
                            default='tab',
                            help='[sep2sep] new data separator')
        parser.add_argument('--add_row_idx',
                            action='store_true',
                            help='[sep2sep] prepend indices to data rows')
        parser.add_argument('--ts_lev',
                            default='d',
                            choices=['d', 'dt', 'none'],
                            help='[tilder] timestamp level')
        parser.add_argument('--ts_pos',
                            choices=['bef', 'aft'],
                            default='aft',
                            help=('[tilder] timestamp position'
                                  + ' relative to the input filename'))
        parser.add_argument('--nopause',
                            action='store_true',
                            help=('do not pause the shell'
                                  + ' at the end of the program'))
        parser.add_argument('file',
                            nargs='+',
                            help='files to be handled')
        return parser.parse_args()

    def disp_func_run(self, msg,
                      border_symb='-'):
        """Display a message that a function will be run.

        Arguments
        ---------
        msg : str
            The message to be displayed
        border_symb : str
            A key of the borders attribute (default '-')
        """
        print(self.borders[border_symb])
        print(msg)
        print(self.borders[border_symb])

    def yn_prompt(self,
                  msg='Continue? (y/n)> '):
        """Invoke a y/n prompt.

        Arguments
        ---------
        msg : str
            The prompt message (default 'Continue? (y/n)> ')

        Returns
        -------
        bool
            True for y or Y, False for n or Y
        """
        while True:
            yn = input(msg)
            if re.match(r'\b[yY]\b', yn):
                return True
            if re.match(r'\b[nN]\b', yn):
                return False

    def exam_exists(self, files,
                    action='exit', border_symb='*'):
        """Examine if the designated files exist.

        Arguments
        ---------
        files : list
            Files to be examined whether they exist
        action : str
            Actions for nonexisting files (default 'exit')
        border_symb : str
            A key of the borders attribute (default '*')

        Returns
        -------
        existing_files : list
            Files found to exist out of the designated files
        """
        existing_files = []
        for f in files:
            f = os.path.abspath(f)
            if os.path.exists(f):
                existing_files.append(f)
        if not existing_files:
            print(self.borders[border_symb])
            print(f'None of the designated files found.', end='')
            if action == 'exit':
                print(' Terminating.')
                print(self.borders[border_symb])
                sys.exit()
            print('')  # For action != 'exit'
            print(self.borders[border_symb])
        return existing_files

    def warn_inplace(self, inplace,
                     border_symb='*'):
        """Warn of the inplace toggle.

        inplace : bool
            The sign whether this method should run or not
        border_symb : str
            A key of the borders attribute (default '*')
        """
        if inplace:
            print(self.borders[border_symb])
            print('[--inplace] toggled on:')
            print('Changes will be made directly to the input files.')
            print(self.borders[border_symb])
            y = self.yn_prompt()
            if not y:
                sys.exit()

    def adj_leading_spaces(self, args,
                           encoding='utf-8'):
        """Adjust the leading spaces of input files.

        Arguments
        ---------
        args : argparse.Namespace
            The list of command line arguments passed
        encoding : str
            The encoding of input and output files (default 'utf-8')
        """
        self.disp_func_run('adj_leading_spaces():'
                           + ' Adjusting leading spaces'
                           + f' by [{args.num_spaces}]...')
        # Preprocessing
        cmt_symbs_str = ''.join(args.cmt_symbs)
        if args.num_spaces < 0:  # Remove leading spaces.
            patt = re.compile(f'^([{cmt_symbs_str}]*)'
                              + r'[\s]{' + str(abs(args.num_spaces)) + '}')
            repl = r'\1'
        if args.num_spaces >= 0:  # Feed leading spaces.
            patt = re.compile(f'^([{cmt_symbs_str}]*)')
            repl = r'\1' + ' ' * args.num_spaces

        # Begin leading space adjustment.
        for f in args.file:
            lns_new = ''  # Initialization
            # Adjust the leading spaces of an abspath-ed input file.
            f_abs = os.path.abspath(f)
            fh_abs = open(f_abs, encoding=encoding)
            for ln in fh_abs:
                ln_new = re.sub(patt, repl, ln)
                lns_new += ln_new
            fh_abs.close()
            # Write the modified lines to an output file.
            f_abs_new = '{}{}{}'.format(os.path.splitext(f_abs)[0],
                                        '' if args.inplace else args.flag,
                                        os.path.splitext(f_abs)[1])
            fh_abs_new = open(f_abs_new, 'w', encoding=encoding)
            fh_abs_new.write(lns_new)
            fh_abs_new.close()
            # Report using the input filename as is (i.e. not abspath-ed).
            f_new = '{}{}{}'.format(os.path.splitext(f)[0],
                                    '' if args.inplace else args.flag,
                                    os.path.splitext(f)[1])
            print('Input:  [{}]'.format(f))
            print('Output: [{}]'.format(f_new))

    def sep2sep(self, args,
                encoding='utf-8'):
        """Change a data separator to a designated one.

        Arguments
        ---------
        args : argparse.Namespace
            The list of command line arguments passed
        encoding : str
            The encoding of input and output files (default 'utf-8')
        """
        self.disp_func_run('sep2sep():'
                           + ' Changing the data separator'
                           + f' from [{args.sep_from}] to [{args.sep_to}]...')
        # Preprocessing
        cmt_symbs_str = ''.join(args.cmt_symbs)
        patt_cmt_symbs = re.compile(r'^\s*[{}]+'.format(cmt_symbs_str))
        seps = {
            'from': args.sep_from,
            'to': args.sep_to,
        }
        for k in seps.keys():
            if re.match(r'(?i)space', seps[k]):
                seps[k] = ' '
            if re.match(r'(?i)tab', seps[k]):
                seps[k] = '\t'

        # Begin data separator changing.
        for f in args.file:
            lns_new = ''  # Initialization
            # Change the data separator of an abspath-ed input file.
            f_abs = os.path.abspath(f)
            fh_abs = open(f_abs, encoding=encoding)
            row_idx = 0
            for ln in fh_abs:
                # Skip comment and blank lines.
                if re.match(patt_cmt_symbs, ln) or re.match('^$', ln):
                    lns_new += ln
                    continue
                # Data lines
                data = re.split(r'{}+'.format(seps['from']), ln)
                data[-1] = data[-1].rstrip()
                if args.add_row_idx:
                    data = [str(row_idx)] + data
                    row_idx += 1
                lns_new += seps['to'].join(data)
                lns_new += '\n'  # which was lost by rstrip() in the above
            fh_abs.close()
            # Write the modified lines to an output file.
            f_abs_new = '{}{}{}'.format(os.path.splitext(f_abs)[0],
                                        '' if args.inplace else args.flag,
                                        os.path.splitext(f_abs)[1])
            fh_abs_new = open(f_abs_new, 'w', encoding=encoding)
            fh_abs_new.write(lns_new)
            fh_abs_new.close()
            # Report using the input filename as is (i.e. not abspath-ed).
            f_new = '{}{}{}'.format(os.path.splitext(f)[0],
                                    '' if args.inplace else args.flag,
                                    os.path.splitext(f)[1])
            print('Input:  [{}]'.format(f))
            print('Output: [{}]'.format(f_new))

    def tilder(self, args):
        """Back up files into respective subdirectories.

        Arguments
        ---------
        args : argparse.Namespace
            The list of command line arguments passed
        """
        self.disp_func_run('tilder(): Backing up the input files...')
        # Timestamps
        ymd = datetime.today().strftime('%Y%m%d')
        hm = datetime.today().strftime('%H%M')  # Capital: zero-padded
        ts = ''
        if re.search(r'(?i)\bd\b', args.ts_lev):
            ts = ymd
        elif re.search(r'(?i)\bdt\b', args.ts_lev):
            ts = ymd + '_' + hm
        fname_sep = '_' if ts else ''

        # Buffering
        f_and_f_copy = {}
        for f in args.file:
            # Filenaming
            # e.g. f == './samples/tilder/dummy.txt'
            # dname == '<..>/samples/tilder'
            # fname == 'dummy.txt'
            # bname == 'dummy'
            # ext == '.txt'
            # f_copy == '20200705_dummy' (for args.ts_pos == 'bef')
            # f_copy == 'dummy_20200705' (for args.ts_pos == 'aft')
            # subdir == '<..>/samples/tilder/dummy.txt~'
            f_abs = os.path.abspath(f)
            if not os.path.exists(f_abs) or os.path.isdir(f_abs):
                continue
            dname = os.path.dirname(f_abs)
            fname = os.path.basename(f_abs)
            bname = os.path.splitext(fname)[0]
            ext = os.path.splitext(fname)[1]
            f_copy = None
            if re.match('(?i)bef', args.ts_pos):
                f_copy = ts + fname_sep + bname
            elif re.match('(?i)aft', args.ts_pos):
                f_copy = bname + fname_sep + ts
            if ext:  # Skip extensionless filenames.
                f_copy = f_copy + ext
            # Buffer the original and copy files as key-val pairs.
            subdir = dname + os.sep + fname + '~'
            f_and_f_copy[f] = [  # To be k below
                subdir,  # To be v[0] below
                subdir + os.sep + f_copy,  # To be v[1] below
            ]

        # Flushing
        if f_and_f_copy:
            for k, v in f_and_f_copy.items():
                print('Path:   [{}]'.format(os.path.dirname(k)))
                print('Input:  [{}]'.format(os.path.basename(k)))
                print('Output: [{}]'.format(os.path.basename(v[1])))
                if not os.path.exists(v[0]):
                    os.mkdir(v[0])
                shutil.copyfile(k, v[1])


if __name__ == '__main__':
    fh = FHandler()

    # I/O
    argv = fh.read_argv()

    # Preprocessing
    argv.file = fh.exam_exists(argv.file)
    if argv.func != 'tilder':
        fh.warn_inplace(argv.inplace)

    # Run the user-requested file handling function.
    fh.funcs[argv.func](argv)
    if not argv.nopause:
        input('Press enter to exit...')
