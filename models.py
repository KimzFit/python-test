from pydantic import BaseModel


class User(BaseModel):
  name : str
  age : int
  
class Student(User):
  student_id : int