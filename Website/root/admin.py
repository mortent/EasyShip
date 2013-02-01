from django.contrib import admin
from root.models import *

#Register our objects with the Django admin
admin.site.register(ServiceLevel)
admin.site.register(Zone)
admin.site.register(Rate)