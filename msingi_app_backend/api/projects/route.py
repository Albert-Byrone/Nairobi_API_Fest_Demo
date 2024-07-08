from fastapi import Response, APIRouter, status, Depends, FastAPI
from sqlalchemy.orm import Session

from .constants import CREATED_PROJECT_SUCCESSFUL_MESSAGE, GET_PROJECTS_SUCCESSFUL_MESSAGE, UPDATE_PROJECT_SUCCESSFUL_MESSAGE, \
    PROJECT_NOT_FOUND_MESSAGE, PROJECT_DELETED_SUCCESSFUL_MESSAGE, PROJECT_NOT_COMPLETED_MESSAGE, PROJECT_REOPEN_SUCCESSFUL_MESSAGE,CREATED_DEVELOPMENT_SUCCESSFUL_MESSAGE, GET_DEVELOPMENTS_SUCCESSFUL_MESSAGE, UPDATE_DEVELOPMENT_SUCCESSFUL_MESSAGE, DEVELOPMENT_NOT_FOUND_MESSAGE, DEVELOPMENT_DELETED_SUCCESSFUL_MESSAGE, DEVELOPMENT_ALREADY_ASSIGNED_MESSAGE, DEVELOPMENT_NOT_COMPLETED_MESSAGE, DEVELOPMENT_REOPEN_SUCCESSFUL_MESSAGE
from .crud import create_project_crud, get_projects_crud, update_project_crud, get_project_crud, create_developement_crud, get_developments_crud, get_development_crud, update_development_crud,create_payment_crud
from .models import Project, Development
from .responses import CreateProjectResponse, GetProjectsResponse, CreateDevelopmentResponse, GetDevelopmentsResponse, GetPaymentsResponse
from .schemas import CreateProject, UpdateProject,CreateDevelopment, UpdateDevelopment, CreatePayment

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


@get('/projects/{project_id}', status_code=status.HTTP_200_OK, response_model=CreateProjectResponse)
async def get_project(project_id: int, response: Response, db: Session = Depends(get_db)):
    project_response = CreateProjectResponse()
    if project_instance := get_project_crud(db, project_id):
        project_response.success = True
        project_response.data.project = project_instance
        project_response.message = GET_PROJECTS_SUCCESSFUL_MESSAGE
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        project_response.message = PROJECT_NOT_FOUND_MESSAGE
    return project_response


@patch('/projects/{project_id}', response_model=CreateProjectResponse, status_code=status.HTTP_200_OK)
async def update_project(project_id: int, project: UpdateProject, response: Response,db: Session = Depends(get_db)):
    project_response = CreateProjectResponse()
    project_instance = db.query(Project).filter(Project.id == project_id).first()

    if updated_task := update_project_crud(db, project, project_id):
        project_response.message = UPDATE_PROJECT_SUCCESSFUL_MESSAGE
        project_response.data.project = updated_task
        project_response.success = True
    return project_response


# Inheritanc

# Defines a POST endpoint for creating a new project.
@post('/developments', response_model=CreateDevelopmentResponse, status_code=status.HTTP_201_CREATED)
async def create_development(development: CreateDevelopment, response: Response, db: Session = Depends(get_db)):
    development_response = CreateDevelopmentResponse()
    if created_development := create_developement_crud(db, development):
        development_response.success = True
        development_response.data.development = created_development
        development_response.message = CREATED_DEVELOPMENT_SUCCESSFUL_MESSAGE
    return development_response


@get('/developments', status_code=status.HTTP_200_OK, response_model=GetDevelopmentsResponse)
async def get_developments(response: Response, db: Session = Depends(get_db)):
    development_response = GetDevelopmentsResponse()
    if developments := get_developments_crud(db):
        development_response.success = True
        development_response.data.developments = developments
        development_response.message = GET_DEVELOPMENTS_SUCCESSFUL_MESSAGE
    return development_response


@get('/developments/{development_id}', status_code=status.HTTP_200_OK, response_model=CreateDevelopmentResponse)
async def get_project(development_id: int, response: Response, db: Session = Depends(get_db)):
    project_response = CreateDevelopmentResponse()
    if project_instance := get_development_crud(db, development_id):
        project_response.success = True
        project_response.data.development = project_instance
        project_response.message = GET_DEVELOPMENTS_SUCCESSFUL_MESSAGE
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        project_response.message = DEVELOPMENT_NOT_FOUND_MESSAGE
    return project_response


@patch('/developments/{development_id}', response_model=CreateDevelopmentResponse, status_code=status.HTTP_200_OK)
async def update_project(development_id: int, development: UpdateProject, response: Response,db: Session = Depends(get_db)):
    project_response = CreateDevelopmentResponse()
    project_instance = db.query(Development).filter(Development.id == development_id).first()

    if updated_task := update_development_crud(db, development, development_id):
        project_response.message = UPDATE_DEVELOPMENT_SUCCESSFUL_MESSAGE
        project_response.data.development = updated_task
        project_response.success = True
    return project_response
# Defines a POST endpoint for creating a new project.


@post('/payment', response_model=GetPaymentsResponse, status_code=status.HTTP_201_CREATED)
async def make_payment(payment: CreatePayment, response: Response, db: Session = Depends(get_db)):
    payment_response = GetPaymentsResponse()
    if created_development := create_payment_crud(db, payment):
        payment_response.success = True
        payment_response.data.payment = created_development
        payment_response.message = CREATED_DEVELOPMENT_SUCCESSFUL_MESSAGE
    return payment_response




