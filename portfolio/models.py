from django.db import models
from django.utils.text import slugify

from core.models import TimeStampedModel, Active


class Project(TimeStampedModel, Active):
    title = models.CharField(max_length=255)
    client = models.CharField(max_length=30, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="slug",
                            help_text="Preenchido automaticamente, não editar.",
                            null=True,
                            blank=True, )
    description = models.TextField()
    image = models.ImageField(
        verbose_name="Imagem",
        upload_to='projetos/',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('title', 'slug', 'description')
        verbose_name = 'projeto'
        verbose_name_plural = 'projetos'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImages(TimeStampedModel, Active):
    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
    order = models.PositiveIntegerField(default=0)
    image = models.ImageField(
        verbose_name="Imagem",
        upload_to='projetos/',
    )

    class Meta:
        ordering = ('order',)
        verbose_name = 'imagem extra'
        verbose_name_plural = 'imagens extras'


class Category(TimeStampedModel, Active):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name
