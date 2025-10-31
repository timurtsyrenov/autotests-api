from typing import TypedDict

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from httpx import Response


class User(TypedDict):
    """
    Описание структуры пользователя.
    """

    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestDict(TypedDict):
    """
    Структура запроса для создания пользователя.
    """

    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """

    user: User


class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичным API /api/v1/users.
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создаёт пользователя.

        :param request: Словарь с email, password, lastName, firstName и middleName.
        :return: Ответ от сервера (httpx.Response).
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
