from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from policy.models import Customer, Policy_feature, Policy_tbl
from policy.serializers.Policy import PolicyTableSerializer, PolicyFeatureSerializer
from policy.serializers.Analytics import AnalyticsSerializer
from django.views.decorators.cache import cache_page
from django.shortcuts import get_list_or_404,get_object_or_404
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.db import connection

class AnalyticsView(APIView):
    @method_decorator(cache_page(60*60*2))
    def get(self,request):
        try:
            region=None
            try:
                region=request.query_params['region']
                print(region)
            except Exception as e:
                print(e)
            if region:
              
                annual_report=Policy_tbl.objects.raw(f'''select policy_id, count(policy_id) as count, strftime('%m',date_of_purchase) as month from policy_Policy_tbl where policy_Policy_tbl.Customer_id_id in (select Customer_id from policy_Customer where Customer_Region='{region}') GROUP BY strftime('%m',date_of_purchase)''')
              
                # '''select policy_id, count(policy_id) as count, strftime('%m',date_of_purchase) as month from policy_Policy_tbl where Customer_id in (select Customer_id from policy_Customer where Customer_Region='North') GROUP BY strftime('%m',date_of_purchase)''')
            else:
                annual_report=Policy_tbl.objects.raw('''select policy_id, count(policy_id) as count, strftime('%m',date_of_purchase) as month from policy_Policy_tbl GROUP BY strftime('%m',date_of_purchase)''')
            ser_annual_report=AnalyticsSerializer(annual_report, many=True)
            return Response({"data":ser_annual_report.data},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)