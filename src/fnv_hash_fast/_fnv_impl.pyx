# distutils: language = c

import cython


cdef extern from "fnv_wrapper.h":
    unsigned int _c_fnv1a_32(const unsigned char *data, size_t len)

@cython.binding(False)
def _fnv1a_32(const unsigned char[::1] data):
    cdef size_t length = data.shape[0]
    if length == 0:
        return 0x811c9dc5  # FNV1a_32 offset basis for empty input
    return _c_fnv1a_32(&data[0], length)
