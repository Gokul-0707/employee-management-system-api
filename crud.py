from sqlalchemy.orm import Session

from models import EmployeeDB
from schemas import Employee, EmployeeUpdate


def create_employee(db: Session, employee: Employee):

    db_employee = EmployeeDB(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        salary=employee.salary
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


def get_employees(db: Session):

    return db.query(EmployeeDB).all()


def get_employee(db: Session, employee_id: int):

    return db.query(EmployeeDB).filter(
        EmployeeDB.id == employee_id
    ).first()


def update_employee(
    db: Session,
    employee_id: int,
    employee: EmployeeUpdate
):

    db_employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee_id
    ).first()

    if db_employee is None:
        return None

    db_employee.name = employee.name
    db_employee.email = employee.email
    db_employee.department = employee.department
    db_employee.salary = employee.salary

    db.commit()
    db.refresh(db_employee)

    return db_employee
def delete_employee(db: Session,employee_id:int):
    db_employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee_id
    ).first()
    if db_employee is None:
        return None
    db.delete(db_employee)
    db.commit()
    return db_employee