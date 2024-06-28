from fastapi_camelcase import CamelModel
import cloudinary
import cloudinary.uploader


class BaseProject(CamelModel):
    title: str
    image: str
    description: str
    location: str
    size: str
    bedrooms: str
    dsq: str
    plot_size: str
    prime_location: str
    status: str
    experience: str



class CreateProject(BaseProject):
    pass

class UpdateProject(CamelModel):
    title: str | None
    description: str | None
    location: str | None
    size: str | None
    bedrooms: str | None
    dsq: str | None
    plot_size: str | None
    prime_location: str | None
    status: str | None
    experience: str | None


class GetProject(BaseProject):
    id: int

    class Config:
        orm_mode = True


