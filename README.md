# N1081B-SDK-Python

SDK for N1081B / DT1081B for Python, as a package.

# Installation

You can install it using:

```
pip install https://github.com/ENRG-tr/N1081B-SDK-Python.git
```

# Usage

Import the package, and initialize N1081B SDK:

```python
from n1081b import N1081B

device = N1081B("host:port")
device.login("password")

# ...
```
