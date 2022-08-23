from json import loads

from src.helpers import ResponseType, error_response, response
from src.model import Question, Quiz, Quizzes


def create(event: ResponseType, _) -> ResponseType:

    try:
        data = loads(event['body'])

    except KeyError:
        return error_response(422, 'No body provided.')

    if 'DeviceID' not in data:
        return error_response(422, 'DeviceID is not found')

    elif 'QuizList' not in data:
        return error_response(422, 'No quizzes were found.')

    quizzes = Quizzes(
        device_id=data['DeviceID'],
        modified_time=data['Timestamp'],
        quizzes=data['QuizList']
    )

    quizzes.save()
    return response(201, f"Quizzes created for {data['DeviceID']}")