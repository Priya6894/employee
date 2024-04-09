from django.shortcuts import render

# Create your views here.
# views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics
from .models import Employee
from rest_framework.views import APIView


@api_view(['POST'])
def create_employee(request):
    try:
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Employee created successfully",
                "regid": serializer.data['id'],
                "success": True
            }, status=status.HTTP_200_OK)
        return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"message": "Employee creation failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    


##Get Employee ### 
@api_view(['GET'])
def get_employee(request):
    try:
        regid = request.GET.get('regid')
        if regid:
            employee = Employee.objects.filter(id=regid)
        else:
            employee = Employee.objects.all()
        
        serializer = EmployeeSerializer(employee, many=True)
        if employee.exists():
            return Response({"message": "Employee details found", "success": True, "employees": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "Employee details not found", "success": False, "employees": []}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": "Error retrieving employee details", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


### test.py class ##
class EmployeeDetailView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



class EmployeeDetailView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    



class EmployeeDetailView(generics.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeUpdate(APIView):
    def put(self, request, regid, format=None):
        try:
            employee = Employee.objects.get(regid=regid)
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Employee details updated successfully", "success": True}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response({"message": "No employee found with this regid", "success": False}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Employee updation failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return Response({"message": "Employee updation failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class EmployeeDelete(APIView):
    def delete(self, request, regid, format=None):
        try:
            employee = Employee.objects.get(regid=regid)
            employee.delete()
            return Response({"message": "Employee deleted successfully", "success": True}, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({"message": "No employee found with this regid", "success": False}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Employee deletion failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
