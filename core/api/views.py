from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.api.serializers import SignUpSerializer,ProfileSerialzer,AddressSerialzer
from core.models import Address

class SignUpView(APIView):

    def post(self,request):
        serialzier = SignUpSerializer(data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(status=201)
        return Response(serialzier.errors,status=400)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        serialzier = ProfileSerialzer(user.profile)
        return Response(serialzier.data)
        

    def put(self,request):
        profile = request.user.profile
        serialzier = ProfileSerialzer(profile,data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(status=201)
        return Response(serialzier.errors,status=400)
    


class AddressView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        adresses = Address.objects.filter(user=user)
        serializer = AddressSerialzer(adresses,many=True)
        return Response(serializer.data)
        

    def post(self,request):
        user = request.user
        serializer = AddressSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(status=201)
        return Response(serializer.errors,status=400)