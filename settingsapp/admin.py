from django.contrib import admin
from django.http import HttpRequest

from settingsapp.models import About, Social_links

# Register your models here.


class ABoutAdmin(admin.ModelAdmin):

    def has_add_permission(self, request: HttpRequest) -> bool:
        return About.objects.all().count() == 0


admin.site.register(About, ABoutAdmin)
admin.site.register(Social_links)