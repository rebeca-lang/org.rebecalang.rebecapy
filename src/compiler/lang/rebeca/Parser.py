#!/usr/bin/python
# Filename: Parser.py
# Description: Parser for the Rebeca vocabulary

from compiler.lang.rebeca.Lexer import Lexer
from compiler.lang.rebeca.Module import Module
from compiler.lang.rebeca.Call import *

from compiler.lang.program.Call	import Call 
from compiler.lang.program.Expression import Expression 
from compiler.lang.program.For import For 
from compiler.lang.program.Assignment import Assignment 
from compiler.lang.program.Declaration import Declaration 
from compiler.lang.program.Do import Do 
from compiler.lang.program.If import If 
from compiler.lang.program.LoopBlock import LoopBlock 
from compiler.lang.program.Return import Return 
from compiler.lang.program.While import While 


 
import ply.yacc as yacc

class Parser:
    def __init__(self, automata=None, evaluator=None):
        self.parser     = None
        self.filename   = None
        self.program    = None
        self.debug      = False
        self.definitions    = None
        return

    def build(self,**kwargs):
        global tokens

        self.lexer          = Lexer()
        self.lexer.build()
        self.tokens	        = self.lexer.tokens

        self.parser         = yacc.yacc(module=self, **kwargs)

        # Initialize the state variables
        self.module         = Module()

        return

    def parse(self, data:str, path:str=None):
        if path is not None:
            self.filename	= path

        data    = self.preprocess(data, path)
        if len(data) == 0:
            return

        self.lexer.setfile( self.filename )

        self.parser.parse(data)
        self.__dump()
        return

    def preprocess(self, data:str, path:str=None):
        data    = data.strip()
        return data

    def __dump(self):
        if self.debug == False:
            return
        
        print( f'Definitions {len(self.definitions)}')
        return

    # GRAMMAR
    def p_model(self, p):
        """
        model : envs blocks main
        """
        blocks  = p[1]
        if blocks is None:
            return
            
        return

    def p_envs(self, p):
        """
        envs : 
        envs : envs env
        """
        self.fold(p, 2)
        return
    
    def p_env(self, p):
        """
        env : ENV DeclAssignment SEMICOLON
        """
        self.module.add_env( p[2] )
        return
    
    def p_blocks(self, p):
        """
        blocks : null_clause
        blocks : reactive_class
        blocks : blocks reactive_class
        """
        self.move(p)
        return

    def p_main(self, p):
        """
        main : MAIN BLOCKSTART main_body BLOCKEND
        """

        # Iterate through the instances and declare it
        for i in p[3]:
            typename    = i[0]
            typename    = i[0]
            typename    = i[0]
            self.module.main.declare(i)
        return

    def p_main_body(self, p):
        """
        main_body : MainStmts
        """
        self.move(p)
        return

    def p_MainStmts(self, p):
        """
        MainStmts : 
        MainStmts : MainStmts InstanceDecl
        """
        self.fold(p, 2)
        return

    def p_InstanceDecl(self, p):
        """
        InstanceDecl : classname identifier LPAREN arglist RPAREN COLON LPAREN arglist RPAREN SEMICOLON
        """
        p[0]    = (p[1], p[2], p[4], p[8])
        return

    def p_classname(self, p):
        """
        classname : identifier
        """
        p[0]    = p[1]
        return

    def p_reactive_class(self, p):
        """
        reactive_class : REACTIVECLASS identifier queue_def BLOCKSTART class_body BLOCKEND
        """
        rclass  = self.module.reactive_class( p[2], p[3] )
        body    = p[5]
        # Add known rebecs and state variables
        for k in body['knownrebecs']:
            rclass.known_rebec( k[1], k[0] )

        # Add state variables
        for k in body['vars']:
            rclass.state_var( k[1], k[0] )

        # Add constructor
        ctor    = body.get('ctor', None)
        if ctor is not None:
            rclass.constructor( ctor[2], ctor[1] )

        # Add destructor
        dtor    = body.get('dtor', None)
        if dtor is not None:
            rclass.destructor( dtor[1], dtor[0] )
            
        # Add servers
        for srv in body['servers']:
            rclass.msg_server( srv[0], srv[2], srv[1] )

        # Add local functions
        for func in body['locals']:
            rclass.local_function( func[0], func[2], func[1] )
        
        return

    def p_class_body(self, p):
        """
        class_body : KnownRebecs Vars Constructor Destructor MsgSrvs LocalFunctions
        """
        p[0]    = {
                    'knownrebecs': p[1], 
                    'vars': p[2], 
                    'ctor': p[3], 
                    'dtor': p[4], 
                    'servers': p[5], 
                    'locals': p[6]
                }
        return

    def p_Constructor(self, p):
        """
        Constructor : 
        Constructor : methodName param_list BLOCKSTART Stmts BLOCKEND
        """
        match len(p):
            case 1:
                p[0]    = None
            case 6:
                p[0]    = (p[1], p[2], p[4])
        return

    def p_Destructor(self, p):
        """
        Destructor : 
        Destructor : OP_NOT methodName LPAREN RPAREN BLOCKSTART Stmts BLOCKEND
        """
        match len(p):
            case 1:
                p[0]    = None
            case 8:
                p[0]    = (p[2], p[6])
        return

    def p_MsgSrvs(self, p):
        """
        MsgSrvs : 
        MsgSrvs : MsgSrv
        MsgSrvs : MsgSrvs MsgSrv
        """
        self.fold(p, 2)
        return

    def p_MsgSrv(self, p):
        """
        MsgSrv : MSGSRV msgName param_list BLOCKSTART Stmts BLOCKEND
        """
        p[0]    = ( p[2], p[3], p[5] )
        return

    def p_msgName(self, p):
        """
        msgName : identifier
        """
        self.move(p)
        return

    def p_LocalFunctions(self, p):
        """
        LocalFunctions : 
        LocalFunctions : LocalFunction
        LocalFunctions : LocalFunctions LocalFunction
        """
        self.fold(p,2)
        return

    def p_LocalFunction(self, p):
        """
        LocalFunction : ReturnType methodName param_list BLOCKSTART Stmts ReturnStmt BLOCKEND
        """
        p[0]    = ( p[2], p[3], p[5] )
        return

    def p_methodName(self, p):
        """
        methodName : identifier
        """
        self.move(p)
        return

    def p_param_list(self, p):
        """
        param_list : LPAREN params RPAREN
        """
        p[0]    = p[2]
        return

    def p_params(self, p):
        """
        params : 
        params : param
        params : params COMMA param
        """
        match len(p):
            case 1: # No parameters
                p[0]    = []
            case 2: # Single parameter
                p[0]    = [p[1]]
            case 4: # Multiple parameters
                values  = p[1]
                values.append(p[3])
                p[0]    = values
        return

    def p_param(self, p):
        """
        param : ExtType identifier
        """
        p[0]    = (p[1], p[2])
        return

    def p_KnownRebecs(self, p):
        """
        KnownRebecs : 
        KnownRebecs : KNOWNREBECS BLOCKSTART var_decls BLOCKEND
        """
        match len(p):
            case 1: # No known rebecs
                p[0]    = []
            case 5:
                p[0]    = p[3]
        return

    def p_Vars(self, p):
        """
        Vars : 
        Vars : STATEVARS BLOCKSTART var_decls BLOCKEND
        """
        match len(p):
            case 1: # No state variables
                p[0]    = []
            case 5:
                p[0]    = p[3]
        return

    def p_var_decls(self, p):
        """
        var_decls : 
        var_decls : VarDcl
        var_decls : var_decls VarDcl
        """
        self.fold(p, 2)
        return

    def p_VarDcl(self, p):
        """
        VarDcl : Type varlist SEMICOLON
        """
        p[0]    = (p[1], p[2])
        return

    def p_ReturnType(self, p):
        """
        ReturnType : TYPE_VOID
        ReturnType : ExtType
        """
        # TODO: Introduce array and type checking
        self.move(p)
        return

    def p_BuiltinObject(self, p):
        """
        builtinObject : TYPE_LIST
        builtinObject : TYPE_MAP
        builtinObject : TYPE_STACK
        builtinObject : TYPE_QUEUE
        builtinObject : TYPE_PORT
        builtinObject : TYPE_FSM
        """
        self.move(p)
        return


    def p_ExtType(self, p):
        """
        ExtType : TYPE_FLOAT
        ExtType : TYPE_DOUBLE
        ExtType : Type
        """
        # TODO: Introduce array and type checking
        self.move(p)
        return

    def p_Type(self, p):
        """
        Type : TYPE_BOOLEAN
        Type : TYPE_INT
        Type : TYPE_SHORT
        Type : TYPE_BYTE 
        Type : className
        Type : builtinObject
        Type : Type LBRACKET number RBRACKET
        """
        match len(p):
            case 2:
                p[0]    = p[1]
            case 5:
                p[0]    = f'{p[1]}[{p[3]}]'
        return

    

    def p_className(self, p):
        """
        className : identifier
        """
        self.move(p)
        return

    def p_varlist(self, p):
        """
        varlist : identifier
        varlist : varlist identifier
        """
        self.fold(p, 2)
        return

    def p_queue_def(self, p):
        """
        queue_def : 
        queue_def : LPAREN INTEGER RPAREN
        """
        match len(p):
            case 4:
                p[0] = p[2]
            case 1:
                p[0] = -1
        return

    def p_Stmts(self, p):
        """
        Stmts : 
        Stmts : Stmts Stmt
        """
        self.fold(p, 2)
        return

    def p_Stmt(self, p):
        """
        Stmt : LocalVars SEMICOLON
        Stmt : DeclAssignment SEMICOLON
        Stmt : SendMessage SEMICOLON
        Stmt : MethodCall SEMICOLON
        Stmt : ConditionalStmt
        Stmt : LoopStmt
        Stmt : DelayStmt
        Stmt : TraceStmt
        """
        match len(p):
            case 2:
                p[0]    = p[1]
            case 3:
                p[0]    = p[1]
            case _:
                self.throw( p, 'Invalid statement' )

        return

    def p_ReturnStmt(self, p):
        """
        ReturnStmt : 
        ReturnStmt : RETURN Exp SEMICOLON
        """
        if len(p) == 1:
            p[0]    = None
        else:
            p[0]    = Return( ','.join(p[2]) )
        return

    def p_Assignment(self, p):
        """
        Assignment : AssignmentExpr 
        """
        p[0]        = p[1]
        return
    
    def p_DeclAssignment(self, p):
        """
        DeclAssignment : ExtType AssignmentExpr 
        DeclAssignment : AssignmentExpr 
        """
        if len(p) == 3:
            expr            = p[2]
            expr.type       = p[1]
            expr.declare    = True
        else:
            expr    = p[1]

        p[0]    = expr
        return

    def p_SendMessage(self, p):
        """
        SendMessage : rebecExp DOT msgName LPAREN ArgList RPAREN
        """
        opcode  = SendMessage( f'{p[1]}.{p[3]}', p[5] )
        p[0]    = opcode.location( self.location(p) )

        return

    def p_ObjectMethodCall(self, p):
        """
        ObjectMethodCall : identifier DOT msgName LPAREN ArgList RPAREN
        """
        opcode  = Call( f'{p[1]}.{p[3]}', p[5] )
        p[0]    = opcode.location( self.location(p) )

        return

    def p_MethodCall(self, p):
        """
        MethodCall : methodName LPAREN ArgList RPAREN
        """
        method  = p[1]
        args    = p[3]

        opcode  = Call( p[1], p[3] )
        p[0]    = opcode.location( self.location(p) )
        return

    def p_DelayStmt(self, p):
        """
        DelayStmt : DELAY LPAREN Exp RPAREN SEMICOLON
        """
        opcode  = Delay( p[3] )
        p[0]    = opcode.location( self.location(p) )
        return

    def p_TraceStmt(self, p):
        """
        TraceStmt : TRACE LPAREN Exp RPAREN SEMICOLON
        """
        opcode  = Trace( p[3] )
        p[0]    = opcode.location( self.location(p) )
        return

    def p_ConditionalStmt(self, p):
        """
        ConditionalStmt : IF LPAREN LogicalExp RPAREN ConditionBlock 
        ConditionalStmt : IF LPAREN LogicalExp RPAREN ConditionBlock ELSE ConditionBlock
        """
        opcode  = If( p[3], p[5], p[7] if len(p) == 8 else None )
        p[0]    = opcode.location( self.location(p) )
        return

    def p_LoopStmt(self, p):
        """
        LoopStmt : ForStmt
        LoopStmt : WhileStmt
        """
        self.move(p)
        return

    def p_ForStmt(self, p):
        """
        ForStmt : FOR LPAREN DeclAssignment SEMICOLON LogicalExp SEMICOLON AssignmentExpr RPAREN ConditionBlock
        """
        opcode  = For( p[9], p[3], Expression(p[5]), p[7] )
        p[0]    = opcode.location( self.location(p) )
        return

    def p_WhileStmt(self, p):
        """
        WhileStmt : WHILE LPAREN LogicalExp RPAREN ConditionBlock
        """
        opcode  = While( Expression(p[3]), p[5] )
        p[0]    = opcode.location( self.location(p) )
        return

    def p_ConditionBlock(self, p):
        """
        ConditionBlock : BLOCKSTART Stmts BLOCKEND
        ConditionBlock : Stmt
        """
        if len(p) == 4:
            p[0]    = p[2]
        else:
            p[0]    = [p[1]]

        return
    
    def p_LocalVars(self, p):
        """
        LocalVars : ExtType varlist
        """
        p[0]    = Declaration( p[1], p[2] ) 
        return
    
    def p_AssignmentExpr(self, p):
        """
        AssignmentExpr : rebecName OP_EQUALS Exp 
        AssignmentExpr : IncrementExpr
        AssignmentExpr : DecrementExpr
        """
        match len(p):
            case 4:
                opcode  = Assignment( p[1], p[3] )
                p[0]    = opcode.location( self.location(p) )
            case 2:
                p[0]    = p[1]
            case _:
                self.throw( p, 'Invalid assignment expression' )

        return   

    def p_IncrementExpr(self, p):
        """
        IncrementExpr : rebecName INCR
        IncrementExpr : rebecName PLUS OP_EQUALS Exp
        """
        match len(p):
            case 3:
                p[0]    = Assignment(p[1], f'{p[1]} + 1')
            case 5:
                p[0]    = Assignment(p[1], f'{p[1]} + {p[4]}')
            case _:
                self.throw( p, 'Invalid increment expression' )
        return   

    def p_DecrementExpr(self, p):
        """
        DecrementExpr : rebecName DECR 
        DecrementExpr : rebecName MINUS OP_EQUALS Exp
        """
        match len(p):
            case 3:
                p[0]    = Assignment(p[1], f'{p[1]} - 1')
            case 5:
                p[0]    = Assignment(p[1], f'{p[1]} - {p[4]}')
            case _:
                self.throw( p, 'Invalid decrement expression' )

        return   


    def p_rebecExp(self, p):
        """
        rebecExp : SELF
        rebecExp : rebecTerm
        """
        self.move(p)
        return

    def p_rebecTerm(self, p):
        """
        rebecTerm : SENDER
        rebecTerm : rebecName
        """
        self.move(p)
        return

    def p_rebecName(self, p):
        """
        rebecName : identifier
        rebecName : arrayVar
        """
        self.move(p)
        return

    def p_arrayVar(self, p):
        """
        arrayVar : identifier LBRACKET Exp RBRACKET
        """
        p[0]    = f'{p[1]}[{p[3]}]'
        return

    def p_ArgList(self, p):
        """
        ArgList :
        ArgList : Exp
        ArgList : ArgList COMMA Exp
        """
        match len(p):
            case 1:
                p[0]    = []
            case 2:
                p[0]    = [p[1]]
            case 4:
                values  = p[1]
                values.append(p[3])
                p[0]    = values
            case _:
                self.throw( p, 'Invalid argument list' )
        return

    def p_Exp(self, p):
        """
        Exp : arg
        Exp : MathExp
        Exp : LogicalExp
        Exp : ChoiceExp
        Exp : ObjectMethodCall
        Exp : LPAREN Exp RPAREN
        """
        match len(p):
            case 2:
                p[0]    = p[1]
            case 4:
                p[0]    = p[2]
            case _:
                self.throw( p, 'Invalid expression' )
        return
    
    def p_TerenaryExp(self, p):
        """
        ChoiceExp : QUESTION LPAREN Exp COMMA Exp RPAREN
        """
        return

    def p_LogicalExp(self, p):
        """
        LogicalExp : arg
        LogicalExp : MathExp
        LogicalExp : LogicExp
        LogicalExp : LPAREN LogicalExp RPAREN
        """
        match len(p):
            case 2:
                p[0]    = p[1]
            case 4:
                p[0]    = p[2]
            case _:
                self.throw( p, 'Invalid logical expression' )
        return

    def p_LogicExp(self, p):
        """
        LogicExp : MathExpArg LOGIC_AND MathExpArg
        LogicExp : MathExpArg LOGIC_OR MathExpArg
        LogicExp : MathExpArg LTE MathExpArg
        LogicExp : MathExpArg GTE MathExpArg
        LogicExp : MathExpArg LT MathExpArg
        LogicExp : MathExpArg GT MathExpArg
        LogicExp : MathExpArg EQ MathExpArg 
        LogicExp : MathExpArg NEQ MathExpArg
        LogicExp : EXCLAMATION MathExpArg
        """
        match len(p):
            case 3: # Unary operator
                p[0]    = f'not {p[2]}'
                return
            
        op  = p[2]
        match op:
            case '&&':
                op  = 'and'
            case '||':
                op  = 'or'
            case '<=' | '>=' | '<' | '>' | '==' | '!=':
                pass
            case _:
                self.throw( p, f'Invalid logical operator {op}' )

        p[0]    = f'({p[1]} {op} {p[3]})'
        return

    def p_MathExp(self, p):
        """
        MathExp : MathExpArg PLUS MathExpArg
        MathExp : MathExpArg MINUS MathExpArg
        MathExp : MathExpArg MULTIPLY MathExpArg
        MathExp : MathExpArg DIVIDE MathExpArg
        MathExp : MathExpArg MODULO MathExpArg
        MathExp : MathExpArg OP_AND MathExpArg
        MathExp : MathExpArg OP_OR MathExpArg
        """
        match len(p):
            case 3: # Unary operator
                p[0]    = f'not {p[2]}'
                return
            
        op  = p[2]

        match len(p):
            case 3: # Unary operator
                p[0]    = f'not {p[2]}'
                return
            
        op  = p[2]
        match op:
            case '&':
                op  = 'and'
            case '|':
                op  = 'or'
            case '+' | '-' | '*' | '/' | '%':
                pass
            case _:
                self.throw( p, f'Invalid logical operator {op}' )

        p[0]    = f'({p[1]} {op} {p[3]})'
        return

    def p_MathExpArg(self, p):
        """
        MathExpArg : arg
        MathExpArg : Exp
        """
        self.move(p)
        return

    def p_null_clause(self, p):
        """
        null_clause : 
        """
        p[0]    = None
        return
    
    def p_rvalue(self, p):
        """
        rvalue : identifier
        rvalue : number
        rvalue : boolean
        """
        self.move(p)
        return
    
    def p_array(self, p):
        """
        array : LBRACKET arglist RBRACKET
        """
        self.move(p, p[2])
        return

    def p_arglist(self, p):
        """
        arglist :
        arglist : arg
        arglist : arglist COMMA arg
        """
        self.fold(p, 3)
        return

    def p_arg(self, p):
        """
        arg : SENDER
        arg : SELF
        arg : identifier
        arg : number
        arg : boolean
        arg : string
        arg : arrayVar
        """

        if p[1] == 'null':
            p[0]    = None
        else:
            self.move(p)
        return


    def p_value(self, p):
        """
        value : IDENTIFIER
        value : FLOAT
        value : INTEGER
        value : string
        value : boolean
        """
        p[0]    = p[1]
        return

    def p_string(self, p):
        """
        string : STRING
        """
        
        p[0]    = ('string', p[1])
        return

    def p_identifier(self, p):
        """
        identifier : IDENTIFIER
        """
        p[0]    = p[1]
        return

    def p_boolean(self, p):
        """
        boolean : TRUE
        boolean : FALSE
        """
        val    = p[1]

        if val == 'true' :
            p[0]    = True
        else:
            p[0]    = False

        return

    def p_number(self, p):
        """
        number : INTEGER
        number : FLOAT
        """
        p[0]    = p[1]
        return

    def p_error(self, p):
        loc   = self.location(p)            
        raise TypeError( f"{loc[0]}:{loc[1]} Unknown text at \'{p.value}\' [{p.type}]" )

        
    def resolve(self, p, var):
        if len(self.definitions) == 0:
            return var
        
        token   = var
        for n in range(64):
            next    = self.definitions.get(token, None)
            if next is None:
                return token
            
            token     = next

        self.throw( p, f'Recursive definition in variable {var}' )

    def move(self, p, arg=None):
        if arg is None:
            arg = p [1]
        p[0]    = arg
        return
    
    def fold(self, p, offset):
        match len(p):
            case 1:
                result    = []
            case 2:
                result    = [p[1]]
            case _:
                values  = p[1]
                values.append(p[offset])
                result  = values

        p[0]    = result
        return

    def location(self, p):
        if p.lexer.filename is not None:
            context = p.lexer.filename
        else:
            context = 'line'
        return (context, p.lexer.lineno)

    def here(self, p):
        loc   = self.location(p)
        return f'{loc[0]}:{loc[1]}'

    def throw(self, p, ex):
        raise RuntimeError( f'{self.location(p)} {ex}' )
    
    def trace(self, p):
        print(f'->{len(p)}:')
        if self.filename is not None:
            context = self.filename
        else:
            context = 'line'
        path    = []
        for i in range(1, len(p.stack)):
            value = p.stack[i].value
            if value is None:
                value   = 'None'

            path.append( str(value) )

        vars    = []
        for i in range(1, len(p)):
            vars.append(str(p[i]))

        print(f"{self.location(p)} \n  at `{' '.join(path)}`\n  expression=`{','.join(vars)}`")
        return

    
if __name__ == "__main__":
    parser  = Parser()
    file    =  'compiler\\test-cases\\TwoPhaseCommitProtocol.rebeca'
    parser.build()
    with open(file, 'rt') as f:
        codepage = f.read()
        parser.parse(codepage, file)
        print(parser.module)
