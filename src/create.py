from json import loads

from src.helpers import ResponseType, error_response, respond_with_data
from src.model import Quizzes


def create(event: ResponseType, _) -> ResponseType:

    data = loads(event.get('body'))

    if not data:
        return error_response(422, 'No body provided.')

    elif 'DeviceID' not in data:
        return error_response(422, 'DeviceID is not found')

    elif 'QuizList' not in data:
        return error_response(422, 'No quizzes were found.')

    quizzes = Quizzes(
        device_id=data.get('DeviceID'),
        quizzes=data.get('QuizList'),
        modified_time=data.get('Timestamp')
    )

    quizzes.save()
    return respond_with_data(201, quizzes)