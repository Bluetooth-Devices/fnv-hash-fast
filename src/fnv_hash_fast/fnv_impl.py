from typing import TYPE_CHECKING, Callable, Union

from fnvhash import FNV1_32_INIT, FNV_32_PRIME, fnva

_FNV_SIZE = 2**32

if TYPE_CHECKING:
    fnv1a_32: Callable[[Union[bytes, bytearray, memoryview]], int]


def _fnv1a_32_py(data: Union[bytes, bytearray, memoryview]) -> int:
    if not isinstance(data, bytes):
        data = bytes(memoryview(data))
    return fnva(
        data, hval_init=FNV1_32_INIT, fnv_prime=FNV_32_PRIME, fnv_size=_FNV_SIZE
    )


fnv1a_32 = _fnv1a_32_py

try:
    from ._fnv_impl import _fnv1a_32 as fnv1a_32  # type: ignore[no-redef] # noqa: F811 F401
except ImportError:
    pass
