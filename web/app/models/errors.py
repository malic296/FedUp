class RedirectError(Exception):
    def __init__(self, message: str, redirect_url: str):
        super().__init__(message)
        self.redirect_url = redirect_url
