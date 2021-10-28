#include <pybind11/pybind11.h>
#include "other.h"

namespace py = pybind11;

PYBIND11_MODULE(gassppi, m) {
    m.doc() = "pybind11 gassppi plugin";
    m.def("add", &add, "A function which add two numbers");
}
