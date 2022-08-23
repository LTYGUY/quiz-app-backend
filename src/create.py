from src.helpers import error_response, respond_with_data
from src.model import Quizzes


def create(event, _):

    data = event['body']

    if 'DeviceID' not in data:
        return error_response(422, 'DeviceID is not found')

    elif 'QuizList' not in data:
        return error_response(422, 'No quizzes were found.')

    elif not data['QuizList']['QuizName']:
        return error_response(422, 'No quiz name was found.')

    quiz = Quizzes(
        device_id=data['DeviceID'],
        quiz_name=data['QuizList'],
        modified_time=data['Timestamp']
    )

    quiz.save()
    return respond_with_data(201, quiz)