import os
import time

import requests

from typing import Union
from requests import Response
from lib import project_folder, dataset
from lib.definition import Endpoints, settings
from lib.logger import logger


def assert_response(response: Response):
    expected_code = 200
    err_msg = f"Запрос завершился с кодом ошибки {response.status_code} - {response.text}"
    try:
        assert response.status_code == expected_code
    except AssertionError as e:
        logger.raised_error(e, err_msg)
        # pytest.fail(error_text)
        raise Exception(err_msg[:300])


def post(endpoint: Union[Endpoints, str], params: dict, body: dict) -> Response:
    headers = {'SessionId': settings.session_id}
    url = settings.base_url + endpoint
    logger.log.info(f"POST: {endpoint}, headers: {headers}, params: {params}, json: {body}")
    response = requests.post(url, headers=headers, params=params, json=body)
    logger.response(response)
    return response


def post_tries(endpoint: Union[Endpoints, str], params: dict, body: dict) -> Response:
    response = Response()
    headers = {'SessionId': settings.session_id}
    url = settings.base_url + endpoint
    logger.log.info(f"POST: {endpoint}, headers: {headers}, params: {params}, json: {body}")
    import requests.exceptions as re
    for _ in range(3):
        try:
            response = requests.post(url, headers=headers, params=params, json=body)
            if response.status_code >= 500:
                response.raise_for_status()
            logger.response(response)
            return response
        except (re.HTTPError, re.ConnectionError, re.Timeout) as error:
            logger.log.warning(error)
        time.sleep(10)
    else:
        try:
            response = requests.post(url, headers=headers, params=params, json=body)
            response.raise_for_status()
            logger.response(response)
            return response
        except (re.HTTPError, re.ConnectionError, re.Timeout) as error:
            if response.status_code >= 500:
                logger.raised_error(error)
                raise Exception(error[:300])


def post_file(endpoint: Endpoints, params: dict, file_name: str) -> Response:
    file_path = os.path.join(project_folder, dataset.RESOURCE_FOLDER, file_name)
    headers = {
        'SessionId': settings.session_id
    }
    url = settings.base_url + endpoint
    logger.log.info(f"POST: {endpoint}, headers: {headers}, params: {params}, file_path: {file_path}")
    with open(file_path, 'rb') as f:
        file = {'uploadedFile': f}
        response = requests.post(url, headers=headers, params=params, files=file, timeout=10)
        logger.response(response)
    return response


def delete(endpoint: Union[Endpoints, str], params: dict = None) -> Response:
    headers = {'SessionId': settings.session_id}
    url = settings.base_url + endpoint
    logger.log.info(f"DELETE: {endpoint}, headers: {headers}, params: {params}")
    response = requests.delete(url, headers=headers, params=params)
    logger.response(response)
    return response


def get(endpoint: Union[Endpoints, str], params: dict = None) -> Response:
    headers = {'SessionId': settings.session_id}
    url = settings.base_url + endpoint
    logger.log.info(f"GET: {endpoint}, headers: {headers}, params: {params}")
    response = requests.get(url, headers=headers, params=params)
    logger.response(response)
    return response


def head(url: str) -> Response:
    logger.log.info(f"request: HEAD - {url}")
    response = requests.head(url)
    logger.response(response)
    return response


def post_file_chunk(photo_id: str, offset: int, chunk: bytes) -> Response:
    header = {'Content-Type': 'application/octet-stream'}
    chunk_url = f"{settings.api_url}/TL_Mobile_UploadFileChunkRequest?uid={photo_id}&offset={offset}"
    logger.log.info("Отправка chunk файла на сервер")
    logger.log.info(f"request: POST - {chunk_url} + chunks_size: {len(chunk)}")
    response = requests.post(url=chunk_url, headers=header, data=chunk)
    logger.response(response)
    return response


def old_api_post_file_chunk(chunk_url: str, chunk: bytes) -> Response:
    header = {
        'Content-Type': 'application/octet-stream',
        'Content-Length': str(len(chunk))
    }
    logger.log.info("Отправка chunk файла на сервер")
    logger.log.info(f"request: POST - {chunk_url} + chunks_size: {len(chunk)}")
    response = requests.post(url=chunk_url, headers=header, data=chunk)
    logger.response(response)
    return response


def put(endpoint: Union[Endpoints, str], params: dict, body: dict) -> Response:
    headers = {'SessionId': settings.session_id}
    url = settings.base_url + endpoint
    logger.log.info(f"PUT: {endpoint}, headers: {headers}, params: {params}, json: {body}")
    response = requests.put(url, headers=headers, params=params, json=body)
    logger.response(response)
    return response
