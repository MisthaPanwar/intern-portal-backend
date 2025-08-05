from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET']) 
def get_intern_data(request):
    """
    This view returns dummy intern data as a JSON response.
    """
    dummy_data = {
        'internName': 'Mistha',
        'referralCode': 'mistha2025',
        'totalDonations': 750  
    }
    return Response(dummy_data)

