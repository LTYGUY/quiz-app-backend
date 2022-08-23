from src.helpers import error_response, respond_with_data
from src.model import Quizzes


def create(event, _):

    if 'DeviceID' not in event:
        return error_response(422, 'DeviceID is not found')

    elif 'QuizList' not in event:
        return error_response(422, 'No quizzes were found.')

    elif not event['QuizList']['QuizName']:
        return error_response(422, 'No quiz name was found.')

    quiz = Quizzes(
        device_id=event['DeviceID'],
        quiz_name=event['QuizList'],
        modified_time=event['Timestamp']
    )

    quiz.save()
    return respond_with_data(201, quiz)