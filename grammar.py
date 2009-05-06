# coding: utf-8

import re

keywords = ['BEGIN', 'END', 'CLASS', 'IS', 'METHOD', 'READ', 'WRITE',
            'IF', 'THEN', 'ELSE', 'WHILE', 'DO', 'MOD', 'NEW', 'SELF',
            'NULL', 'TRUE', 'FALSE']

#operators
ops = {'.' : 'PERIOD', ';' : 'SEMICOLON', ',' : 'COMMA', ')' : 'RPAREN',
       '(' : 'LPAREN', '=' : 'EQ', '#' : 'NEQ', '>' : 'GT', '+' : 'PLUS',
       '-' : 'MINUS', '*' : 'TIMES', '/' : 'DIV', ':' : 'COLON', '<' : 'LT'
       }
#operators with len == 2
long_ops = {':' : ('=', 'BECOMES'), '>' : ('=', 'GTEQ'), '<' : ('=', 'LTEQ')}


whitespace = re.compile(r'\s')
letter = re.compile('[a-zA-Z]')
letter_or_digit = re.compile('[a-zA-Z0-9]')
digit = re.compile('[0-9]')
