import datetime

from django.contrib import messages
from django.urls import reverse
from django.views.generic import FormView, TemplateView, ListView

from apps.company.forms import WorkingForm
from apps.company.models import WorkingModel


class ReportView(FormView, ListView):
    form_class = WorkingForm
    model = WorkingModel
    template_name = "report.html"

    def calculate_total_working_time(self):
        working_list = WorkingModel.objects.filter(user=self.request.user)

        total_working = datetime.timedelta(hours=0)
        for working in working_list:
            total_working = total_working + (working.ending_time - working.starting_time)

        return total_working

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reports_list'] = WorkingModel.objects.order_by('-created_at').filter(user=self.request.user)
        context['total'] = self.calculate_total_working_time
        return context

    def form_valid(self, form):
        working = form.save(commit=False)
        working.user = self.request.user
        working.save()
        messages.success(self.request, "The working type is added successfully to list!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('company:report')


class ResultView(TemplateView):
    model = WorkingModel
    template_name = "result.html"

    def calculate_total_working_time(self):
        working_list = WorkingModel.objects.filter(user=self.request.user)
        total_working = datetime.timedelta(hours=0)
        for working in working_list:
            total_working = total_working + (working.ending_time - working.starting_time)

        return total_working

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result_list'] = WorkingModel.objects.order_by('-created_at')
        context['total'] = self.calculate_total_working_time
        return context
