from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Person
from .serializer import GeneralPersonSerializer, GetPersonSerializer


class PersonCustomView(APIView):
    """Handles all CRUD operations made on the person model"""

    def get(self, request, id):
        """Returns a person data, serialized as name, id"""

        id = self.kwargs.get('id')

        if not id:
            return Response(
                "Id field must not be blank"
            )

        try:
            person = Person.objects.get(id=id)
            serializer = GetPersonSerializer(person)

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except Person.DoesNotExist:
            return Response(
                {"details": "User does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, id):
        """Updates a person object"""

        # id = request.data.get('id')
        # name = request.data.get('name')

        # try:
        #     person = Person.objects.get(id=id)
        # except Person.DoesNotExist:
        #     return Response(
        #         "No user with id found",
        #         status=status.HTTP_404_NOT_FOUND
        #     )

        # serializer = GetPersonSerializer(person, data=request.data)
        # if serializer.is_valid():
        #     # Checks if a user with updated name already exist
        #     person = Person.objects.filter(name=name)
        #     if person:
        #         return Response(
        #             "A person with the updated name already exist",
        #             status=status.HTTP_400_BAD_REQUEST
        #         )
        #     else:
        #         serializer.save()
        #         return Response(
        #             {'person': serializer.validated_data},
        #             status=status.HTTP_200_OK
        #         )
        # else:
        #     return Response(
        #         serializer.errors,
        #         status=status.HTTP_400_BAD_REQUEST
        #     )

        name = request.data.get('name')
        id = self.kwargs.get('id')

        if not id:
            return Response(
                "Id field cannot be blank",
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            person = Person.objects.get(id=id)
        except Person.DoesNotExist:
            return Response(
                {"error": "No user with id found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = GeneralPersonSerializer(person, data=request.data)
        if serializer.is_valid():
            # Checks if a user with updated name already exist
            person_exist = Person.objects.filter(name=name)
            if person_exist:
                return Response(
                    {"detail": "A person with the updated name already exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                serializer.save()
                person_serializer = GetPersonSerializer(person)

                return Response(
                    person_serializer.data,
                    status=status.HTTP_200_OK
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, id):
        """Delete a user"""

        id = self.kwargs.get('id')
        try:
            person = Person.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        person.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_person(request):
    """Creates a person object"""

    name = request.POST.get('name')
    data = {
        'name': name
    }

    serializer = GeneralPersonSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        try:
            person = Person.objects.get(name=name)
        except:
            return Response(
                "Something went wrong",
                status=status.HTTP_400_BAD_REQUEST
            )
        person_serializer = GetPersonSerializer(person)

        return Response(
            person_serializer.data,
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# @api_view(['GET'])
# def get_person(request, id):
#     """Returns a person object"""
#     if not id:
#         return Response(
#             "Id field must not be blank"
#         )

#     try:
#         person = Person.objects.get(id=id)
#         serializer = GetPersonSerializer(person)

#         return Response(
#             serializer.data,
#             status=status.HTTP_200_OK
#         )
#     except Person.DoesNotExist:
#         return Response(
#             "User does not exist",
#             status=status.HTTP_404_NOT_FOUND
#         )


# @api_view(['PATCH'])
# def update_person(request, id=None):
#     """Updates a person object"""

#     name = request.data.get('name')

#     if not id:
#         return Response(
#             "Id field cannot be blank",
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     try:
#         person = Person.objects.get(id=id)
#     except Person.DoesNotExist:
#         return Response(
#             "No user with id found",
#             status=status.HTTP_404_NOT_FOUND
#         )

#     serializer = GeneralPersonSerializer(person, data=request.data)
#     if serializer.is_valid():
#         # Checks if a user with updated name already exist
#         person = Person.objects.filter(name=name)
#         if person:
#             return Response(
#                 "A person with the updated name already exist",
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         else:
#             serializer.save()
#             data = {
#                 'name': name,
#                 'id': id
#             }
#             person_serializer = GetPersonSerializer(data=data)
#             return Response(
#                 {'person': person_serializer.data},
#                 status=status.HTTP_200_OK
#             )
#     else:
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )


# @api_view(['DELETE'])
# def delete_person(request, id):
#     """Delete a person"""

#     try:
#         person = Person.objects.get(id=id)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     person.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
