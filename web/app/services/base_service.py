import json
from abc import ABC
from app.models.errors import RedirectError

class BaseService(ABC):
    def _parse_error_message(self, response):
        try:
            return json.loads(response.content).get("message", "Unexpected error")
        except (json.JSONDecodeError, AttributeError):
            return "Failed parsing response message."

    def _handle_response(self, response):
        match response.status_code:
            case 200:
                return response

            case 401:
                raise RedirectError(
                    message=self._parse_error_message(response),
                    redirect_url="auth.login",
                )

            case 409:
                message = self._parse_error_message(response)
                if "password" in message:
                    redirect_url = "user.profile"
                else:
                    redirect_url = "auth.register"

                raise RedirectError(
                    message=message,
                    redirect_url=redirect_url,
                )

            case 400:
                raise RedirectError(
                    message=self._parse_error_message(response),
                    redirect_url="auth.verify",
                )

            case 410:
                raise RedirectError(
                    message=self._parse_error_message(response),
                    redirect_url="auth.register",
                )

            case 403:
                raise RedirectError(
                    message=self._parse_error_message(response),
                    redirect_url="user.profile",
                )

            case 503:
                raise Exception("Služba je nedostupná. Prosím zkuste to znovu za chvíli.")

            case 429:
                raise Exception("Zpomal! Příliš mnoho požadavků.")

            case 500:
                raise Exception("Došlo k nečekané chybě na serveru. Zkuste to znovu za chvíli")

            case 404:
                raise Exception("Zadaná adresa nebyla nalezena.")

            case _:
                raise Exception(f"Došlo k nečekané chybě na serveru. Zkuste to znovu za chvíli")