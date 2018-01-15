#!/usr/bin/python

#Mini Interpreiaitor
Text_string = 0
import os
#from tkinter import *
import sys


def main():
    while True:
        try:
            text = raw = input('Interpretaitor> ')
        except EOFError:
	    print "Going out on KEYBOARD interrupt"
            break
        if not text:
            continue
        if text == 'dir':
            print(os.getcwd())
        if text == '{write':
            Wi = input('              ?> ')
            print(Wi, ' }')
        if text == 'while for h x[/':
            whiled = input('                            ?>')
            if whiled == 'var: nw v;':
                var_nw = input('                         name>')
                var_txt = input('                          var>')
        if text == 'var: file;in{':
            w_var = input('                          name>')
            if w_var == var_nw:
                V1 = var_nw
                print('int>{[', V1, var_txt, 'dne<}]')
        if text == 'var: nw v;':
            var_nw = input('                         name>')
            var_txt = input('                          var>')
        if text == 'Qall':
            sys.exit()
	    print "Leaving on <Qall> command"

        

if __name__ == '__main__':
    main()
