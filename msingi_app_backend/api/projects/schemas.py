from fastapi_camelcase import CamelModel



class BaseProject(CamelModel):
    title: str
    description: str


class CreateProject(BaseProject):
    pass

class UpdateProject(CamelModel):
    title: str | None
    description: str | None

class GetProject(BaseProject):
    id: int

    class Config:
        orm_mode = True


