#!/usr/bin/python
# Filename: Token.py
# Description: Implementation of the Token class

from enum import Enum

class TokenType(Enum):			
    VARIABLE        = 1
    CONSTANT        = 2
    KEYWORD         = 3
    PRAGMA          = 4

		

if __name__ == "__main__":
	test = TokenType.VARIABLE

