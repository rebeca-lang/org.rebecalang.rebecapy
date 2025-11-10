# Class: compiler.lang.program.Call.Call
## Method: Call.__init__
Constructor

| Argument | Description |
| --- | --- |
| method | Method name |
| args | Map of arguments to the method |
| lineno | Linenumber in the code |
| delay | Delay for asynchronous call |

## Method: Call.__joincall
Composes the call instruction

| Argument | Description |
| --- | --- |
| parts | Parts of the call |

## Method: Call.evaluate
Executes the statement

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |

## Method: Call.execute
Executes the statement

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |

## Method: Call.__call_object
Invokes a method call

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |
| obj | Reference to the object |

## Method: Call.__call_subroutine
Calls a subroutine

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |

## Method: Call.__str__
A string notation of the object

| Argument | Description |
| --- | --- |

