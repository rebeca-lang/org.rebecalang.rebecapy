# Class: compiler.lang.objects.Port.Interface
## Method: Interface.send
Sends a message on a socket

| Argument | Description |
| --- | --- |
| fd | Socket handle |
| msg | Message to send |
| options | Message options |

## Method: Interface.receive
Receives a message on a socket

| Argument | Description |
| --- | --- |
| fd | Socket handle |
| options | Message options |

## Method: Interface.is_pending
Checks if there are pending messages

| Argument | Description |
| --- | --- |
| fd | Socket handle |

## Method: Interface.is_open
Checks if the socket is open

| Argument | Description |
| --- | --- |
| fd | Socket handle |

## Method: Interface.setopt
Sets option on the socket

| Argument | Description |
| --- | --- |
| fd | Socket handle |
| option | Option name |
| value | Option value |

## Method: Interface.getopt
Returns current options on the socket

| Argument | Description |
| --- | --- |
| fd | Socket handle |
| option | Option name |

## Method: Interface.connect
Connects the socket to an address

| Argument | Description |
| --- | --- |
| fd | Socket handle |
| address | Address to connect to |

## Method: Interface.open
Opens the socekt

| Argument | Description |
| --- | --- |
| fd | Socket handle |
| type | Type of the socket |

## Method: Interface.close
Closes the socket

| Argument | Description |
| --- | --- |
| fd | Socket handle |

