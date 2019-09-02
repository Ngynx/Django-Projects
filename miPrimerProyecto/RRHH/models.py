from django.db import models

class employees(models.Model):
	GENDER_FEMALE = 'F'
	GENDER_MALE = 'M'
	GENDER_CHOICES = (
           (GENDER_FEMALE, 'Female'),
           (GENDER_MALE, 'Male'),
        )

	emp_no = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=255, blank=False, null=False)
	last_name = models.CharField(max_length=255, blank=False, null=False)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	hire_date=models.DateTimeField('fecha de contrato')

	def __str__(self):
	    return self.first_name


class salaries(models.Model):
	salary = models.IntegerField(blank=False, null=False)
	from_date = models.DateTimeField('fecha de')
	to_date = models.DateTimeField('fecha hasta')
	emp_no = models.ForeignKey(employees, on_delete=models.CASCADE)

class titles(models.Model):
	title = models.CharField(max_length=50, blank=False, null=False)
	from_date = models.DateTimeField('fecha de')
	to_date=models.DateTimeField('fecha hasta')
	emp_no = models.ForeignKey(employees, on_delete=models.CASCADE)

	class Meta:
	    verbose_name='titles'
	    verbose_name_plural='title'
	    ordering=['title']

	def __str__(self):
	    return self.title

class departaments(models.Model):
	dept_no =models.AutoField(primary_key=True, blank=False, null=False)
	dept_name = models.CharField(max_length=255, blank=False, null=False)

	class Meta:
	    verbose_name='departament'
	    verbose_name_plural='departaments'
	    ordering=['dept_name']

	def __str__(self):
	    return self.dept_name

class dept_emp (models.Model):
	dept_no = models.ForeignKey(departaments, on_delete=models.CASCADE)
	from_date=models.DateTimeField('fecha de')
	to_date=models.DateTimeField('fecha hasta')
	emp_no = models.ForeignKey(employees, on_delete=models.CASCADE)

class dept_manager(models.Model):
	from_date=models.DateTimeField('fecha de')
	to_date=models.DateTimeField('fecha hasta')
	dept_no = models.ForeignKey(departaments, on_delete=models.CASCADE)
	emp_no = models.ForeignKey(employees, on_delete=models.CASCADE)

