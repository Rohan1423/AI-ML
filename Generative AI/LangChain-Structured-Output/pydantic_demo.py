from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    # default value for name is set to 'rohan'
    name:str = 'rohan'
    # Optional value for age is set to None
    age:Optional[int] = None
    email:EmailStr
    # cgpa is a float value and Constraint -> it should be greater than 0 and less than 10
    cgpa: float = Field(gt=0, lt=10, default=5, description="A decimal value representing the cgpa of the student")

# here we can define a new student with the default name or we can provide a new name
new_student = {'age': '32', 'email': 'abc@gmail.com'}

student = Student(**new_student)

print(student)

student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()

print(student.name)
print(type(student))