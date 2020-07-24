# python

[![Run on Repl.it](https://repl.it/badge/github/nicholashoule/python)](https://repl.it/github/nicholashoule/python)

### pyenv

URL: https://github.com/pyenv/pyenv

```
pyenv install -l
```

```
pyenv install 3.8.2

pyenv versions

pyenv shell

```

### pipenv

URL: https://github.com/pypa/pipenv

```
pipenv sync
```

----

##### Pipefile

```
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests = "*"

[dev-packages]
pytest = "*"

[requires]
python_version = "3.7"
```

##### example.py

```python
"""Example import statement styling

.. _PEP 257 -- Docstring Conventions: https://tinyurl.com/y8mlbogq

"""

# Standard library imports
# .. _Python Module Index: https://docs.python.org/3/py-modindex.html#cap-_
import os
import sys
import datetime
import argparse

# Third party imports
# from flask import Flask
# from flask_restful import Api

# Local application imports
# from local_module import local_class
# from local_package import local_function
# from package.sugar import raw

# f: main
def main(): 
    """main
    Desc: Defining main function
    Return: None
    """
    print("Hello, Python.")
    print(os.uname())
    print(sys.platform.title())
    print(datetime.datetime.now())

    if args.integers:
        print(args.accumulate(args.integers))

# Using the special variable  __name__ 
print("Example __name__ = %s" %__name__) 

if __name__ == "__main__":  
    print("Example is being run directly")

    # argparse, argument parser
    # .. _argparse: https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='*',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    main()
else:  
    print("Example is being imported")

```
