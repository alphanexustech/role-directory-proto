def merge_role_json(files):
    merged = {}

    for i in files:
        merged.update(i)

    return merged
