from django.contrib import admin

from apps.delivery_club.models import DeliveryRecord


@admin.register(DeliveryRecord)
class DeliveryRecordAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order_id',
        'delivery_date',
        'price',
        'price_in_rub',
        'updated'
    )
    search_fields = ('order_id',)
    list_display_links = ('id', 'order_id')
