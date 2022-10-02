from django.contrib import admin

from api.coronavstech.companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
