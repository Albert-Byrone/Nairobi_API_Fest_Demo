from sqlalchemy.orm import Session

from .models import Project
from .schemas import CreateProject, UpdateProject, GetProject


def create_project_crud(db: Session, project: CreateProject):
    print("=========prject", project)
    project_instance = Project(title=project.title, description=project.description, image=project.image, location=project.location, size=project.size, bedrooms=project.bedrooms, dsq=project.dsq, plot_size=project.plot_size, prime_location=project.prime_location,  status=project.status, experience=project.experience)
    db.add(project_instance)
    db.commit()
    db.refresh(project_instance)
    return GetProject(id=project_instance.id, title=project_instance.title, description=project_instance.description, image=project.image, location=project.location, size=project.size, bedrooms=project.bedrooms, dsq=project.dsq, plot_size=project.plot_size, prime_location=project.prime_location,  status=project.status, experience=project.experience)


def get_projects_crud(db: Session):
    projects = db.query(Project).all()
    print("====", projects)
    return [GetProject(
        id=project.id,
        title=project.title,
        image=project.image,
        description=project.description,
        location=project.location,
        size=project.size,
        bedrooms=project.bedrooms,
        dsq=project.dsq,
        plot_size=project.plot_size,
        prime_location=project.prime_location,
        status=project.status,
        experience=project.experience) for project in projects]


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
# prject title='Luxury Residential Estate - Tatu City, Kiambu County, Kenya' image='https://unsplash.com/photos/a-black-car-driving-down-a-street-next-to-tall-buildings-sKzyF_GN7PQ' description='Nestled within the vibrant community of Tatu City in Kiambu County, Kenya, our Luxury Residential Estate stands as a testament to unparalleled comfort and sophistication. This magnificent estate spans 550 square meters and rests gracefully on a sprawling half-acre plot, offering residents a harmonious blend of space, privacy, and luxury living' location='Tatu City, Kiambu County, Kenya' size='550 square meters' bedrooms='Four Bedrooms with Guest Wing: Designed for spacious living, our estate boasts four generously sized bedrooms, each meticulously crafted to provide comfort and tranquility. Additionally, a separate guest wing ensures privacy for visitors and extended family members.' dsq='Expansive Outdoor Area: Embrace the serene beauty of nature in your own backyard. The estate features a lush landscaped garden spanning half an acre, providing ample space for outdoor activities, relaxation, and entertainment.' plot_size='Inviting Poolside Retreat: Escape the Kenyan heat and indulge in leisurely moments by the sparkling poolside. Our estate offers a private swimming pool, perfect for refreshing dips and memorable gatherings with loved ones.' prime_location="ituated within the esteemed Tatu City development, our estate enjoys the convenience of urban amenities amidst a serene and picturesque setting. Kiambu County's rich cultural heritage and natural beauty provide the perfect backdrop for luxurious living." status='Elevate your lifestyle and experience the epitome of luxury living at our exclusive Residential Estate in Tatu City, Kiambu County, Kenya. Contact us today to learn more about this prestigious property and secure your slice of paradise.' experience='Elevate your lifestyle and experience the epitome of luxury living at our exclusive Residential Estate in Tatu City, Kiambu County, Kenya. Contact us today to learn more about this prestigious property and secure your slice of paradise.'
