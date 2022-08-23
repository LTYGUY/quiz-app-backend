from json import dumps

from pynamodb.exceptions import DoesNotExist

from src.helpers import ResponseType, error_response, response
from src.model import Quizzes


def get(event: ResponseType, _) -> ResponseType:

    try:
        print(event)
        quizzes = Quizzes.get(hash_key=event['rawPath'])

    except (DoesNotExist, KeyError):
        return error_response(404, 'Quiz not found')

    return {
        'statusCode': 200,
        'body': dumps(dict(quizzes))
    }