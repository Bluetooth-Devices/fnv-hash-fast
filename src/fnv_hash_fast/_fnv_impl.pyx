# distutils: language = c

import cython


cdef extern from "fnv_wrapper.h":
    unsigned int _c_fnv1a_32(const unsigned char *data, size_t len)

@cython.binding(False)
def _fnv1a_32(const unsigned char[::1] data):
    return _c_fnv1a_32(&data[0], data.shape[0])
