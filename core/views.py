from django.views.generic import TemplateView

from .models import Funcionario, Cliente

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['clientes'] = Cliente.objects.order_by('?').all()       
        return context
