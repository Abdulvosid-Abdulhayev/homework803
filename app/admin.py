from django.contrib import admin
from .models import Klass, Mehmonxona, Travel

@admin.register(Klass)
class KlassAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomi', 'narxi')
    search_fields = ('nomi',)
    ordering = ('nomi',)

@admin.register(Mehmonxona)
class MehmonxonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomi', 'yulduzlar_soni', 'narxi')
    search_fields = ('nomi',)
    list_filter = ('yulduzlar_soni',)
    ordering = ('-yulduzlar_soni',)

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomi', 'muddati', 'narxi', 'klass', 'mehmonxona')
    search_fields = ('nomi', 'klass__nomi', 'mehmonxona__nomi')
    list_filter = ('klass', 'mehmonxona')
    ordering = ('-muddati',)
