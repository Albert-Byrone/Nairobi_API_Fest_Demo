from fastapi import Response, APIRouter, status, Depends, FastAPI
from sqlalchemy.orm import Session

from .constants import CREATED_PROJECT_SUCCESSFUL_MESSAGE, GET_PROJECTS_SUCCESSFUL_MESSAGE, UPDATE_PROJECT_SUCCESSFUL_MESSAGE, \
    PROJECT_NOT_FOUND_MESSAGE, PROJECT_DELETED_SUCCESSFUL_MESSAGE, PROJECT_NOT_COMPLETED_MESSAGE, PROJECT_REOPEN_SUCCESSFUL_MESSAGE
from .crud import create_project_crud, get_projects_crud, update_project_crud
from .models import Project
from .responses import CreateProjectResponse, GetProjectsResponse
from .schemas import CreateProject, UpdateProject

# from ..authentication.helpers import verify_access_token
from ..utils import get_db



router = APIRouter()
get = router.get
post = router.post
patch = router.patch


# Defines a POST endpoint for creating a new project.
@post('/projects', response_model=CreateProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(project: CreateProject, response: Response, db: Session = Depends(get_db)):
    project_response = CreateProjectResponse()
    if created_project := create_project_crud(db, project):
        project_response.success = True
        project_response.data.project = created_project
        project_response.message = CREATED_PROJECT_SUCCESSFUL_MESSAGE
    return project_response


@get('/projects', status_code=status.HTTP_200_OK, response_model=GetProjectsResponse)
async def get_projects(response: Response, db: Session = Depends(get_db)):
    projects_response = GetProjectsResponse()
    if projects := get_projects_crud(db):
        projects_response.success = True
        projects_response.data.projects = projects
        projects_response.message = GET_PROJECTS_SUCCESSFUL_MESSAGE
    return projects_response



@patch('/projects/{project_id}', response_model=CreateProjectResponse, status_code=status.HTTP_200_OK)
async def update_project(project_id: int, project: UpdateProject, response: Response,db: Session = Depends(get_db)):
    project_response = CreateProjectResponse()
    project_instance = db.query(Project).filter(Project.id == project_id).first()

    if updated_task := update_project_crud(db, project, project_id):
        project_response.message = UPDATE_PROJECT_SUCCESSFUL_MESSAGE
        project_response.data.project = updated_task
        project_response.success = True
    return project_response


# Inheritance


# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"