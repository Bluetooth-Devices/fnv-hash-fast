from typing import TYPE_CHECKING, Callable, Union

from fnvhash import FNV1_32_INIT, FNV_32_PRIME, fnva

_FNV_SIZE = 2**32

if TYPE_CHECKING:
    fnv1a_32: Callable[[Union[bytes, bytearray, memoryview]], int]


def fnv1a_32(data: Union[bytes, bytearray, memoryview]) -> int:
    """Pure-Python FNV-1a 32-bit hash fallback.

    The C extension accepts any buffer-protocol object directly; the pure-Python
    path goes through ``fnvhash.fnva`` which only accepts ``bytes``, so
    non-bytes buffer-like inputs are coerced via ``memoryview``.
    """
    if not isinstance(data, bytes):
        data = bytes(memoryview(data))
    return fnva(  # type: ignore[no-any-return]
        data, hval_init=FNV1_32_INIT, fnv_prime=FNV_32_PRIME, fnv_size=_FNV_SIZE
    )


try:
    from ._fnv_impl import _fnv1a_32 as fnv1a_32  # type: ignore[no-redef] # noqa: F811 F401
except ImportError:
    pass
