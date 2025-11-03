import uuid

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl, ValidationError
from pydantic.alias_generators import to_camel


class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str


try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses",
    )
except ValidationError as error:
    print(error)
    print(error.errors())


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(default=1000)
    min_score: int = Field(default=100)
    description: str = "Playwright course"
    # Вложенный объект для файла-превью
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(default="2 weeks")
    # Вложенный объект для пользователя, создавшего курс
    created_by_user: UserSchema = Field(alias="createdByUser")


# course1 = CourseSchema()
# course2 = CourseSchema()
#
# print(course1.id)
# print(course2.id)

course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses",
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(
        id="user-id", email="user@gmail.com", lastName="Bond", firstName="Zara", middleName="Alise"
    ),
)
print("Course default model:", course_default_model)


course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {"id": "file-id", "url": "http://localhost:8000", "filename": "file.png", "directory": "courses"},
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise",
    },
}
course_dict_model = CourseSchema(**course_dict)
print("Course dict model:", course_dict_model)


course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print("Course JSON model:", course_json_model)
print(course_json_model.model_dump_json(by_alias=True))

# пример распаковки json файла
# import json
#
# with open("course.json", "r") as file:
#     course_data = file.read()
#
# course_model = CourseSchema.model_validate_json(course_data)
# print(course_model)
