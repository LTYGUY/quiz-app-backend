from json import dumps

from quizzes.helpers import respond_with_data
from quizzes.model import Quizzes


def list(event, context):

    return {
        'statusCode': 200,
        'body': dumps({
            'quizzes': [dict(result) for result in Quizzes.scan()]
        }),
    }