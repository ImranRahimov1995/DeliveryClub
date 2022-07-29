from django.contrib import admin

from apps.core.models import CurrencyStorage, Subscriber


@admin.register(CurrencyStorage)
class CurrencyStorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'char_code', 'value', 'updated')
    search_fields = ('char_code',)
    list_display_links = ('id', 'char_code')


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id')
    search_fields = ('chat_id',)
    list_display_links = ('id', 'chat_id')
