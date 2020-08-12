from django.db import models
from django.template.defaultfilters import slugify


class Skills(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    live_url = models.CharField(max_length=100, blank=True, default="")
    repo_url = models.CharField(max_length=100, blank=True, default="")
    skills_project = models.ManyToManyField(Skills)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)


class ProjectImages(models.Model):
    project = models.ForeignKey(Project, related_name='imagenes', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name + self.image.path

