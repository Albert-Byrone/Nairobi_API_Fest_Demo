from fastapi_camelcase import CamelModel
from .schemas import GetProject, GetDevelopment, GetPayment
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



# Developemts

class CreateDevelopmentData(CamelModel):
    development: GetDevelopment | None


class CreateDevelopmentResponse(ResponseModel):
    data: CreateDevelopmentData = CreateDevelopmentData()


class GetDevelopmentsData(CamelModel):
    developments: List[GetDevelopment] | None


class GetDevelopmentsResponse(ResponseModel):
    data: GetDevelopmentsData = GetDevelopmentsData()



class GetPaymentsData(CamelModel):
    payment: List[GetPayment] | None


class GetPaymentsResponse(ResponseModel):
    data: GetPaymentsData = GetPaymentsData()
