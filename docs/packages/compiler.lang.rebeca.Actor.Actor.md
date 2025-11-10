# Class: compiler.lang.rebeca.Actor.Actor
## Method: Actor.__init__
Constructor

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |
| rc | Reactive class of the actor |
| name | Instance name |
| idents | List of known rebecs identifiers |
| params | List of constructor parameters |

## Method: Actor.__build_vars
Build state variables for the actor

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |
| rc | Reactive class of the actor |

## Method: Actor.push_msg
Pushes a message to the actor queue

| Argument | Description |
| --- | --- |
| msg | Message to be pushed |

## Method: Actor.pop_msg
Pops a message from the actor queue

| Argument | Description |
| --- | --- |

## Method: Actor.msgcount
Returns the number of messages in the queue

| Argument | Description |
| --- | --- |

## Method: Actor.runnable
Checks if the actor instance is runnable

| Argument | Description |
| --- | --- |

## Method: Actor.stop
Stops the execution of the actor instance

| Argument | Description |
| --- | --- |

## Method: Actor.construct
Constructs the actor instance

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |

## Method: Actor.destroy
Destroys the actor instance

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |

## Method: Actor.step
Processes pending messages and runs the actor instance

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |

## Method: Actor.invoke
Queues an asynchronous method invocation on the actor instance

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |
| method | Method name |
| args | arguments |
| delay | Optional delay in milliseconds before processing the message |

## Method: Actor.__invoke
Invokes a method on the actor instance

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |
| method | Method name |
| args | arguments |

## Method: Actor.__contructor
Constructs the actor instance

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |

