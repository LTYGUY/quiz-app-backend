from json import loads
from uuid import uuid1

from pynamodb.exceptions import DoesNotExist

from quizzes.helpers import error_response, respond_with_data
from quizzes.model import Quizzes


def create(event, context):

    data = loads(event['body'])

    if 'quiz' not in data:
        return error_response(422, 'No quiz was found.')

    elif 'quiz_name' not in data:
        return error_response(422, 'No quiz name was found.')

    elif not data['quiz']:
        return error_response(422, 'Quiz has no content.')

    elif not data['quiz_name']:
        return error_response(422, 'Quiz name has no content.')

    quiz = Quizzes(
        id=uuid1(),
        quiz_name=data['quiz_name'],
        quiz=data['quiz']
    )

    quiz.save()
    return respond_with_data(201, quiz)