Haven't written python in forever. Thought I would see what python project setup looks like in 2024

## Setup
- `python3 -m venv venv` - create virtual environment 
- `source venv/bin/activate` - activate virtual environment
- `pip install -e .[dev]` - install dev in [editable mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html)
- `tox run -e lint` - lint the project
- `tox run -f test` - test the project (-f runs all tox environements with `test` in their action in tox.ini)
- `tox run -e docs` - build documentation
- `tox run -e build` - actually build the project


