# Class: compiler.lang.program.RuntimeContext.RuntimeContext
## Method: RuntimeContext.__init__
Constructor

| Argument | Description |
| --- | --- |
| parent | Parent runtime context |

## Method: RuntimeContext.copy
Copies the runtime context

| Argument | Description |
| --- | --- |
| rhs | Runtime context to copy from |

## Method: RuntimeContext.declare
Declares a new variable in the current scope

| Argument | Description |
| --- | --- |
| name | Variable name |
| value | Initial value for the variable |

## Method: RuntimeContext.set_self
Sets the 'self' pointer in the current context

| Argument | Description |
| --- | --- |
| obj | Object to set as 'self' |

## Method: RuntimeContext.set
Sets the value of a variable in the current context

| Argument | Description |
| --- | --- |
| name | Variable name |
| value | New value for the variable |

## Method: RuntimeContext.test
Tests the runtime context

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.get
Retrieves the value of a variable from the current context

| Argument | Description |
| --- | --- |
| name | Variable name |

## Method: RuntimeContext.step
Executes the current instruction

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |

## Method: RuntimeContext.ip
Returns the instruction pointer for the current stack frame

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.sp
Returns the stack pointer for the current context

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.numvars
Returns the total number of variables in the current context

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.root
Returns the root runtime context

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.variables
Returns a mapping of variable names to their values in the current context

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.callstack
Returns the call stack

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.thisptr
Returns the 'this' pointer for the current context

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.next
Advances the instruction pointer to the next instruction

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.push
Pushes a new stack frame onto the call stack

| Argument | Description |
| --- | --- |
| fname | Function name |
| args | Arguments |
| ip | Instruction pointer |

## Method: RuntimeContext.pop
Pops a stack frame from the call stack

| Argument | Description |
| --- | --- |
| ndx | Index of the frame to pop (default: -1) |

## Method: RuntimeContext.map
Maps the arguments to their values in the current context

| Argument | Description |
| --- | --- |
| args | Arguments to map to after resolution |

## Method: RuntimeContext.trace
Logs a trace message

| Argument | Description |
| --- | --- |
| msg | Message to log |
| logging | Whether to log the message to file (default: False) |

## Method: RuntimeContext.__str__
A string notation of the object

| Argument | Description |
| --- | --- |

