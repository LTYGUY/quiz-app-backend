from json import dumps


def response(status, message):

    return {
        'status': status,
        'body': dumps({
            'message': message
        })
    }

def respond_with_data(status, data):

    return {
        'status': status,
        'body': dumps(dict(data))
    }

def error_response(status, error_message):

    return {
        'status': status,
        'body': dumps({
            'error_message': error_message
        })
    }