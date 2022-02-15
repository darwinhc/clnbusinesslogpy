# Clean business logic python (clnbusinesslogpy)

## Description
It is to create functionalities in the backend, without dependencies and based on use cases. Minimize the cost of a possible migration to another web framework.

For more information go to the [documentation](https://github.com/darwinhc/clnbusinesslog)


## Download

Download the src folder, rename it and put it in your company's infrastructure package.

## Usage

First, it inherits from the **UseCase** class to create my use case and
creating the method that executes what they need from this use case. And
creating an instance of the use case.

Let’s make an example of this proposal in python language

### Use cases

Python example of greeting use case

``` python
from examples.validator import NameValidator
from usecases.UseCase import UseCase


class GreetUseCase(UseCase):
    def __implementation__(self, name, *args, **kwargs):
        return {"message": f"Hi! {name}, how are u?"}



greet = GreetUseCase(input_validator=NameValidator())
```

### Validators

When we want to create validators we inherit from the **Validator**
class and create the validation implementation.

``` python
from usecases.validator.Validator import Validator


class NameValidator(Validator):

    def __implementation__(self, name=None, *args, **kwargs):
        assert isinstance(name, str)
        assert len(name) > 4
```

For python we can return a Boolean or generate an AssertionError error

### Web framework

Now let’s suppose we want to use this use case for the flask framework

#### Flask example

``` python
from flask import Flask
from markupsafe import escape
# Local
from examples.GreetUseCase import greet
from examples.PingAppUseCase import pingApp

app = Flask(__name__)

@app.route("/greet/<name>")
def greet_route(name): return greet(name=escape(name))
```

Or we also want to use it on console, or test it separately

#### Pure python

``` python
from examples.GreetUseCase import greet
if __name__ == '__main__':
    print(greet(input("What is your name?\n")))
```