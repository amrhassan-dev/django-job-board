from django.db import models





JOB_TYPE = [
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
]





# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description =models.TextField(max_length=1000)
    published_at =models.DateTimeField(auto_now=True)
    vacancy =models.IntegerField(default=1)
    salary =models.IntegerField(default=0)
    experince=models.IntegerField(default=1)
    


    class Meta:
        

        verbose_name = 'job'
        verbose_name_plural = 'jobs'

    def __str__(self):
        return self.title


