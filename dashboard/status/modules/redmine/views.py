from django.db.models import Count, Q
from django.shortcuts import render_to_response
from django.template import RequestContext
from profiles.models import Profile

from models import Issue, IssueStatus, Project, User

def graphs(request, extra_context = None):
    """
    Work out which project is the most recently updated based on the most recently updated issue
    for either it or it('s) children
    """
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)

    projects = []
    for project in Project.objects.recently_updated()[:5]:
        children = Project.objects.filter(lft__gte=project.lft, rgt__lte=project.rgt)
        project_issues = Issue.objects.filter(project__in=children)
        total_issues = project_issues.count()
        closed_issues = project_issues.filter(Q(status__name='Closed') | Q(status__name='Rejected')).count()
        percentage = strip_decimal(float(float(closed_issues)/float(total_issues) * 100))
        if not percentage:
            percentage = 0
        projects.append({'name': project.name, 'total_issues': total_issues, 'closed_issues': closed_issues, 'percentage': percentage})
    context.update({'projects': projects})
    return render_to_response('redmine/graphs.html', context)

def list(request, extra_context = None):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)

    projects = []
    for project in Project.objects.recently_updated()[:9]:
        employees = []
        for user in User.objects.filter(issue__project__pk=project.id).annotate(issue_count=Count('issue')).order_by('issue_count'):
            try:
                employee = Profile.objects.get(email=user.mail)
                if employee not in employees and len(employees) < 5:
                    employees.append(employee)
            except Profile.DoesNotExist:
                pass
        projects.append({'name': project.name, 'employees': employees})
    context.update({'projects': projects})
    return render_to_response('redmine/list.html', context)

def strip_decimal(percentage):
    return str.rstrip(str(round(percentage, 0)), '.0')

