import re

#!/usr/bin/python
# Filename: Lexer.py
# Description: Lexer for the Rebeca vocabulary

import ply.lex as lex

class Lexer:
    reserved = {
    'define'    	: 'DEFINE',
    'import'    	: 'IMPORT',
    'line'	        : 'LINE',

    'main'          : 'MAIN',
    'reactiveclass' : 'REACTIVECLASS',
    'knownrebecs'   : 'KNOWNREBECS', 
    'statevars'     : 'STATEVARS',
    'msgsrv'        : 'MSGSRV',
    'self'          : 'SELF',
    'sender'        : 'SENDER',

    'if'            : 'IF',
    'else'          : 'ELSE',
    'for'           : 'FOR',
    'while'         : 'WHILE',
    'return'        : 'RETURN',
    'switch'        : 'SWITCH',
    'case'          : 'CASE',
    'break'         : 'BREAK',
    'continue'      : 'CONTINUE',
    'delay'         : 'DELAY',

    'trace'         : 'TRACE',
    
    'port'          : 'TYPE_PORT',
    'queue'         : 'TYPE_QUEUE',
    'stack'         : 'TYPE_STACK',
    'map'           : 'TYPE_MAP',
    'list'          : 'TYPE_LIST',
    'heap'          : 'TYPE_HEAP',
    'tree'          : 'TYPE_TREE',
    'fsm'           : 'TYPE_FSM',


    'void'	        : 'TYPE_VOID',
    'float'	        : 'TYPE_FLOAT',
    'double'	    : 'TYPE_DOUBLE',
    'int'	        : 'TYPE_INT',
    'byte'  	    : 'TYPE_BYTE',
    'boolean'	    : 'TYPE_BOOLEAN',
    'short' 	    : 'TYPE_SHORT',

    'true'	    : 'TRUE',
    'false'	    : 'FALSE'
    }

    # List of token names.   This is always required
    tokens = [                                                     # OPERATORS #
    'EXCLAMATION' , # !
    'QUESTION' ,    # ?
    'PLUS' ,        # +
    'MINUS' ,       # -
    'MULTIPLY',     # *
    'DIVIDE',       # /
    'MODULO',       # %
    'INCR',         # ++
    'DECR',         # --


    'OP_NOT',       # ~
    'OP_EQUALS',    # =

    # COMPARATORS #
    'LT',           # <
    'GT',           # >
    'LTE',          # <=
    'GTE',          # >=
    'EQ',           # ==
    'NEQ',          # !=
    'OP_AND',       # &
    'OP_OR' ,       # |                                                
    'LOGIC_AND',    # &&
    'LOGIC_OR' ,    # ||                                               

    # BRACKETS #
    'LPAREN',       # (
    'RPAREN',       # )
    'LBRACKET',     # [
    'RBRACKET',     # ]
    'BLOCKSTART',   # {
    'BLOCKEND',     # }

    # SCOPE #
    'DOT',     		# .
    'COLON',     	# :
    'SEMICOLON',    # ;
    'AMPERSAND',    # @
    'COMMA',        # ,

    # DATA TYPES#
    'INTEGER',      # int
    'FLOAT',		# floating point numbers
    'STRING',		# strings

    'COMMENT',  	# Multi-line comment
    'COMMENT_SL',  	# Single-line comment

    'PRAGMA_LINE',  # line pragma

    'IDENTIFIER'	# Identifiers

    ] + list(reserved.values())

    # Regular expression rules for simple tokens

    t_EXCLAMATION	= r'\!'
    t_QUESTION	= r'\?'
    t_PLUS		= r'\+'
    t_MINUS		= r'\-'
    t_MULTIPLY	= r'\*'
    t_DIVIDE	= r'\/'
    t_MODULO	= r'\%'
    t_INCR		= r'\+\+'
    t_DECR		= r'\-\-'  
    t_LPAREN 	= r'\('
    t_RPAREN	= r'\)'
    t_LBRACKET	= r'\['
    t_RBRACKET	= r'\]'
    t_BLOCKSTART = r'\{'
    t_BLOCKEND	= r'\}'
    t_OP_NOT	= r'\~'
    t_OP_EQUALS	= r'\='
    t_GT		= r'\>'
    t_LT		= r'\<'
    t_LTE		= r'\<\='
    t_GTE		= r'\>\='
    t_EQ        = r'\=\='
    t_NEQ		= r'\!\='
    t_OP_AND	= r'\&'
    t_OP_OR		= r'\|'
    t_LOGIC_AND = r'\&\&'
    t_LOGIC_OR  = r'\|\|'                                               
    t_COLON		= r'\:'
    t_SEMICOLON	= r'\;'
    t_DOT		= r'\.'
    t_AMPERSAND	= r'\@'
    t_COMMA 	= r','
    t_ignore 	= ' \t'		# A string containing ignored characters (spaces and tabs)


    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        return

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return
    
    def setfile(self, filename):
        self.lexer.filename    = filename
        self.lexer.lineno      = 1
        self.lexer.charpos     = 0
        return
    
    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok: 
                 break
             print(tok)
        return

    # A regular expression rule with some action code
    def t_FLOAT(self, t):
        r'(\d*\.\d+)|(\d+\.\d*)'
        t.value = float(t.value)
        return t        
    
    def t_INTEGER(self, t):
        r'\d+'
        t.value = int(t.value)    
        return t

    def t_STRING(self, t):
        r'["\'](?:\\.|[^\'\\])*["\']'
        t.value = t.value[1:len(t.value)-1]    
        return t

    def t_COMMENT(self, t):
        r'\/\*(\*(?!\/)|[^*])*\*\/'
        pass
        # No return value. Token discarded

    def t_COMMENT_SL(self, t):
        r'\/\/.*'
        pass
        # No return value. Token discarded

    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
        return t
    
    def t_PRAGMA_LINE(self, t):
        r'\#line\s+\d+\s+([^\s]+)'
        match = re.match(r'\#line\s+(\d+)\s+([^\s]+)', t.value)
        
        # Track line numbers for #line directives
        if match:
            line                = int(match.group(1))
            filename            = match.group(2)
            t.lexer.lineno      = line
            t.lexer.filename    = filename
        
        pass

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        numCR       = len(t.value)
        t.lexer.lineno += numCR
        t.lexer.charpos = t.lexer.lexpos+numCR
        return

if __name__ == "__main__":
    # Build the lexer
    lexer = Lexer()
    