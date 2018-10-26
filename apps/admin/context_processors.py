from project.settings.settings import ENVIRONMENT_NAME, ENVIRONMENT_COLOR

def from_settings(request):
    return {
        'ENVIRONMENT_NAME': ENVIRONMENT_NAME,
        'ENVIRONMENT_COLOR': ENVIRONMENT_COLOR,
    }