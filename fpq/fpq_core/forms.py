def attributes(identifier: str) -> dict:
    if not identifier:
        raise ValueError('The tag identifier can not be empty.')

    return {'id': identifier, 'class': 'form-control'}
