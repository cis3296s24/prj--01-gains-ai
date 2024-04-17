from django.contrib import admin
from .models import Prompt

# Register Models Here
class PromptAdmin(admin.ModelAdmin):
    list_display = ['sentence', 'user']  # Display these fields in the admin list view

    def save_model(self, request, obj, form, change):
        """Override save_model to automatically set the user field."""
        if not obj.pk:  # If the object is being created for the first time
            obj.user = request.user
        obj.save()

admin.site.register(Prompt, PromptAdmin)