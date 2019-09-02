from django.contrib import admin
from .models import employees
from .models import departaments
from .models import titles
from .models import salaries
from .models import dept_emp
from .models import dept_manager

admin.site.register(employees)
admin.site.register(departaments)
admin.site.register(titles)
admin.site.register(salaries)
admin.site.register(dept_emp)
admin.site.register(dept_manager)


# Register your models here.
