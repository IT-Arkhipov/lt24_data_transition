import configparser
import os

import requests

from lib import project_folder
from lib.api import api_request
from lib.definition import endpoint, settings, credentials
from lib.logger import logger

config = configparser.ConfigParser()
config.read(os.path.join(project_folder, 'config.ini'))


def get_session_id_token() -> tuple:
    logger.log.warning("Запрос session_id и token")
    body = {
        "login": credentials.login,
        "password": credentials.password
    }
    response = api_request.post(endpoint.get_token, params={}, body=body)
    api_request.assert_response(response)
    return response.json().get("session_id"), response.json().get("token")


def get_session_id() -> str:
    logger.log.warning("Запрос session_id")
    url = settings.base_url + endpoint.get_token
    params = {
        "login": credentials.login,
        "password": credentials.password
    }
    logger.log.info(f"GET: {endpoint.get_token}, params: {params}")
    response = requests.get(url, params=params)
    logger.response(response)
    api_request.assert_response(response)
    return response.json().get("session_id")


def get_token() -> str:
    logger.log.warning("Запрос token")
    params = {
        "login": credentials.login,
        "password": credentials.password
    }
    response = api_request.get(endpoint.get_token, params=params)
    api_request.assert_response(response)
    return response.json().get("token")


def get_mobile_session_id():
    logger.log.warning("Запрос mobile_session_id")
    url = settings.mobile_url
    header = {'Content-Type': 'application/json; charset=UTF-8'}
    body = {
        'TL_Mobile_LoginRequest': {
            'ClientCode': credentials.client_code,
            'DeviceInfo': 'Xiaomi Mi A2, Android:29, BuildVersion: 4763',
            'Login': credentials.mobile_login,
            'Password': credentials.mobile_password
        }
    }
    logger.log.info(f"request: POST - {url}, body: {body}")
    response = requests.post(url, headers=header, json=body)
    if response:
        logger.log_success(response=response)
        return response.json()['TL_Mobile_LoginResponse']['SessionId']
    else:
        error_text = f"Ошибка {response} при запросе mobile_session_id, response: {response.text}"
        logger.log_error(response=response, error_text=error_text)
        raise RuntimeError(error_text)
