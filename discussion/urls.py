from django.urls import path
from . import views

urlpatterns = [
	path('ajax/discussion/',views.GetDiscussion.as_view(), name='discussion.getDiscussion'),
	path('ajax/addComment/',views.addComment, name='discussion.addComment'),
]	