from django.contrib import admin
# from .models import allusuarios
# from django.contrib.auth.models import Group

# from django.contrib.auth import get_user_model

# User = get_user_model()
     
    
# class PerfilAdmin(admin.ModelAdmin):
   
#     list_display = ['user', 'cui', 'user_groups']   
#     search_fields = ['user__username', 'user__groups__name'] 
#     list_filter = ['user__groups']
#     ordering = ['user']   
        
#     def get_queryset(self, request):
#         return super().get_queryset(request).prefetch_related('user__groups')
    
#     def user_groups(self, obj):
#         return ", ".join([group.name for group in obj.user.groups.all().order_by('name')])
    
#     user_groups.short_description = 'Groups'
    
# admin.site.register(allusuarios, PerfilAdmin)