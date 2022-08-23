from json import loads

from src.helpers import error_response, respond_with_data
from src.model import Quiz


def create(event, context):

    data = loads(event['body'])
    print(data)
    return

    if 'quiz' not in data:
        return error_response(422, 'No quiz was found.')

    elif 'QuizName' not in data:
        return error_response(422, 'No quiz name was found.')

    elif not data['quiz']:
        return error_response(422, 'Quiz has no content.')

    elif not data['quiz_name']:
        return error_response(422, 'Quiz name has no content.')

    quiz = Quiz(
        quiz_name=data['QuizName'],
        questions=data['Question']
    )

    quiz.save()
    return respond_with_data(201, quiz)