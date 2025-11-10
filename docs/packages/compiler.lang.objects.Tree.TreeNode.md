# Class: compiler.lang.objects.Tree.TreeNode
## Method: TreeNode.construct
Constructs the object

| Argument | Description |
| --- | --- |
| name=None | Name of the node |
| parent=None | Parent of the node |

## Method: TreeNode.add
Adds a new child node to the tree

| Argument | Description |
| --- | --- |
| node | Node to add |

## Method: TreeNode.remove
Removes a child node

| Argument | Description |
| --- | --- |
| node | Node to remove |

## Method: TreeNode.move_to
Move the children from one node to another.

| Argument | Description |
| --- | --- |
| target | Target node |

## Method: TreeNode.clear
Deletes all child nodes

| Argument | Description |
| --- | --- |

## Method: TreeNode.destroy
Destroys a node (does not remove it from the list)

| Argument | Description |
| --- | --- |
| node | Node to destroy |

## Method: TreeNode.get
Gets a node using a path notation. (New nodes are created if none exists).

| Argument | Description |
| --- | --- |
| path | Path of the node |

## Method: TreeNode.find
Returns a node associated with a gven path

| Argument | Description |
| --- | --- |
| path | Relative path of the node |

## Method: TreeNode.match
Searches for the first node with a matching name

| Argument | Description |
| --- | --- |
| name | Name of the node |
| flags=0 | UNUSED |

## Method: TreeNode.traverse
Helper function to iterate through child nodes of a node and invoke a callback

| Argument | Description |
| --- | --- |
| fn | Function to call back |
| ctxt | Context argumen passed to the function |
| maxleve=1 | Maximum depth to recurse into |

## Method: TreeNode.traverse_sibling
Helper function to iterate through all the siblings of a node and invoke a callback

| Argument | Description |
| --- | --- |
| fn | Function to call back |
| ctxt | Context argumen passed to the function |

## Method: TreeNode.traverse_child
Helper function to iterate through child nodes of a node and invoke a callback

| Argument | Description |
| --- | --- |
| fn | Function to call back |
| ctxt | Context argumen passed to the function |

## Method: TreeNode.at
Returns a child by index

| Argument | Description |
| --- | --- |
| ndx | Index of the child to return |

## Method: TreeNode.child
Returns a child node with a matching name

| Argument | Description |
| --- | --- |
| name | Name of the node to search for |

## Method: TreeNode.path
Returns the path of the node

| Argument | Description |
| --- | --- |

## Method: TreeNode.level
Returns the depth of the node

| Argument | Description |
| --- | --- |

## Method: TreeNode.get_path
Returns the path of the node

| Argument | Description |
| --- | --- |

## Method: TreeNode.size
Returns the number of children of the node

| Argument | Description |
| --- | --- |

## Method: TreeNode.level
Returns the number of parents to this node

| Argument | Description |
| --- | --- |

## Method: TreeNode.parent
Returns the parent of this node

| Argument | Description |
| --- | --- |

## Method: TreeNode.set_parent
Sets the parent of this node

| Argument | Description |
| --- | --- |
| parent | Parent node |

## Method: TreeNode.data
Gets the data associated with the node

| Argument | Description |
| --- | --- |

## Method: TreeNode.data
Sets the data associated with the node

| Argument | Description |
| --- | --- |
| data | Opaque data value |

## Method: TreeNode.name
Returns the name of the node

| Argument | Description |
| --- | --- |

## Method: TreeNode.name
Sets the name of the node

| Argument | Description |
| --- | --- |
| name | Name of the node |

