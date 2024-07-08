from __future__ import absolute_import, unicode_literals

import os
import base64
import datetime
import json
import uuid

import requests
from requests.auth import HTTPBasicAuth
from fastapi import WebSocketException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from ..configs.database_config import SessionLocal
from dotenv import load_dotenv

load_dotenv()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ResponseModel(BaseModel):
    success: bool = False
    data: dict | None
    message: str | None

    class Config:
        orm_mode = True

# consumer_key = os.getenv('SAFARICOM_CONSUMER_KEY')
# consumer_secret = os.getenv('SAFARICOM_CONSUMER_SECRET')
# api_UR= os.getenv('api_UR')


class MpesaC2BKeys:
    consumer_key =os.environ['consumer_key']
    consumer_secret = os.environ['consumer_secret']
    api_URL = (
        "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    )
def generate_token():
    mpesa_access_token = json.loads(
        (
            requests.get(
                MpesaC2BKeys.api_URL,
                auth=HTTPBasicAuth(
                    MpesaC2BKeys.consumer_key, MpesaC2BKeys.consumer_secret
                ),
            )
        ).text
    )
    token = mpesa_access_token["access_token"]

    return token



# callable for mpesa transactions prerequisites - DO NOT TOUCH
class LipanaMpesaPW:
    time_of_payment = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    short_code = os.environ['short_code']
    safaricom_passkey = os.environ['safaricom_passkey']
    concatenated_data = short_code + safaricom_passkey + time_of_payment
    online_password = base64.b64encode(concatenated_data.encode())
    decode_password = online_password.decode("utf-8")