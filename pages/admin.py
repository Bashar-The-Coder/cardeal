from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Imtrn, Order
# Register your models here.

# admin.site.register(Team)

### list display for team admin

class TeamAdmin(admin.ModelAdmin):
    # add thumbnail
    def thumbnail(self, object):
        return format_html("<img src = '{}' width = '40' style = 'border-radius : 50%' />".format(object.photo.url))
    # rename the thumbnail
    thumbnail.short_description = "photo"
    list_display = ('id' , 'thumbnail' ,'fname' , 'desig',  'create_date')
    # create fname link clickable
    list_display_links = ('fname','id', 'thumbnail')
    # make a search bar
    search_fields = ('fname' , 'lname' , 'desig')
    #make a filter 
    list_filter = ('desig',)


#now register team admin in admin
admin.site.register(Team, TeamAdmin)

# admin.site.register(Item)
# admin.site.register(Zid)
# admin.site.register(Order)