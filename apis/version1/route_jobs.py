from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, session

from db.session import get_db
from db.models.jobs import Job
from db.repository.jobs import create_new_job, retreive_job
from schemas.jobs import JobCreate, ShowJob

router = APIRouter()

@router.post("/", response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job=job, db = db, owner_id=owner_id)
    return job

@router.get("/get/{id}", response_model=ShowJob)
def retreive_job_by_id(id: int, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail = f"Job with id {id} does not exist")
    return job