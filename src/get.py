from json import dumps, loads

from pynamodb.exceptions import DoesNotExist

from src.helpers import ResponseType, error_response
from src.model import Quizzes


def get(event: ResponseType, _) -> ResponseType:

    try:
        quizzes = dict(Quizzes.get(hash_key=event['pathParameters']['device_id']))

    except (DoesNotExist, KeyError):
        return error_response(404, 'Quiz not found')
    
    quizzes["quizzes"] = loads(quizzes["quizzes"])

    return {
        'statusCode': 200,
        'body': dumps(quizzes)
    }
