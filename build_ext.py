"""Build optional C extension modules."""

import os
from distutils.command.build_ext import build_ext
from os.path import join
from typing import Any

try:
    from setuptools import Extension
except ImportError:
    from distutils.core import Extension

fnv_module = Extension(
    "fnv_hash_fast._fnv_impl",
    [
        join("src", "fnv_hash_fast", "_fnv_impl.c"),
    ],
    language="c",
    extra_compile_args=["-O3", "-g0"],
)


class BuildExt(build_ext):
    def build_extensions(self) -> None:
        try:
            super().build_extensions()
        except Exception:  # nosec
            pass


def build(setup_kwargs: Any) -> None:
    if os.environ.get("SKIP_CYTHON", False):
        return
    try:
        setup_kwargs.update(
            dict(
                ext_modules=[fnv_module],
                cmdclass=dict(build_ext=BuildExt),
            )
        )
    except Exception:
        if os.environ.get("REQUIRE_CYTHON"):
            raise
        pass
