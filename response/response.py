from validator_collection import validators, checkers, errors

try:
    email_add = validators.email(input("What's your email address? "))

except errors.EmptyValueError:
    print('Invalid')

except errors.InvalidEmailError:
    print('Invalid')
else:
    is_valid_email = checkers.is_email(email_add)
    if is_valid_email:
        print('Valid')
    else:
        print('Invalid')