from pynamodb.exceptions import DeleteError, DoesNotExist

from src.helpers import error_response, response
from src.model import Quiz


def delete(event, context):

    try:
        quiz = Quiz.get(hash_key=event['path']['id'])

    except DoesNotExist:
        return error_response(404, 'Quiz not found.')

    try:
        quiz.delete()

    except DeleteError:
        return error_response(400, 'Could not delete quiz.')

    return response(204, 'Quiz deleted.')