from pynamodb.exceptions import DoesNotExist

from src.helpers import ResponseType, error_response, response
from src.model import Quizzes


def get(event: ResponseType, _) -> ResponseType:

    try:
        quiz = Quizzes.get(event['path']['id'])

    except DoesNotExist:
        return error_response(404, 'Quiz not found')

    return response(200, "Quiz found")