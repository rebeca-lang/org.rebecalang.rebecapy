# Class: compiler.lang.program.PreProcessor.PreProcessor
## Method: PreProcessor.__init__
Constructor

| Argument | Description |
| --- | --- |
| includes | List of include directories |

## Method: PreProcessor.process
Process the given file

| Argument | Description |
| --- | --- |
| path | Path to the file |

## Method: PreProcessor.__get_file
Extract the file path from an import statement

| Argument | Description |
| --- | --- |
| line | Import statement line |

## Method: PreProcessor.__resolve_abs_path
Resolve absolute file path

| Argument | Description |
| --- | --- |
| file | File path to resolve |

## Method: PreProcessor.__resolve_rel_path
Resolve relative file path

| Argument | Description |
| --- | --- |
| parent | Parent directory |
| file | File path to resolve |

## Method: PreProcessor.__resolve_file
Resolve file path

| Argument | Description |
| --- | --- |
| parent | Parent directory |
| file | File path to resolve |

## Method: PreProcessor.__import_file
Import the given file

| Argument | Description |
| --- | --- |
| path | Path to the file |

## Method: PreProcessor.process_line
Processes a single line

| Argument | Description |
| --- | --- |
| pathinfo | Path information tuple (file, line number) |
| line | Line of code to process |

## Method: PreProcessor.process_import
Process an import statement

| Argument | Description |
| --- | --- |
| result | Resulting lines list to append processed lines |
| pathinfo | Path information tuple (file, line number) |
| line | Line of code to process |

