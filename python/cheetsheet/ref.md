# Python Cheatsheet
This page has Python links and constructs that I find useful but often forget.

## Style Guides
[Google Python](https://google.github.io/styleguide/pyguide.html)
[PEP8](https://pep8.org)


## Magic ("Dunder" Methods)
Reference: [tutorial](https://rszalski.github.io/magicmethods/)
- with:     ```__enter__, __exit__```
- iterator: ```__iter__, __next__```
- string:   ```__str__```  # human-readable representation of object
- repr:     ```__repr__``` # prints Python code for object
- comparison: ```__gt__, __lt__, ...```
- containers: ```__len__, __getitem__, __setitem__``` and iterator methods

## Class Decorators
```python
# getter
@property
def x(self):
    return self._x

# setter
@<x>.setter
def x(self, x):
    self._x = x

@classmethod
def foo(cls, x):
    print(f'class: {cls}, x = {x}')

@staticmethod
def static_foo(x):
    print(f'x = {x}')
```

## Other Decorators
```python
@lru_cache(max_size=32)
def f(n):
    ...

print(f.cache_info())  # see performance
```


## String Encoding

bytes to unicode string: ```l_bytes.encode()```
string to bytes:         ``````
hexsttring to bytes:     ``````


try/catch/finally