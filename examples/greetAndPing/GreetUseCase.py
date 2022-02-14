from examples.greetAndPing.validator import NameValidator
from clnbusinesslog.UseCase import UseCase


class GreetUseCase(UseCase):
    def __implementation__(self, name, *args, **kwargs):
        return {"message": f"Hi! {name}, how are u?"}



greet = GreetUseCase(input_validator=NameValidator())
