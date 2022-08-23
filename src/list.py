from json import dumps

from src.helpers import respond_with_data
from src.model import Quiz


def list(event, context):

    return {
        'statusCode': 200,
        'body': dumps({
            'quizzes': [dict(result) for result in Quiz.scan()]
        }),
    }