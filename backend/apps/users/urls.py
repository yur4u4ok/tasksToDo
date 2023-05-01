from django.urls import path

from .views import UserToAdmin, AdminToUser, AllUsersView

urlpatterns = [
    path('', AllUsersView.as_view(), name="list_all_users"),
    path('/<int:pk>/to_admin', UserToAdmin.as_view(), name='user_to_admin'),
    path('/<int:pk>/to_user', AdminToUser.as_view(), name="admin_to_user"),
]
