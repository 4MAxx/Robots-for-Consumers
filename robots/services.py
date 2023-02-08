
def get_valid_robot_models():
    ''' Список производимых моделей можно получать откуда угодно'''
    AVAILABLE_MODELS = ['R1', 'R2', 'R5', 'S1', 'S2', 'S3']
    return AVAILABLE_MODELS


def is_valid_robot_model(model):
    return model in get_valid_robot_models()