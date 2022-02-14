from abc import abstractmethod, ABC


class Validator(ABC):
    """Checking that something is correct in the input or output data"""

    def __init__(self):
        self._name = self.__class__.__name__.replace('Validator', '')

    def check(self, *args, **kwargs):
        try:
            res = self.__implementation__(*args, **kwargs)
            if res is None: return True
            else: return res
        except AssertionError as e:
            print(f"Validator {self._name} has found an inconsistency, {e}")
            return False

    @abstractmethod
    def __implementation__(self, *args, **kwargs): pass
