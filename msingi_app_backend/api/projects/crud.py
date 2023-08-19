from sqlalchemy.orm import Session

from .models import Project
from .schemas import CreateProject, UpdateProject, GetProject


def create_project_crud(db: Session, project: CreateProject):
    project_instance = Project(title=project.title, description=project.description)
    db.add(project_instance)
    db.commit()
    db.refresh(project_instance)
    return GetProject(id=project_instance.id, title=project_instance.title, description=project_instance.description)


def get_projects_crud(db: Session):
    projects = db.query(Project).all()
    print("====", projects)
    return [GetProject(id=project.id, title=project.title, description=project.description) for project in projects]


def update_project_crud(db: Session, project: UpdateProject, project_id):
    project_instance = db.query(Project).filter(Project.id == project_id).first()
    if project.title:
        project_instance.title = project.title

    if project.description:
        project_instance.description = project.description
    db.add(project_instance)
    db.commit()
    db.refresh(project_instance)
    return GetProject(id=project_instance.id, title=project_instance.title, description=project_instance.description)
