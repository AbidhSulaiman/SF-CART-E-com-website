from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserDetail

# # Inline to display UserDetails on the User admin page
# class UserDetailsInline(admin.StackedInline):
#     model = UserDetail
#     can_delete = False

# # Extend the UserAdmin to include UserDetails
# class CustomUserAdmin(UserAdmin):
#     inlines = (UserDetailsInline,)

# # Unregister the original User admin and register the customized one
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
admin.site.register(UserDetail)