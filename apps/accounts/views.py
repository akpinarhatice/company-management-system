from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import FormView, TemplateView, RedirectView

from apps.accounts.forms import RegistrationForm


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:login')


class LoginView(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse('accounts:home')


class LogoutView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = '/'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)

    def get_success_url(self):
        return reverse('accounts:home')


class Home(TemplateView):
    template_name = "home.html"
