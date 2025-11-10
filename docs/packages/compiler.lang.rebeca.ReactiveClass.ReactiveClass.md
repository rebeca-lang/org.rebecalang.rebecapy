# Class: compiler.lang.rebeca.ReactiveClass.ReactiveClass
## Method: ReactiveClass.constructor
Defines the constructor for the reactive class

| Argument | Description |
| --- | --- |
| instructions | Instructions of the constructor |
| arglist | Argument list of the constructor |

## Method: ReactiveClass.destructor
Defines the destructor for the reactive class

| Argument | Description |
| --- | --- |
| instructions | Instructions of the destructor |

## Method: ReactiveClass.known_rebec
Defines known rebecs for the reactive class

| Argument | Description |
| --- | --- |
| names | Names of the rebecs |
| rtype | Type of the rebecs |

## Method: ReactiveClass.state_var
Defines state variables of the reactive class

| Argument | Description |
| --- | --- |
| names | Name of the variables |
| vtype | Type of the variables |

## Method: ReactiveClass.msg_server
Defines a message server for the reactive class

| Argument | Description |
| --- | --- |
| name | Name of the message server |
| instructions | Instructions of the message server |
| arglist | Argument list of the message server |

## Method: ReactiveClass.local_function
Defines a local function for the reactive class

| Argument | Description |
| --- | --- |
| name | Name of the local function |
| rtype | Return type of the local function |
| instructions | Instructions of the constructor |
| arglist | Argument list of the constructor |

## Method: ReactiveClass.construct
Invokes a on instance of the reactive class

| Argument | Description |
| --- | --- |
| inst | Instance to be constructed |
| ctxt | Runtime memory context |
| args | arguments |

## Method: ReactiveClass.invoke
Invokes a method of the reactive class

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |
| method | Method name |
| args | arguments |

## Method: ReactiveClass.get_method
Retrieves a method by its name

| Argument | Description |
| --- | --- |
| name | Name of the method |

