
from rest_framework.test import APITestCase
from django.urls import reverse

from core.tests.factories.organization import OrganizationFactory


class OrganizationViewSetTest(APITestCase):
    list_view = 'public:organization-list'

    def test_organization_list_view(self):
        o1, o2 = OrganizationFactory.create_batch(size=2)

        response = self.client.get(reverse(self.list_view))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_organization_list_view_with_empty_name_filter(self):
        o1 = OrganizationFactory.create(name='healthy-anaconda')  # noqa:841

        response = self.client.get(
            reverse(self.list_view),
            data={'name': ''},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_organization_list_view_with_name_filter(self):
        o1 = OrganizationFactory.create(name='healthy-anaconda')  # noqa:841
        o2 = OrganizationFactory.create(name='healthy-health')  # noqa:841
        o3 = OrganizationFactory.create(name='healthy-org')  # noqa:841
        o4 = OrganizationFactory.create(name='google')  # noqa:841

        response = self.client.get(
            reverse(self.list_view),
            data={'name': 'healthy'},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
