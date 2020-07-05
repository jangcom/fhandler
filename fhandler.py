#!/usr/bin/env python3
import os
import sys
import re
import argparse


class FHandler():
    def __init__(self):
        self.cwd = os.getcwd()
        self.funcs = {
            'adj_leading_spaces': self.adj_leading_spaces,
            # ... Add new file handling functions here.
        }
        self.border_len = 60
        self.borders = {s: s * self.border_len for s in ['-', '=', '+', '*']}

    def read_argv(self):
        """Read in sys.argv."""
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('--func',
                            default='adj_leading_spaces',
                            choices=['adj_leading_spaces'],
                            help='file handling function')
        parser.add_argument('--flag',
                            default='_new',
                            help=('filename flag'
                                  + 'to be appended to the output file'))
        parser.add_argument('--inplace',
                            action='store_true',
                            help=('changes will be made'
                                  + ' directly to the input files'))
        parser.add_argument('--num_spaces',
                            default=-4,
                            type=int,
                            help=('[adj_leading_spaces]'
                                  + ' number of leading spaces'
                                  + ' to be adjusted'))
        parser.add_argument('--cmt_symbs',
                            default=['#', '%'],
                            nargs='*',
                            help=('[adj_leading_spaces]'
                                  + ' comment symbols of the input files'))
        parser.add_argument('file',
                            nargs='+',
                            help='files to be handled')
        return parser.parse_args()

    def disp_func_run(self, msg,
                      border_symb='-'):
        """Display a message that a function will be run."""
        print(self.borders[border_symb])
        print(msg)
        print(self.borders[border_symb])

    def yn_prompt(self,
                  msg='Continue? (y/n)> '):
        """Invoke a y/n prompt."""
        while True:
            yn = input(msg)
            if re.match(r'\b[yY]\b', yn):
                return True
            if re.match(r'\b[nN]\b', yn):
                return False

    def exam_exists(self, files,
                    action='exit', border_symb='*'):
        """Examine if the designated files exist."""
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
        """Warn of the inplace toggle."""
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
        """Adjust the leading spaces of input files."""
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

        # Work on the input files.
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


if __name__ == '__main__':
    """fhandler - File handling assistant"""
    import fhandler
    fh = fhandler.FHandler()

    # I/O
    args = fh.read_argv()

    # Preprocessing
    args.file = fh.exam_exists(args.file)
    fh.warn_inplace(args.inplace)

    # Run the user-requested file handling function.
    fh.funcs[args.func](args)
