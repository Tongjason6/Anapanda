from django.contrib import admin
from .models import Circle, Project, Task, RoleKummitment, Kummitment, Role

admin.site.register([Circle, Project, Task, RoleKummitment, Kummitment, Role])

