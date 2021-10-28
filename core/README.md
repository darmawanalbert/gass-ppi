# GASS-PPI Core Modules

Written in C++.

## pybind11

### Prerequisites

1. Install `python3-dev` package
2. Install `pybind11` package. [Guide](https://pybind11.readthedocs.io/en/stable/installing.html)
3. Install `cmake` package. [Guide](https://cmake.org/install/)
4. [Sample implementation](https://pybind11.readthedocs.io/en/stable/basics.html)

### Compilation

The C++ source code needs to be compiled into `.so` file, which then copied into the Python web directory.

Then, simply import it inside the Python code (as shown at `test-pybind.py`).

In Linux:
```
c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) gassppi.cpp other.cpp -o gassppi$(python3-config --extension-suffix)
```

In Mac:
```
c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup $(python3 -m pybind11 --includes) gassppi.cpp other.cpp -o gassppi$(python3-config --extension-suffix)
```

More details can be found at the [official documentation](https://pybind11.readthedocs.io/en/stable/compiling.html#building-manually)

