from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aqui você pode adicionar dados para o dashboard
        return context

class SuprimentosView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/suprimentos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aqui você pode adicionar dados específicos de suprimentos
        return context

class OrcamentosView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/orcamentos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aqui você pode adicionar dados específicos de orçamentos
        return context 