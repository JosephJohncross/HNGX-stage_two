from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializer import GeneralPersonSerializer, GetPersonSerializer


class PersonCustomView(APIView):
    """Handles all CRUD operations made on the person model"""

    def get(self, request):
        """Returns a person data, serialized as name, id"""

        name = request.query_params.get('name')

        try:
            print(name)
            person = Person.objects.get(name=name)
            serializer = GetPersonSerializer(person)

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except Person.DoesNotExist:
            return Response(
                "User does not exist",
                status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        """Creates a person object"""

        serializer = GeneralPersonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                "Person created succesfully",
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request):
        """Updates a person object"""

        id = request.data.get('id')
        name = request.data.get('name')

        try:
            person = Person.objects.get(id=id)
        except Person.DoesNotExist:
            return Response(
                "No user with id found",
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = GetPersonSerializer(person, data=request.data)
        if serializer.is_valid():
            # Checks if a user with updated name already exist
            person = Person.objects.filter(name=name)
            if person:
                return Response(
                    "A person with the updated name already exist",
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                serializer.save()
                return Response(
                    {'person': serializer.validated_data},
                    status=status.HTTP_200_OK
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request):
        """Delete a user"""

        id = request.data.get('id')
        try:
            person = Person.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
