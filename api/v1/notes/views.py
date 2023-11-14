import traceback

from django.db import transaction

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from general.functions import generate_serializer_errors
from api.v1.notes.serializers import *
from web.models import Notes


@api_view(['POST'])
@permission_classes([AllowAny])
def add_notes(request):
    try:
        transaction.set_autocommit(False)
        serialized_data = CreateNotesSerializer(data=request.data)
        if serialized_data.is_valid():
            title = request.data["title"]
            body = request.data["body"]

            notes = Notes.objects.create(
                title = title,
                body = body
            )

            transaction.commit()
            response_data = {
                "StatusCode" : 6000,
                "data" : {
                    "title" : "Success",
                    "message" : "Notes added successfully"
                }
            }
        else:
            response_data = {
                "StatusCode" : 6001,
                "data" : {
                    "title" : "Failed",
                    "message" : generate_serializer_errors(serialized_data._errors)
                }
            }
    except Exception as e:
        transaction.rollback()
        errType = e.__class__.__name__
        errors = {
            errType: traceback.format_exc()
        }
        response_data = {
            "status": 0,
            "api": request.get_full_path(),
            "request": request.data,
            "message": str(e),
            "response": errors
        }

    return Response({'app_data': response_data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def single_note(request, pk):
    try:
        if (notes := Notes.objects.filter(pk=pk, is_deleted=False)).exists():
            notes = notes.latest("created_at")

            print(notes,"0-0-0-0-0-0-0-0-0")

            serialized_data = ListNotesSerializer(
                notes,
                context  = {
                    "request" : request
                },
            ).data

            response_data = {
                "StatusCode" : 6000,
                "data" : serialized_data
            }
        else:
            response_data = {
                "StatusCode" : 6001,
                "data" : {
                    "title" : "Failed",
                    "message" : "Note not found"
                }
            }
    except Exception as e:
        transaction.rollback()
        errType = e.__class__.__name__
        errors = {
            errType: traceback.format_exc()
        }
        response_data = {
            "status": 0,
            "api": request.get_full_path(),
            "request": request.data,
            "message": str(e),
            "response": errors
        }

    return Response({'app_data': response_data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def list_notes(request):
    try:
        q = request.GET.get('q')
        if (notes := Notes.objects.filter(is_deleted=False)).exists():

            if q:
                notes = notes.filter(title__icontains=q)

            serialized_data = ListNotesSerializer(
                notes,
                context  = {
                    "request" : request
                },
                many = True,
            ).data

            response_data = {
                "StatusCode" : 6000,
                "data" : serialized_data
            }
        else:
            response_data = {
                "StatusCode" : 6001,
                "data" : []
            }
    except Exception as e:
        transaction.rollback()
        errType = e.__class__.__name__
        errors = {
            errType: traceback.format_exc()
        }
        response_data = {
            "status": 0,
            "api": request.get_full_path(),
            "request": request.data,
            "message": str(e),
            "response": errors
        }

    return Response({'app_data': response_data}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([AllowAny])
def edit_note(request, pk):
    try:
        transaction.set_autocommit(False)
        title = request.data.get("title")
        body = request.data.get("body")

        if (notes := Notes.objects.filter(pk=pk, is_deleted=False)).exists():
            notes = notes.latest("created_at")

            if title:
                notes.title = title
            if body:
                notes.body = body
            
            notes.save()

            transaction.commit()
            response_data = {
                "StatusCode" : 6000,
                "data" : {
                    "title" : "Success",
                    "message" : "Note updated successfully"
                }
            }
        else:
            response_data = {
                "StatusCode" : 6001,
                "data" : {
                    "title" : "Failed",
                    "message" : "Note not found"
                }
            }

    except Exception as e:
        transaction.rollback()
        errType = e.__class__.__name__
        errors = {
            errType: traceback.format_exc()
        }
        response_data = {
            "status": 0,
            "api": request.get_full_path(),
            "request": request.data,
            "message": str(e),
            "response": errors
        }

    return Response({'app_data': response_data}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_note(request, pk):
    try:
        if (notes := Notes.objects.filter(pk=pk, is_deleted=False)).exists():
            notes = notes.latest("created_at")
            notes.delete()

            response_data = {
                "StatusCode" : 6000,
                "data" : {
                    "title" : "Success",
                    "message" : "Note deleted successfully"
                }
            }
        else:
            response_data = {
                "StatusCode" : 6001,
                "data" : {
                    "title" : "Failed",
                    "message" : "Note not found"
                }
            }
    except Exception as e:
        transaction.rollback()
        errType = e.__class__.__name__
        errors = {
            errType: traceback.format_exc()
        }
        response_data = {
            "status": 0,
            "api": request.get_full_path(),
            "request": request.data,
            "message": str(e),
            "response": errors
        }

    return Response({'app_data': response_data}, status=status.HTTP_200_OK)




