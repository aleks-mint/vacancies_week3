from django.db.models import Count
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views.generic import ListView, TemplateView, DetailView

from vacancies.models import Specialty, Vacancy, Company


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'specialties': Specialty.objects.annotate(vacancies_count=Count('vacancies')),
            'companies': Company.objects.annotate(vacancies_count=Count('vacancies')),
        }

        return context


class VacanciesListView(ListView):
    model = Vacancy
    template_name = 'vacancies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'vacancies': Vacancy.objects.all(),
            }

        return context


class VacanciesCatView(TemplateView):
    template_name = 'vacancies.html'

    def get_context_data(self, category, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'vacancies': Vacancy.objects.filter(specialty__code=category),
            'title': Specialty.objects.get(code=category).title,
        }

        return context


class VacancyView(DetailView):
    template_name = "vacancy.html"
    pk_url_kwarg = 'id'
    model = Vacancy
    queryset = Vacancy.objects.select_related('company').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prev_page'] = self.request.META.get('HTTP_REFERER')
        return context


class CompanyView(TemplateView):
    template_name = "company.html"

    def get_context_data(self, id, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'vacancies': Vacancy.objects.filter(company__id=id),
            'company': Company.objects.get(id=id),
            'prev_page': self.request.META.get('HTTP_REFERER'),
        }

        return context


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')
