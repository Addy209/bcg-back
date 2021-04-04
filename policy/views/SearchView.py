from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from policy.models import Customer, Policy_feature, Policy_tbl
from policy.serializers.Policy import PolicyTableSerializer, PolicyFeatureSerializer
from django.views.decorators.cache import cache_page
from django.shortcuts import get_list_or_404,get_object_or_404
from django.utils.decorators import method_decorator
from django.db.models import Q

class SearchView(APIView):
   # @method_decorator(cache_page(60*60*2))
    def get(self, request):
        try:
            print()
            search_key=int(request.query_params['search_key'])
            search_by=int(request.query_params['by'])
            result=None
            print(search_by)
            if search_by==10:
                result=Policy_tbl.objects.filter(Q(Policy_id__startswith=search_key))[0:10]
            elif search_by==11:
                result=Policy_tbl.objects.filter(Q(Customer_id__Customer_id__startswith=search_key))[0:10]
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            ser_result=PolicyTableSerializer(result, many=True)
            return Response({"data":ser_result.data})
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
