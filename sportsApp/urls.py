from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('leaderboard/',views.leaderboard,name='leaderboard'),
    path("events/",views.events, name='events'),
    path("news/<int:news_id>/",views.latest_news_page,name='news_detail'),
    path("teams/",views.teams,name="team"),
    path("submit_team_request/",views.submit_team_request,name='submit_team_request'),
    path("success_state/",views.success_state,name="success_state")
]