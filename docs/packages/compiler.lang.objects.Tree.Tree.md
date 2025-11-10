# Class: compiler.lang.objects.Tree.Tree
## Method: Tree.vtble
Virtual table of the Tree class

| Argument | Description |
| --- | --- |

## Method: Tree.invoke
Invokes a method on the tree

| Argument | Description |
| --- | --- |
| ctxt | Runtime memory context |
| method | Method name |
| args | arguments |

## Method: Tree.clear
Clears the tree

| Argument | Description |
| --- | --- |

## Method: Tree.count
Returns the number of nodes in the tree

| Argument | Description |
| --- | --- |

## Method: Tree.add
Adds a child node to a node a path

| Argument | Description |
| --- | --- |
| path | Path of the parent node |
| node | Node to attach |
| value | Value |

## Method: Tree.remove
Reemoves a node identifed by a path

| Argument | Description |
| --- | --- |
| path | Path of the node |

## Method: Tree.match
Searches for a node with a matching name

| Argument | Description |
| --- | --- |
| name | Name of the node |
| flags=0 | UNUSED |

## Method: Tree.find
Finds a node at a particular path

| Argument | Description |
| --- | --- |
| path | Path of the node |

## Method: Tree.find_node
Finds a node at a particular path

| Argument | Description |
| --- | --- |
| path | Path of the node |

## Method: Tree.exists
Checks if a node exists at a particular path

| Argument | Description |
| --- | --- |
| path | Path of the node |

## Method: Tree.get
Gets a node using a path notation. (New nodes are created if none exists).

| Argument | Description |
| --- | --- |
| path | Path of the node |

## Method: Tree.traverse
Helper function to iterate through child nodes of a node and invoke a callback

| Argument | Description |
| --- | --- |
| fn | Function to call back |
| ctxt | Context argumen passed to the function |
| maxleve=1 | Maximum depth to recurse into |

## Method: Tree.dump
Dumps the tree to an output stream

| Argument | Description |
| --- | --- |
| flags=0 | Flag used to control the ouput |

## Method: Tree.root
Returns the root node

| Argument | Description |
| --- | --- |

## Method: Tree.root
Sets a new root node

| Argument | Description |
| --- | --- |
| node | new root node |

## Method: Tree.attach_root
Attaches a new root node

| Argument | Description |
| --- | --- |
| node | new root node |

