from django.http import (
    JsonResponse,
)


def version(request):
    return JsonResponse(
        {
            'message': 'This is Healthyhealth API',
        },
    )
