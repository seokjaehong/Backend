from django.contrib.auth import get_user_model

from rest_framework import permissions, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from reservation.models import WishTravel
from reservation.serializer.wish_travel import WishTravelSerializer
from travel.serializer import TravelInformationWishListSerializer

User = get_user_model()


class WishTravelListCreateView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request):
        user = User.objects.get(username=request.user)
        wish_lists = user.wish_products.all()
        serializer = TravelInformationWishListSerializer(wish_lists, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        """
        위시리스트 생성
        :param request:
        :return:
        """

        context = {
            "request": self.request,
        }

        serializer = WishTravelSerializer(data=request.data, context=context)

        if serializer.is_valid(raise_exception=True, ):
            wishlist_created = serializer.save()
            if wishlist_created:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(status.HTTP_400_BAD_REQUEST)


#  해당 상품이 위시리스트에 있는지 체크
class TravelInfoDoesNotExists(APIException):
    status_code = 400
    default_detail = '해당 상품이 위시리스트에 없습니다.'
    default_code = 'travel_info_DoesNotExists'


class WishTravelDeleteView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def delete(self, request):
        """
        위시리스트 삭제
        1. travel_info 와 request.user 정보를 통해 해당 위시리스트 목록을 삭제
        예외처리
        - travel_info 없는 경우
        - 유저의 위시리스트에 해당 travel_info가 없는 경우
        :param request:
        :return:
        """

        if 'travel_info' in request.data:
            try:
                wish_product = WishTravel.objects.get(travel_info=request.data['travel_info'], user=request.user)

                if wish_product:
                    wish_product.delete()
                    data = {
                        'message': '해당 위시리스트 목록이 삭제되었습니다.'
                    }
                    return Response(data, status=status.HTTP_200_OK)

                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

            except WishTravel.DoesNotExist:
                raise TravelInfoDoesNotExists

        else:
            data = {
                'travel_info': "이 필드는 blank일 수 없습니다."
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
