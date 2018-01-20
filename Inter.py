#Mini Interpreiaitor
Text_string = 0
import os
import sys
import pygame

def main():
    while True:
        try:
            text = raw = input('Interpretaitor> ')
        except EOFError:
            break
        if not text:
            continue
        if text == 'dir':
            print(os.getcwd())
        if text == '{write':
            Wi = input('              ?> ')
            print(Wi, ' }')
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
        if text == 'file: nw;':
            name_f = input('              filename> ')
            sys.stderr=open(name_f,'w')
        if text == 'file: open;':
            name_op = input('              filename> ')
            f2 = open(name_op, 'r') 
            fd1 = f2.read()
            print(fd1)
        if text == 'vers>c;<':
            print(sys.platform)



if __name__ == '__main__':
    main()
