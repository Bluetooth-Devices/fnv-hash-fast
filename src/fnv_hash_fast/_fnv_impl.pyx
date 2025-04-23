# distutils: language = c

import cython


cdef extern from "fnv_wrapper.h":
    unsigned int _c_fnv1a_32(const unsigned char *data, size_t len)

def _fnv1a_32(data: bytes) -> int:
    return _c_fnv1a_32(data, len(data))
