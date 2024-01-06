from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from accounts.serializers import CustomUserSerializer
from rest_framework.response import Response
from accounts.models import CustomUser
