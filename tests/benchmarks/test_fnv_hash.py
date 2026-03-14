from pytest_codspeed import BenchmarkFixture

from fnv_hash_fast import fnv1a_32

ITERATIONS = 10000


def test_fnv1a_32(benchmark: BenchmarkFixture) -> None:
    _fnv1a_32 = fnv1a_32
    data = b"hello"

    @benchmark
    def _() -> None:
        for _ in range(ITERATIONS):
            _fnv1a_32(data)


def test_fnv1a_32_large_payload(benchmark: BenchmarkFixture) -> None:
    _fnv1a_32 = fnv1a_32
    payload = b"goodbye" * 4096

    @benchmark
    def _() -> None:
        for _ in range(ITERATIONS):
            _fnv1a_32(payload)
