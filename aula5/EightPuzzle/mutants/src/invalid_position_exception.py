from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore
class InvalidPositionException(Exception):

    def __init__(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁInvalidPositionExceptionǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁInvalidPositionExceptionǁ__init____mutmut_mutants'), args, kwargs, self)

    def xǁInvalidPositionExceptionǁ__init____mutmut_orig(self):
        self.message = 'Posicao invalida.'
        # super().__init__(self.message)

    def xǁInvalidPositionExceptionǁ__init____mutmut_1(self):
        self.message = None
        # super().__init__(self.message)

    def xǁInvalidPositionExceptionǁ__init____mutmut_2(self):
        self.message = 'XXPosicao invalida.XX'
        # super().__init__(self.message)

    def xǁInvalidPositionExceptionǁ__init____mutmut_3(self):
        self.message = 'posicao invalida.'
        # super().__init__(self.message)

    def xǁInvalidPositionExceptionǁ__init____mutmut_4(self):
        self.message = 'POSICAO INVALIDA.'
        # super().__init__(self.message)
    
    xǁInvalidPositionExceptionǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁInvalidPositionExceptionǁ__init____mutmut_1': xǁInvalidPositionExceptionǁ__init____mutmut_1, 
        'xǁInvalidPositionExceptionǁ__init____mutmut_2': xǁInvalidPositionExceptionǁ__init____mutmut_2, 
        'xǁInvalidPositionExceptionǁ__init____mutmut_3': xǁInvalidPositionExceptionǁ__init____mutmut_3, 
        'xǁInvalidPositionExceptionǁ__init____mutmut_4': xǁInvalidPositionExceptionǁ__init____mutmut_4
    }
    xǁInvalidPositionExceptionǁ__init____mutmut_orig.__name__ = 'xǁInvalidPositionExceptionǁ__init__'
