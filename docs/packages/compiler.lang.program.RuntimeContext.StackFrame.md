# Class: compiler.lang.program.RuntimeContext.StackFrame
## Method: StackFrame.__init__
Constructor

| Argument | Description |
| --- | --- |
| address | Address of the current instruction |
| return_address | Address to return to after execution |
| vars | Local variables for the stack frame |

## Method: StackFrame.execute
Executes the current instruction

| Argument | Description |
| --- | --- |
| runtime | Runtime environment |
| ctxt | Runtime memory context |

## Method: StackFrame.__str__
A string notation of the object

| Argument | Description |
| --- | --- |

