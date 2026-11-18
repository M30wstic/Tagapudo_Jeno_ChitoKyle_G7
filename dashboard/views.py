from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home.html"  # fallback

    ROLE_TEMPLATES = {
        "FARMER": "dashboard/farmer.html",
        "COOPERATIVE": "dashboard/cooperative.html",
        "BUYER": "dashboard/buyer.html",
        "ADMIN": "dashboard/admin.html",
    }

    def get_template_names(self):
        return [self.ROLE_TEMPLATES.get(self.request.user.role, self.template_name)]