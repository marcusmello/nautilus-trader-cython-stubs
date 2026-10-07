"""
This module exports the fuzzy candle enums for use from Python.

The enums are defined in the .pxd file for use in Cython code,
and this .pyx file makes them available to Python code.
"""

__all__ = [
    "CandleDirection",
    "CandleSize",
    "CandleBodySize",
    "CandleWickSize",
]

# Enums Cython (pxd) expostos a Python. Os membros vivem no enum nativo; aqui a
# declaracao opaca basta para resolucao de import e uso como tipo.
class CandleDirection: ...
class CandleSize: ...
class CandleBodySize: ...
class CandleWickSize: ...