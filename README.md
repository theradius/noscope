# noscope
A tool for taking snapshots of a Python stack frame. All names in a scope can be saved and loaded with minimal syntax.

Useful in debugging, recursive breakpointing, moving state between python processes and general testing.

## Installation

`pip install noscope`


## Usage
```python
import noscope
foo = 123
noscope.save()
del foo
noscope.load()
print(foo)
```

