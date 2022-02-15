from abc import ABCMeta
# Local
from .UseCaseCore import UseCaseCore


class UseCase(UseCaseCore, metaclass=ABCMeta):
    """Use case with integration of input validators to detect possible
    inconsistent or harmful inputs to the system and output validation to detect
    inconsistencies created by developers that violate security."""

    def __init__(self, category=None, input_validator=None,
                 output_validator=None):
        UseCaseCore.__init__(self, category=category)
        if input_validator:
            assert callable(getattr(input_validator, "check", None))
        if output_validator:
            assert callable(getattr(output_validator, "check", None))
        self._in_val = input_validator
        self._out_val = output_validator

    def __run__(self, *args, **kwargs):
        if self._in_val and not self._in_val.check(*args, **kwargs):
            self.abort(400)
        res = super(UseCase, self).__call__(*args, **kwargs)
        if self._out_val and not self._out_val.check(res): return

        return res
