# Class: compiler.lang.objects.StateMachine.StateMachine
## Method: StateMachine.__init__
Constructor

| Argument | Description |
| --- | --- |

## Method: StateMachine.vtble
Virtual table of the StateMachine class

| Argument | Description |
| --- | --- |

## Method: StateMachine.invoke
Invokes a method on the state machine

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |
| method | Method name |
| args | arguments |

## Method: StateMachine.transition
Transitions the state machine to a new state

| Argument | Description |
| --- | --- |
| state_input | Input that triggers the transition |

## Method: StateMachine.add
Adds a state transition

| Argument | Description |
| --- | --- |
| current | Current state |
| input | Input to trigger the transition |
| state_to | Target state |

## Method: StateMachine.remove
Removes a state transition

| Argument | Description |
| --- | --- |
| current | Current state |
| input | Input to trigger the transition |

## Method: StateMachine.current
Returns the current state

| Argument | Description |
| --- | --- |

## Method: StateMachine.set_current
Sets the current state

| Argument | Description |
| --- | --- |
| state | New current state |

## Method: StateMachine.default
Returns the default state

| Argument | Description |
| --- | --- |

## Method: StateMachine.set_default
Sets the default state

| Argument | Description |
| --- | --- |
| state | New default state |

## Method: StateMachine.has
Checks if a state transition exists

| Argument | Description |
| --- | --- |
| current | Current state |
| input | Input to trigger the transition |

## Method: StateMachine.load
Loads the state machine from a file

| Argument | Description |
| --- | --- |
| path | Path to the JSON file |

## Method: StateMachine.save
Saves the state machine to a file

| Argument | Description |
| --- | --- |
| path | Path to the JSON file |

## Method: StateMachine.reset
Resets the state machine to the default state

| Argument | Description |
| --- | --- |

## Method: StateMachine.__str__
A string notation of the object

| Argument | Description |
| --- | --- |

