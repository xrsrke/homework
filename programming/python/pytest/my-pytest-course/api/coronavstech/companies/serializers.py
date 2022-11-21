from rest_framework import serializers
from api.coronavstech.companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "status", "application_link", "last_update", "notes"]
