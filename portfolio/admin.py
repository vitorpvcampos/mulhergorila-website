from django.contrib import admin

from .models import Project, ProjectImages, Category


class ProjectImagesInline(admin.StackedInline):
    model = ProjectImages
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [
        ProjectImagesInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
