from django.db import models
from django.db.models import Max

class IssueManager(models.Manager):
    def unresolved(self):
        """
        Return all issues that are open.
        """
        return self.get_query_set().exclude(status__is_closed=True)

class ProjectManager(models.Manager):
    def recently_updated(self):
        """
        Return all projects with in most recently updated first order.

        Returns a list, instead of a query set, since the query set needs to be sorted.
        """
        from models import Issue
        project_list = list(self.get_query_set().filter(parent__isnull=True).annotate(max_updated=Max('issue__updated_on')).order_by('-max_updated'))
        for project in project_list:
            child_max_updated = Issue.objects.filter(project__parent=project).aggregate(max_updated_on=Max('updated_on'))['max_updated_on']
            if child_max_updated and child_max_updated > project.max_updated:
                project.max_updated = child_max_updated
        project_list = sorted(project_list, key=lambda p: p.max_updated)
        project_list.reverse()

        return project_list

