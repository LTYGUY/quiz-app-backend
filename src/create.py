from src.helpers import ResponseType, error_response, respond_with_data
from src.model import Quizzes


def create(event: ResponseType, _) -> ResponseType:

    data = event['body']
    print(data)
    print(type(data))

    if 'DeviceID' not in data:
        return error_response(422, 'DeviceID is not found')

    elif 'QuizList' not in data:
        return error_response(422, 'No quizzes were found.')

    quizzes = Quizzes(
        device_id=data['DeviceID'],
        quizzes=data['QuizList'],
        modified_time=data['Timestamp']
    )

    quizzes.save()
    return respond_with_data(201, quizzes)