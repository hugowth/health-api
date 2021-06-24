
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from core.serializers import OrganizationSerializer
from core.models import Organization
from core.filters import OrganizationFilter
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiExample,
)


@extend_schema_view(
    list=extend_schema(
        operation_id='List organizations',
        auth=None,
        parameters=[OrganizationSerializer],
        description='Lists all organizations, in the order that they were created on Server.',  # noqa
        examples=[
            OpenApiExample(
                name='Filter name=healthy',
                media_type='application/json',
                value=[
                    {
                        "id": 1,
                        "name": "healthy-anaconda",
                        "create_date": "2021-06-13T03:32:46.974959Z",
                        "update_date": "2021-06-13T03:32:46.975660Z"
                    },
                    {
                        "id": 2,
                        "name": "healthy-health",
                        "create_date": "2021-06-13T03:33:16.237837Z",
                        "update_date": "2021-06-13T03:33:16.238405Z"
                    },
                    {
                        "id": 3,
                        "name": "healthy-org",
                        "create_date": "2021-06-13T03:33:20.385233Z",
                        "update_date": "2021-06-13T03:33:20.386178Z"
                    }
                ],
                description='Filter with empty string',
            ),
            OpenApiExample(
                name='Without Filter',
                media_type='application/json',
                value=[
                    {
                        "id": 4,
                        "name": "amazon",
                        "create_date": "2021-06-13T03:34:34.475823Z",
                        "update_date": "2021-06-13T03:34:34.476562Z"
                    }, {
                        "id": 5,
                        "name": "google",
                        "create_date": "2021-06-13T03:34:39.253105Z",
                        "update_date": "2021-06-13T03:34:39.254055Z"
                    }, {
                        "id": 1,
                        "name": "healthy-anaconda",
                        "create_date": "2021-06-13T03:32:46.974959Z",
                        "update_date": "2021-06-13T03:32:46.975660Z"
                    },
                    {
                        "id": 2,
                        "name": "healthy-health",
                        "create_date": "2021-06-13T03:33:16.237837Z",
                        "update_date": "2021-06-13T03:33:16.238405Z"
                    }, {
                        "id": 3,
                        "name": "healthy-org",
                        "create_date": "2021-06-13T03:33:20.385233Z",
                        "update_date": "2021-06-13T03:33:20.386178Z"
                    },
                ],
                description='Without Filter',
            ),
            OpenApiExample(
                name='Filter with empty string',
                media_type='application/json',
                value=[
                    {
                        "id": 4,
                        "name": "amazon",
                        "create_date": "2021-06-13T03:34:34.475823Z",
                        "update_date": "2021-06-13T03:34:34.476562Z"
                    }, {
                        "id": 5,
                        "name": "google",
                        "create_date": "2021-06-13T03:34:39.253105Z",
                        "update_date": "2021-06-13T03:34:39.254055Z"
                    }, {
                        "id": 1,
                        "name": "healthy-anaconda",
                        "create_date": "2021-06-13T03:32:46.974959Z",
                        "update_date": "2021-06-13T03:32:46.975660Z"
                    },
                    {
                        "id": 2,
                        "name": "healthy-health",
                        "create_date": "2021-06-13T03:33:16.237837Z",
                        "update_date": "2021-06-13T03:33:16.238405Z"
                    }, {
                        "id": 3,
                        "name": "healthy-org",
                        "create_date": "2021-06-13T03:33:20.385233Z",
                        "update_date": "2021-06-13T03:33:20.386178Z"
                    },
                ],
                description='Filter with empty string',
            ),
        ],
    )
)
class OrganizationViewSet(GenericViewSet, ListModelMixin):
    authentication_classes = []
    filterset_class = OrganizationFilter
    serializer_class = OrganizationSerializer
    search_fields = [
        'name',
    ]

    def get_queryset(self):
        queryset = Organization.objects.all()

        return queryset
