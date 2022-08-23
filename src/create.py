from json import loads

from src.helpers import ResponseType, error_response, respond_with_data
from src.model import Question, Quiz, Quizzes


def create(event: ResponseType, _) -> ResponseType:

    try:
        data = loads(event['body'])

    except KeyError:
        return error_response(422, 'No body provided.')

    if 'DeviceID' not in data:
        return error_response(422, 'DeviceID is not found')

    elif 'QuizList' not in data:
        return error_response(422, 'No quizzes were found.')

    quiz_list = []

    for quiz in data['QuizList']:
        question_list = []

        for question in quiz['QuestionList']:
            question = Question(
                question=question['QuizQuestion'],
                answer_index=question['CorrectOptionIndex'],
                options=question['OptionList'],
            )

            question_list.append(question)

        quiz = Quiz(
            quiz_name=quiz['QuizName'],
            questions=question_list,
        )

        quiz_list.append(quiz)

    quizzes = Quizzes(
        device_id=data.get('DeviceID'),
        quizzes=quiz_list,
        modified_time=data.get('Timestamp')
    )

    quizzes.save()
    return respond_with_data(201, quizzes)