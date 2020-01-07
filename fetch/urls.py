from django.urls import path
from . import views


urlpatterns = [
	path('',views.home, name = 'home'),
	path('fetch_result', views.add, name = 'fetch_result'),
	path('recivecaptha', views.recivecaptha, name = 'recivecaptha'),
	path('captcha', views.getcaptcha, name = 'captcha'),
	path('about', views.about, name = 'about'),
	path('results', views.results, name = 'results'),
	path('login', views.login, name = 'login'),
	path('logout', views.logout, name = 'logout'),
	path('result_db', views.result_db, name = 'result_db'),
	path('analysis', views.analysis, name = 'analysis'),
	path('student', views.student, name = 'student'),
	path('analysis_result', views.analysis_result, name = 'analysis_result'),
]