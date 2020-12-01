"""
Version minuté (et sécuritaire) de la fonction builtin eval (DIRO)

2020 Austin Brodeur
"""

from typing import Any
from wrapt_timeout_decorator import timeout
from m_safe_eval import safe_eval

DELAI_SEC = 1.0
"""delai par défaut pour l'éval"""
def timeout_eval(__source: str,
                __globals: dict = None,
                __locals: dict = None,
                safe: bool = True,
                 delai_sec: float = DELAI_SEC) -> Any:
    """
    Évalue l'expression dans un delai donner en argument
    lève un timeout si expiration
    DIRO pour eval
    """
    return capped_eval(__source,__globals,__locals,safe,dec_timeout=delai_sec)

@timeout(DELAI_SEC) # Décorateur
def capped_eval(__source: str,
                __globals: dict = None,
                __locals: dict = None,
                safe: bool = True) -> Any:
    """
    Évalue l'expression dans un delai
    lève un timeout si expiration
    DIRO pour eval
    """
    return(safe_eval if safe else eval)(__source,__globals,__locals)