from fastapi_camelcase import CamelModel
from .schemas import GetProject
from ..utils import ResponseModel
from typing import List

class CreateProjectData(CamelModel):
    project: GetProject | None


class CreateProjectResponse(ResponseModel):
    data: CreateProjectData = CreateProjectData()


class GetProjectsData(CamelModel):
    projects: List[GetProject] | None


class GetProjectsResponse(ResponseModel):
    data: GetProjectsData = GetProjectsData()

