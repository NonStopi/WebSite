menu = [
    {'title': 'Афиша', 'url_name': 'search'},
    {'title':'Заказ билетов', 'url_name': 'contact'},
    {'title':'Контакты', 'url_name': 'contact'},
    {'title':'История дворца', 'url_name': 'contact'},
    {'title':'Галерия', 'url_name': 'contact'},
    {'title':'Планы залов', 'url_name': 'contact'},
]

class DataMixin:
    title_page = None
    extra_context = {}

    def __init__(self) -> None:
        if self.title_page:
            self.extra_context['title'] = self.title_page

    def get_mixin_context(self, context, **kwargs):
        context.update(kwargs)
        return context
