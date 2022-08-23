from pynamodb.exceptions import DoesNotExist

from src.helpers import error_response, respond_with_data
from src.model import Quizzes


def get(event, context):

    try:
        quiz = Quizzes.get(event['path']['id'])

    except DoesNotExist:
        return error_response(404, 'Quiz not found')

    return respond_with_data(200, quiz)