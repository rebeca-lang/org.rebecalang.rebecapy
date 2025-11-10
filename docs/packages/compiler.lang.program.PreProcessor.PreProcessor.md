# Class: compiler.lang.program.PreProcessor.PreProcessor
## Method: PreProcessor.process
Process the given file

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

