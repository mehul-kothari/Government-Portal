from django.contrib import admin

from Login.models import  form2,GeneralProblems,Area,Locality,Areas,Localities,Likes,Discussion,UserProfile,Notifications,SpecificProblems,Likes1,SpecificLocality


class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class RatingAdmin1(admin.ModelAdmin):
    readonly_fields = ('locality_id',)

admin.site.register(form2,RatingAdmin)
admin.site.register(GeneralProblems)
admin.site.register(Area)
admin.site.register(Locality)
admin.site.register(Areas)
admin.site.register(Localities)
admin.site.register(Likes)
admin.site.register(Discussion)
admin.site.register(UserProfile)
admin.site.register(Notifications)
admin.site.register(SpecificProblems)
admin.site.register(Likes1)
admin.site.register(SpecificLocality,RatingAdmin1)





# Register your models here.
