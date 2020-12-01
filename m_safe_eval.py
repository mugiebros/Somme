#!/usr/bin/env python3
"""
Définition utiles pour une évaluation sécuritaire du code

Inclue un DIRO pour le builtin eval

2020 Austin Brodeur
"""
import math
from typing import Any

SAFE_GLOBALS = {
    "__builtins__":{},
    **math.__dict__,
    "abs":abs,
    "min":min,
    "max":max,
    "sum":sum,
}
"""globals sécuritaire pour eval et exec"""

def sanitize(code: str) -> str:
    """assainit le code source insécure"""
    return code.replace('__','')

def safe_eval(__source: str, __globals: dict = None, __locals: dict = None) -> Any:
    """Évalue sécuritairement l'expression. Diro pour eval"""
    return eval(sanitize(__source),__globals or SAFE_GLOBALS, __locals)

