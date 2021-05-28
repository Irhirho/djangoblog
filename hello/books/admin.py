from django.contrib import admin
from models import Author,Publisher,Book


class BookAdmin(admin.ModelAdmin):
	list_display=('title','publication_date','publisher')
	list_filter=('publication_date',)
	date_hierarchy='publication_date'
	filter_horizontal=('authors',)
	#filter_horizontal=('publisher',)
	raw_id_fields=('publisher',)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book,BookAdmin)
