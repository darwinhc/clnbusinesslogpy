from clnbusinesslog.validator.Validator import Validator


class NameValidator(Validator):

    def __implementation__(self, name=None, *args, **kwargs):
        assert isinstance(name, str)
        assert len(name) > 4
