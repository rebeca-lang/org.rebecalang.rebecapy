# Class: compiler.lang.rebeca.RuntimeContext.RuntimeContext
## Method: RuntimeContext.__init__
Constructor

| Argument | Description |
| --- | --- |
| module | Rebeca module |
| factory | Factory for creating actors and objects |

## Method: RuntimeContext.stacklen
Size of the stack

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.fork
Forks the current runtime context

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.clone
Clones the current runtime context

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.create
Creates a runtime context from a module

| Argument | Description |
| --- | --- |
| module | Rebeca module to create a context from |
| argv | Arguments for the main rebec |

## Method: RuntimeContext.destroy
Destroys the runtime context

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.bind
Binds the rebec instances in the context

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.step
Runs a single step of the runtime context

| Argument | Description |
| --- | --- |

## Method: RuntimeContext.get
Retrieves a variable from the context

| Argument | Description |
| --- | --- |
| name | Name of the variable |

## Method: RuntimeContext.create_actor
Creates a new actor instance

| Argument | Description |
| --- | --- |
| rc | Runtime context |
| name | Name of the actor |
| idents | Identifiers |
| params | Parameter list |

## Method: RuntimeContext.create_object
Creates a runtime object

| Argument | Description |
| --- | --- |
| type | Object type |

