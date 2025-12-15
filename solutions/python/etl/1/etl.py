def transform(legacy_data):
    data = {}
    for key,value in legacy_data.items():
        for character in value:
            data[character.lower()] = key

    return data