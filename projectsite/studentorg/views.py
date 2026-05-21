from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, Student, Program, College, OrgMember
from django.utils import timezone
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_year = timezone.now().year
        context['organizations_count'] = Organization.objects.count()
        context['students_count'] = Student.objects.count()
        context['programs_count'] = Program.objects.count()
        context['colleges_count'] = College.objects.count()
        context['org_members_count'] = OrgMember.objects.count()
        context['joined_this_year'] = OrgMember.objects.filter(date_joined__year=current_year).count()
        return context

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

from studentorg.forms import OrganizationForm 
 
class OrganizationCreateView(CreateView): 
    model = Organization 
    form_class = OrganizationForm 
    template_name = 'org_form.html' 
    success_url = reverse_lazy('organization-list') 

class OrgMemberListView(ListView):
    model = OrgMember
    context_object_name = 'members'
    template_name = 'orgmember_list.html'
    paginate_by = 10

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'student_list.html'
    paginate_by = 10

class CollegeListView(ListView):
    model = College
    context_object_name = 'colleges'
    template_name = 'college_list.html'
    paginate_by = 5

class ProgramListView(ListView):
    model = Program
    context_object_name = 'programs'
    template_name = 'program_list.html'
    paginate_by = 10
