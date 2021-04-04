from functools import partial
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.views import APIView
from policy.models import Customer, Policy_feature, Policy_tbl
from policy.serializers.Policy import PolicyTableSerializer, PolicyFeatureSerializer
from django.views.decorators.cache import cache_page
from django.shortcuts import get_list_or_404,get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework.pagination import PageNumberPagination

class GetPolicyView(APIView): 
        def get(self, request, pk):
            try:
                policy_tbl_object=get_object_or_404(Policy_tbl,pk=pk)
                policy_feature_list=get_list_or_404(Policy_feature,Policy_id=pk)
                ser_policy_tbl_object=PolicyTableSerializer(policy_tbl_object)
                ser_policy_feature_list=PolicyFeatureSerializer(policy_feature_list, many=True)
                return Response({"data":ser_policy_tbl_object.data, "feature":ser_policy_feature_list.data})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        def put(self, request, pk):
            print(request.data)
            try:
                patch_data=request.data
                Policy_obj=get_object_or_404(Policy_tbl,pk=pk)
                Policy_details_ser=PolicyTableSerializer(Policy_obj, data=patch_data, partial=True)
                Feature_obj=Policy_feature.objects.filter(Policy_id=pk)[0]
                Feature_ser=PolicyFeatureSerializer(Feature_obj,data=patch_data, partial=True)
                if Policy_details_ser.is_valid() and Feature_ser.is_valid():
                    Policy_details_ser.save()
                    Feature_ser.save()
                    return Response({"data":"sucess"},status=status.HTTP_200_OK)
                
                
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            

class GetAllPaginatedPolicy(generics.ListAPIView):
    queryset=Policy_feature.objects.all()
    serializer_class=PolicyFeatureSerializer
    pagination_class=PageNumberPagination