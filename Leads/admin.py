from django.contrib import admin
from Leads.models import User,Agent,Lead,UserProfile,Category

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(UserProfile)
admin.site.register(Category)