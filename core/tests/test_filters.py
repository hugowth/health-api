from django.test import TestCase
from core.filters import OrganizationFilter
from core.tests.factories.organization import OrganizationFactory
from core.models import Organization


class OrganizationFilterTest(TestCase):
    def test_can_filter_by_status(self):
        organization1 = OrganizationFactory.create(name='healthy-anaconda')
        organization2 = OrganizationFactory.create(name='healthy-health')
        organization3 = OrganizationFactory.create(name='healthy-org')
        organization4 = OrganizationFactory.create(name='google')

        qs = Organization.objects.all()
        f = OrganizationFilter(
            data={'name': 'healthy'},
            queryset=qs,
        )
        self.assertEqual(f.qs.count(), 3)
        self.assertCountEqual(
            f.qs.all(), [organization1, organization2, organization3])

        qs = Organization.objects.all()
        f = OrganizationFilter(
            data={'name': 'google'},
            queryset=qs,
        )
        self.assertEqual(f.qs.count(), 1)
        self.assertCountEqual(
            f.qs.all(), [organization4])
