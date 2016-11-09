from django.contrib import admin
from websites.forms import *
from websites.models import * 

admin.site.register(Industry)
admin.site.register(Location)
admin.site.register(Age)
admin.site.register(Gender)
admin.site.register(Income)
admin.site.register(Relationship)
admin.site.register(Children)

# for some reason TabularInline is breaking this but didn't persure as we discovered it's unusale anyway:
class WebsiteAdminInline1(admin.StackedInline):
    model = Crawl.websites.through
    form = WebsiteInlineForm
    extra = 0
    allow_add = False
    readonly_fields = ("website",)


class CrawlAdmin(admin.ModelAdmin):
    inlines = [WebsiteAdminInline1,]
    readonly_fields = ['created_at']
    filter_horizontal = ['websites', ]
    list_display = ('created_at',)
    fieldsets = (
        (None, {
            "fields": ('created_at', 'websites')
        }),
    )
    readonly_fields = ['created_at']

admin.site.register(Crawl, CrawlAdmin)


class WebsiteAdmin(admin.ModelAdmin):
    fs = ['domain', 'industry', 'location',
          'age', 'gender', 'income', 'relationship',
          'children']
    list_display = fs
    list_filter = fs

admin.site.register(Website, WebsiteAdmin)
