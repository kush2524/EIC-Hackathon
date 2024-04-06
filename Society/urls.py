
from django.urls import path,re_path
from django.conf.urls import handler404
from .views import index,register_society,enter_uid,submit_problem,problem_submission_success,secretary_problems,secretary_uid_form,solve_problem,view_pending_problems,view_pending_requests,view_pending_problems_resident
urlpatterns = [
    path('', index, name='index_page'),
    path('register_society/', register_society, name='register_society'),
     path('enter-uid/', enter_uid, name='enter_uid'),\
    
      path('submit-problem/<uuid:society_uid>/', submit_problem, name='submit_problem'),
    path('problem-submission-success/', problem_submission_success, name='problem_submission_success'),
      path('secretary/<uuid:secretary_uid>/', secretary_problems, name='secretary_problems'),
    path('secretary/', secretary_uid_form, name='secretary_uid_form'),
        path('solve-problem/', solve_problem, name='solve_problem'),
            path('view-pending-requests/', view_pending_requests, name='view_pending_requests'),
    path('view-pending-problems/', view_pending_problems, name='view_pending_problems'),
       path('view-pending-problems/<str:resident_uid>/', view_pending_problems_resident, name='view_pending_problems_resident'),
       ]
handler404 = 'Society.views.custom_404'