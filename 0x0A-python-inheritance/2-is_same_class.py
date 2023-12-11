def is_same_class(obj, a_class):
    """
    Checks if object is exactly instance of a class
    Args:
        obj: object being checked
        a_class: the specified class

    Returns:
        True if obj is exactly instance of a_class else False
    """
    return type(obj) is a_class
