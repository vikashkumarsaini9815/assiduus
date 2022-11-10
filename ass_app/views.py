from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timezone
from itertools import islice
import uuid
from .models import User, Message
# Create your views here.


# class UserAPIView(APIView):
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"success":True}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MessageAPIView(APIView):
#     def post(self, request, format=None):
#         serializer = MessageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"success":True}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    
    def post(self, request, format = None) :
        data = request.data
        # username = data['username']
        # email = data['email']
        # message = data['message']
        try:
            username = data['username']
            email = data['email']
            message = data['message']
            
    
            try:
                U = User.objects.get(email = email)

                if data['Token'] == U.Token:
                    m = Message.objects.filter(user = U)
                    length = len(m)
                    cal = length - 10
                    if length <= 10:
                        result = m
                    else:
                        result = m[cal:]           
                    var1 = result[0].created
                    dt = datetime.utcnow()
                    var2 = dt.replace(tzinfo=timezone.utc)
                    count_time = var2 - var1
                    time_in_hour = count_time.seconds // 3600 
                    insert_flag = False
                    if length < 10:
                        insert_flag = True
                    elif time_in_hour > 1:
                        insert_flag = True

                    if insert_flag == True :
                        m = Message(user = U, message = message)
                        m.save()
                
                        final_result = {
                                            "id":m.id ,
                                            "message": m.message,
                                            "created_at": m.created,
                                            "updated_at": m.updated,
                                            "created_by": {
                                            "id": U.id,
                                            "username": U.username,
                                            "email": U.email,

                                            }
                                            }
                        return Response(final_result, status=status.HTTP_201_CREATED)
                    else:
                        return Response({"success":"complite your one hour message try after 1 hour"})
                else:
                    return Response({"success":"Your token is not valid"})
            except:
            # return Response({"succes":"no"})
                ganrate_Token = uuid.uuid1()
                U = User(username = username, email = email, Token = ganrate_Token)
                U.save()
                m = Message(user = U , message = message)
                m.save()
                final_result = {
                                            "id":m.id ,
                                            "message": m.message,
                                            "created_at": m.created,
                                            "updated_at": m.updated,
                                            "created_by": {
                                            "id": U.id,
                                            "username": U.username,
                                            "email": U.email,
                                            "Token":ganrate_Token,

                                            }
                                            }
                return Response(final_result, status=status.HTTP_201_CREATED)


        except KeyError:
            return Response({"success":False},status=status.HTTP_400_BAD_REQUEST)



