from json import dumps, loads

from src.helpers import ResponseType, error_response, response
from src.model import Quizzes


def create(event: ResponseType, _) -> ResponseType:

    try:
        data = loads(event['body'])

    except KeyError:
        return error_response(422, 'No body provided.')

    if 'DeviceID' not in data:
        return error_response(422, 'DeviceID is not found')

    if 'QuizList' not in data:
        return error_response(422, 'No quizzes were found.')

    device_id: int = data['DeviceID']
    del data['DeviceID']

    quizzes = Quizzes(
        device_id=device_id,
        quizzes=dumps(data)
    )

    quizzes.save()
    return response(201, f"Quizzes created for {device_id}")
