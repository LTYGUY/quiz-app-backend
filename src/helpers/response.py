from json import dumps

ResponseType = dict[str, any]

def response(status, message) -> ResponseType:

    return {
        'status': status,
        'body': dumps({
            'message': message
        })
    }

def respond_with_data(status, data) -> ResponseType:

    return {
        'status': status,
        'body': dumps(dict(data))
    }

def error_response(status, error_message) -> ResponseType:

    return {
        'status': status,
        'body': dumps({
            'error_message': error_message
        })
    }