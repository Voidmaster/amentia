from django.contrib import admin

from clientes.models import Work, Category, Client, Service

admin.site.register(Work)
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Service)