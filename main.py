from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from database import get_db
from schemas import (
    Employee,
    EmployeeUpdate,
    EmployeeResponse,
    DeleteResponse
)
import crud


app = FastAPI()


# Home
@app.get("/")
def home():
    return {
        "message": "Employee Management System API"
    }

@app.post("/employees", response_model=EmployeeResponse)
def create_employee(
    employee: Employee,
    db: Session = Depends(get_db)
):
    try:
        db_employee= crud.create_employee(
            db,
            employee
        )
        return db_employee
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

@app.get("/employees", response_model=list[EmployeeResponse])
def get_employees(
    db: Session = Depends(get_db)
):
    employees = crud.get_employees(db)

    return employees

@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = crud.get_employee(
        db,
        employee_id
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee

@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    updated_employee = crud.update_employee(
        db,
        employee_id,
        employee
    )

    if updated_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return updated_employee


# Delete Employee
@app.delete("/employees/{employee_id}", response_model=DeleteResponse)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    deleted_employee = crud.delete_employee(
        db,
        employee_id
    )

    if deleted_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully",
        "employee_id": employee_id
    }