from django.urls import path

from issue_tracker.views.issue_tracker import *

urlpatterns = [
    path('', IssueTrackerView.as_view()),
    path('issue_tracker/', IssueTrackerView.as_view(), name='issues_list'),
    path('issue_tracker/<int:pk>', IssueDetailView.as_view(), name='issue_detail'),
    path('issue_tracker/<int:pk>/update', IssueUpdateView.as_view(), name='issue_update'),
    path('issue_tracker/add', IssueAddView.as_view(), name='issue_add')
]