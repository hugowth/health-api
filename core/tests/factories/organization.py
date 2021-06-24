import uuid
import factory

from core.models import Organization


class OrganizationFactory(factory.django.DjangoModelFactory):
    name = 'health' + str(uuid.uuid4)

    class Meta:
        model = Organization
