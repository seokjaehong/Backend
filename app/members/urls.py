from django.urls import path

from .apis.user_detail import UserDetailView, UserDetailImageView, UserDetailPhoneNumberView

urlpatterns = [
    path('info/', UserDetailView.as_view(), name='user-detail'),
    path('info/img-change/', UserDetailImageView.as_view(), name='user-image-change'),
    path('info/phone-change/', UserDetailPhoneNumberView.as_view(), name='user-phonenumber-change'),
    # path('reservation/', UserReservationListView.as_view(), name='user-reservation-list'),
    # path('reservation/cancel/', UserReservationCancelListView.as_view(), name='user-reservation-cancel-list'),

]
