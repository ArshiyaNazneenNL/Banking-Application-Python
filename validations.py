def validate_mobile_number(mobile):
    return len(mobile) == 10 and mobile.isdigit()
