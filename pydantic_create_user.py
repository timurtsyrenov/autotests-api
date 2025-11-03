from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """
    Схема данных пользователя.

    Представляет информацию о пользователе в системе, включая идентификатор,
    адрес электронной почты и ФИО.

    Attributes:
        id (str): Уникальный идентификатор пользователя (например, UUID).
        email (EmailStr): Адрес электронной почты пользователя.
        last_name (str): Фамилия пользователя. JSON-ключ — "lastName".
        first_name (str): Имя пользователя. JSON-ключ — "firstName".
        middle_name (str): Отчество пользователя. JSON-ключ — "middleName".
    """

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Схема запроса на создание пользователя.

    Используется для получения данных от клиента при регистрации нового пользователя.

    Attributes:
        email (EmailStr): Адрес электронной почты пользователя.
        password (SecretStr): Пароль пользователя.
        last_name (str): Фамилия пользователя. JSON-ключ — "lastName".
        first_name (str): Имя пользователя. JSON-ключ — "firstName".
        middle_name (str): Отчество пользователя. JSON-ключ — "middleName".
    """

    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа при создании пользователя.

    Возвращает информацию о зарегистрированном пользователе в виде вложенного объекта.

    Attributes:
        user (UserSchema): Объект пользователя с данными профиля.
    """

    user: UserSchema
