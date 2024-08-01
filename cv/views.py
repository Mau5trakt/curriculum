from django.views.generic import TemplateView
from .models import *


class CurriculumView(TemplateView):
    template_name = 'cv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = CustomUser.objects.filter(id=1).first()
        context['user'] = user
        context['personal_informations'] = PersonalInformation.objects.filter(user=user)
        context['work_experiences'] = WorkExperience.objects.filter(user=user)
        context['languages'] = Language.objects.filter(user=user)
        context['courses'] = Course.objects.filter(user=user)
        context['programming_experiences'] = ProgrammingExperience.objects.filter(user=user)
        # each field of programming experience
        context['programming_languages'] = ProgrammingExperience.objects.filter(user=user, h_type='Programming languages')
        context['web_technologies'] = ProgrammingExperience.objects.filter(user=user, h_type='Web technologies')
        context['databases'] = ProgrammingExperience.objects.filter(user=user, h_type='Databases')
        context['vcs'] = ProgrammingExperience.objects.filter(user=user, h_type='VCS')
        context['other'] = ProgrammingExperience.objects.filter(user=user, h_type='Other')

        context['achievements'] = Achievement.objects.filter(user=user)
        context['additional'] = Additional.objects.filter(user=user)

        return context
