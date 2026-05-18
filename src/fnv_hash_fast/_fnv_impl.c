#include <stdint.h>
#include "Python.h"

/* Release the GIL when hashing payloads at or above this size. Smaller inputs
 * skip the release/reacquire dance, which would otherwise dominate the few
 * hundred nanoseconds of actual work. */
#define FNV_GIL_RELEASE_THRESHOLD 4096

static inline uint32_t
_fnv1a_32(const unsigned char *data, Py_ssize_t len)
{
    uint32_t hash = 0x811c9dc5u;
    for (Py_ssize_t i = 0; i < len; ++i) {
        hash = 0x01000193u * (hash ^ data[i]);
    }
    return hash;
}

static inline uint32_t
_fnv1a_32_nogil(const unsigned char *data, Py_ssize_t len)
{
    uint32_t h;
    Py_BEGIN_ALLOW_THREADS
    h = _fnv1a_32(data, len);
    Py_END_ALLOW_THREADS
    return h;
}

static PyObject *
py_fnv1a_32(PyObject *module, PyObject *arg)
{
    if (!PyBytes_CheckExact(arg)) {
        PyErr_SetString(PyExc_TypeError,
                        "_fnv1a_32 requires a bytes object");
        return NULL;
    }
    const unsigned char *buf = (const unsigned char *)PyBytes_AS_STRING(arg);
    Py_ssize_t len = PyBytes_GET_SIZE(arg);
    uint32_t h = (len >= FNV_GIL_RELEASE_THRESHOLD)
        ? _fnv1a_32_nogil(buf, len)
        : _fnv1a_32(buf, len);
    return PyLong_FromUnsignedLong(h);
}

static PyMethodDef module_methods[] = {
    {"_fnv1a_32", py_fnv1a_32, METH_O, NULL},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "fnv_hash_fast._fnv_impl",
    NULL,
    -1,
    module_methods,
};

PyMODINIT_FUNC
PyInit__fnv_impl(void)
{
    return PyModule_Create(&moduledef);
}
