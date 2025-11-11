# Rebeca Python Toolkit
This is the Rebeca python runtime. It is an embeddable verion of Rebeca written entirely in Python. The rebeca language and its tools facilitate verification of actor models within a controlled discrete environment definition. To extend the utility of the models RebecaPy introduces the same actors as embeddable versions in complex uncertain environment, for example a simulation running a world model. Here, hundreds of actors, environmental factors, traffic models, regulatory protocols and the likes may be tested in concert to evaluate situations that closely emulate the real world. 

All source code should be placed in the `src/` directory.

## Contributing to RebecaPy
Note that the package is pre-release and experimental. Your feedback on improvements and bugs would be much appreciated.


## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the main script:
   ```bash
   python apps/rebeca/rebeca.py samples/basics/helloworld.rebeca
   ```

## Project Structure

- `src/` - Source code
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation
- `docs/packages` - [Class library](docs/packages/classes.md)
- `samples/` - [Rebeca samples](samples/README.md)
