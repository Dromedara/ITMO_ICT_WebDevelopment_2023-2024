from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from practice.models import *
from practice.serializers import (WarriorSerializer, ProfessionCreateSerializer, SkillSerializer,
                                  SkillCreateSerializer, OneWarriorSerializer, WarriorProfessionSerializer, WarriorSkillSerializer)

### 3.2.1


class WarriorAPIView(APIView):
   def get(self, request):
       warriors = Warrior.objects.all()
       serializer = WarriorSerializer(warriors, many=True)
       return Response({"Warriors": serializer.data})


class ProfessionCreateView(APIView):

   def post(self, request):
       profession = request.data.get("profession")
       serializer = ProfessionCreateSerializer(data=profession)

       if serializer.is_valid(raise_exception=True):
           profession_saved = serializer.save()

       return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


class SkillCreateView(APIView):

    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillCreateSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})


### 3.2.2

class WarriorListAPIView(generics.ListAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionCreateSerializer
    queryset = Profession.objects.all()


class ShowWarriorAPIView(generics.RetrieveAPIView):
    serializer_class = OneWarriorSerializer
    queryset = Warrior.objects.all()


class DeleteWarriorAPIView(generics.DestroyAPIView):
    serializer_class = OneWarriorSerializer
    queryset = Warrior.objects.all()


class UpdateWarriorAPIView(generics.UpdateAPIView):
    serializer_class = OneWarriorSerializer
    queryset = Warrior.objects.all()


class WarriorProfessionListAPIView(generics.ListAPIView):
    serializer_class = WarriorProfessionSerializer
    queryset = Warrior.objects.all()


class WarriorSkillListApiView(generics.ListAPIView):
    serializer_class = WarriorSkillSerializer
    queryset = Warrior.objects.all()
