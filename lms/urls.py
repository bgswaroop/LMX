# Core Django imports.
from django.urls import path

# LMS app imports
from lms.views.account.login_view import UserLoginView
from lms.views.account.logout_view import UserLogoutView
from lms.views.account.register_view import (
    ActivateView,
    AccountActivationSentView,
    UserRegisterView,
)
from lms.views.course.course_views import (
    CourseListView,
)
from lms.views.course.grading_scheme_view import (
    GradingSchemeUpdateView,
    GradingSchemeCreateView
)
from lms.views.course.settings_view import (
    CourseDetailsView,
    CourseManageView,
    CourseSectionsView,
    CourseStatisticsView
)
from lms.views.dashboard.student.dashboard_views import (
    DashboardHomeView,
)

# Specifies the app name for name spacing.
app_name = "lms"

# lms/urls.py
urlpatterns = [

    # LMS URLS #

    # /home/
    path(
        route='',
        view=CourseListView.as_view(),
        name='home'
    ),

    # ACCOUNT URLS #

    # /account/login/
    path(
        route='account/login/',
        view=UserLoginView.as_view(),
        name='login'
    ),

    # /account/login/
    path(
        route='account/register/',
        view=UserRegisterView.as_view(),
        name='register'
    ),

    # /account/logout/
    path(
        route='account/logout/',
        view=UserLogoutView.as_view(),
        name='logout'
    ),

    path(route='account_activation_sent/',
         view=AccountActivationSentView.as_view(),
         name='account_activation_sent'
         ),

    path(route='activate/<uidb64>/<token>/',
         view=ActivateView.as_view(),
         name='activate'
         ),

    # DASHBOARD URLS #

    # /author/dashboard/home/
    path(
        route="student/dashboard/home/",
        view=DashboardHomeView.as_view(),
        name="dashboard_home"
    ),

    # COURSE SETTINGS URLS #

    path(
        route="course/<int:pk>/details/",
        view=CourseDetailsView.as_view(),
        name="course_details"
    ),
    path(
        route="course/<int:pk>/manage/",
        view=CourseManageView.as_view(),
        name="course_manage"
    ),
    path(
        route="course/<int:pk>/sections/",
        view=CourseSectionsView.as_view(),
        name="course_sections"
    ),
    path(
        route="course/<int:pk>/statistics/",
        view=CourseStatisticsView.as_view(),
        name="course_statistics"
    ),
    path(
        route="course/<int:pk>/grading_scheme/new",
        view=GradingSchemeCreateView.as_view(),
        name="course_grading_scheme_create"
    ),
    path(
        route="course/<int:pk>/grading_scheme/update",
        view=GradingSchemeUpdateView.as_view(),
        name="course_grading_scheme_update"
    )
]
