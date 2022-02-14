from clnbusinesslog.UseCase import UseCase


class PingAppUseCase(UseCase):
    def __implementation__(self, *args, **kwargs):
        return {"ping": "ok"}


pingApp = PingAppUseCase()
