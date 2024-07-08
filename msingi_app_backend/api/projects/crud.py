from sqlalchemy.orm import Session

from .models import Project, Development, Payment
from .schemas import CreateProject, UpdateProject, GetProject, CreateDevelopment, UpdateDevelopment, GetDevelopment, GetPayment,CreatePayment


def create_project_crud(db: Session, project: CreateProject):
    print("=========prject", project)
    project_instance = Project(title=project.title, description=project.description, image=project.image, location=project.location, size=project.size, bedrooms=project.bedrooms, dsq=project.dsq, plot_size=project.plot_size, prime_location=project.prime_location,  status=project.status, experience=project.experience)
    db.add(project_instance)
    db.commit()
    db.refresh(project_instance)
    return GetProject(id=project_instance.id, title=project_instance.title, description=project_instance.description, image=project.image, location=project.location, size=project.size, bedrooms=project.bedrooms, dsq=project.dsq, plot_size=project.plot_size, prime_location=project.prime_location,  status=project.status, experience=project.experience)

def get_project_crud(db: Session, project_id):
    return  db.query(Project).filter(Project.id == project_id).first()


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



# Development CreateDevelopment, UpdateDevelopment, GetDevelopment,

def create_developement_crud(db: Session, developement: CreateDevelopment):
    print("=========prject", developement)
    developement_instance = Development(title=developement.title, description=developement.description, image=developement.image, location=developement.location, size=developement.size, bedrooms=developement.bedrooms, dsq=developement.dsq, plot_size=developement.plot_size, prime_location=developement.prime_location,  status=developement.status, experience=developement.experience)
    db.add(developement_instance)
    db.commit()
    db.refresh(developement_instance)
    return GetProject(id=developement_instance.id, title=developement_instance.title, description=developement_instance.description, image=developement_instance.image, location=developement_instance.location, size=developement_instance.size, bedrooms=developement_instance.bedrooms, dsq=developement_instance.dsq, plot_size=developement_instance.plot_size, prime_location=developement_instance.prime_location,  status=developement_instance.status, experience=developement_instance.experience)

def get_development_crud(db: Session, development_id):
    return  db.query(Development).filter(Development.id == development_id).first()


def get_developments_crud(db: Session):
    developments = db.query(Development).all()
    print("====", developments)
    return [GetDevelopment(
        id=development.id,
        title=development.title,
        image=development.image,
        description=development.description,
        location=development.location,
        size=development.size,
        bedrooms=development.bedrooms,
        dsq=development.dsq,
        plot_size=development.plot_size,
        prime_location=development.prime_location,
        status=development.status,
        experience=development.experience) for development in developments]


def update_development_crud(db: Session, development: UpdateDevelopment, development_id):
    development_instance = db.query(Development).filter(Development.id == development_id).first()
    if development.title:
        development_instance.title = development.title

    if development.description:
        development_instance.description = development.description
    db.add(development_instance)
    db.commit()
    db.refresh(development_instance)
    return GetDevelopment(id=development_instance.id, title=development_instance.title, description=development_instance.description)




# def create_payment_crud(db: Session, payment: CreatePayment):
#     print("=========prject", payment)
#     payment_instance = Payment(phone_number=payment.title, amount=payment.description)
#     db.add(payment_instance)
#     db.commit()
#     db.refresh(payment_instance)
#     return GetPayment(id=payment_instance.id,phone_number=payment_instance.title, amount=payment_instance.description)

from ..utils import generate_token, LipanaMpesaPW
def create_payment_crud(db: Session, payment: CreatePayment):
    try:

        access_token = generate_token()
        api_url = "https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        domain = request.META["HTTP_HOST"]
        req = {
            "BusinessShortCode": LipanaMpesaPW.short_code,
            "Password": LipanaMpesaPW.decode_password,
            "Timestamp": LipanaMpesaPW.time_of_payment,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": payment.amount,
            "PartyA": payment.phone_number,
            "PartyB": LipanaMpesaPW.short_code,
            "PhoneNumber": payment.phone_number,
            "CallBackURL": "https://" + domain + "/c2b/callback/" + str(user_uuid),
            "AccountReference": "Pessafy",
            "TransactionDesc": transaction_desc,
        }
        # logger.debug(requests.post(api_url, json=req, headers=headers))
        print(requests.post(api_url, json=req, headers=headers))
    except Exception as e:
        # logger.debug(e)
        print("Error", e)


# def mpesa_request(request, number, user_uuid, transaction_desc, amount):









