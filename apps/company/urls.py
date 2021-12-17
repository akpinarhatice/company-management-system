from django.urls import path

from apps.company.views import ReportView, ResultView

app_name = "company"

urlpatterns = [

    path('report/', ReportView.as_view(), name="report"),
    path('result/', ResultView.as_view(), name="result"),

]
