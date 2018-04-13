from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from reservation.models import Reservation
from reservation.serializer import ReservationCancelSerializer


class ReservationCancelView(APIView):

    def get(self, request, **kwargs):
        reservation_informations = Reservation.objects.filter(is_canceled=True)
        serializer = ReservationCancelSerializer(reservation_informations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        reservation = Reservation.objects.get(pk=pk)
        serializer = ReservationCancelSerializer(reservation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)