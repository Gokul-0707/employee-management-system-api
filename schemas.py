from pydantic import BaseModel,ConfigDict,EmailStr,Field


class Employee(BaseModel):
    name: str
    email: EmailStr
    department: str
    salary: float =Field(gt=0)
class EmployeeUpdate(BaseModel):
    name: str
    email: EmailStr
    department: str
    salary: float = Field(gt=0)
class EmployeeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:int
    name:str
    email:str
    department:str
    salary:float
class DeleteResponse(BaseModel):
    message: str
    employee_id: int