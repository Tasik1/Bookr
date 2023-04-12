from django.contrib import admin
from .models import Publisher, Book, Review, Contributor, BookContributor


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("title", "publication_date", "isbn", "publisher")


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')


admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, MemberAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)
