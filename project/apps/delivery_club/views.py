from django.views.generic import ListView
from django.db.models import Sum

from apps.delivery_club.models import DeliveryRecord


class DeliveryRecordsDashboard(ListView):
    # Сортируем по row id для точного повторения таблицы
    queryset = DeliveryRecord.objects.all().order_by('row_id')
    template_name = 'index.html'
    context_object_name = 'records'

    def get_context_data(self, *args, **kwargs):
        """
            Записываем в контекст дополнительно:
             Сумму в долларах, рублях, отдельно даты и цены для графика.
        """
        context = super().get_context_data(*args, **kwargs)

        context['total_in_usd'] = DeliveryRecord.objects.aggregate(
            Sum('price')
        )['price__sum']

        context['total_in_rub'] = DeliveryRecord.objects.aggregate(
            Sum('price_in_rub')
        )['price_in_rub__sum']

        _ = DeliveryRecord.objects.order_by('-delivery_date').values_list(
            'delivery_date', "price"
        )
        _dates = []
        _prices = []

        for _date, _price in _:
            _dates.append(_date.strftime("%d.%m.%Y"))
            _prices.append(str(_price))

        context['dates'] = _dates
        context['prices'] = _prices

        return context
