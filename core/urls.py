from django.urls import include, path
from rest_framework.routers import SimpleRouter
from core.views import OrganizationViewSet


router = SimpleRouter()

router.register(
    'organization',
    OrganizationViewSet,
    basename='organization',
)

urlpatterns = [
    path('', include(router.urls)),
]
