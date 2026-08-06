from datetime import datetime


# Success Response
def success_response(message: str, data=None):

    return {
        "success": True,
        "message": message,
        "data": data
    }


# Error Response
def error_response(message: str):

    return {
        "success": False,
        "message": message
    }


# Current Date & Time
def current_datetime():

    return datetime.now()


# Pagination Helper
def pagination(skip: int = 0, limit: int = 10):

    return {
        "skip": skip,
        "limit": limit
    }
