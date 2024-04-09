from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Employee

class EmployeeAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_employee(self):
        url = '/employees/create/'
        data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "age": 30,
            "gender": "male",
            "phoneNo": "1234567890",
            "addressDetails": {
                "hno": "123",
                "street": "Main St",
                "city": "Springfield",
                "state": "IL"
            },
            "workExperience": [
                {
                    "companyName": "ABC Inc.",
                    "fromDate": "2010-01-01",
                    "toDate": "2015-12-31",
                    "address": "123 Business St"
                }
            ],
            "qualifications": [
                {
                    "qualificationName": "Bachelor's Degree",
                    "fromDate": "2008-01-01",
                    "toDate": "2010-12-31",
                    "percentage": 80.0
                }
            ],
            "projects": [
                {
                    "title": "Project X",
                    "description": "Managed the development of Project X"
                }
            ],
            "photo": ""
        }

        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        # Assert response status code and content
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertIn('regid', response.data)

def test_create_duplicate_employee(self):
    url = '/employees/create/'
    data = {
        "name": "John Doe",
        "email": "johndoe@example.com",  # Duplicate email
        "age": 30,
        "gender": "male",
        "phoneNo": "1234567890",
        "addressDetails": {
            "hno": "123",
            "street": "Main St",
            "city": "Springfield",
            "state": "IL"
        },
        "workExperience": [
            {
                "companyName": "ABC Inc.",
                "fromDate": "2010-01-01",
                "toDate": "2015-12-31",
                "address": "123 Business St"
            }
        ],
        "qualifications": [
            {
                "qualificationName": "Bachelor's Degree",
                "fromDate": "2008-01-01",
                "toDate": "2010-12-31",
                "percentage": 80.0
            }
        ],
        "projects": [
            {
                "title": "Project X",
                "description": "Managed the development of Project X"
            }
        ],
        "photo": ""
    }

    response = self.client.post(url, data=json.dumps(data), content_type='application/json')

    # Assert response for duplicate email
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertFalse(response.data['success'])
    self.assertEqual(response.data['message'], 'Employee with this email already exists')



def test_get_all_employees(self):
    url = '/employees/'
    response = self.client.get(url)

    # Assert response for getting all employees
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertTrue(response.data['success'])
    self.assertTrue('employees' in response.data)



################ Update,Delete,Reterive  ##############
class EmployeeAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.employee = Employee.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            age=30,
            gender='male',
            phoneNo='1234567890',
            addressDetails={
                'hno': '123',
                'street': 'Main Street',
                'city': 'Anytown',
                'state': 'CA'
            }
            # Add more fields as needed based on your Employee model
        )

    def test_update_employee(self):
        update_url = '/employees/update/EMP001/'  # Assuming 'EMP001' is a valid employee regid
        update_data = {
        "name": "Updated Name",
        "age": 35,
        "phoneNo": "9876543210",
        "addressDetails": {
            "hno": "456",
            "street": "New St",
            "city": "Springfield",
            "state": "IL"
        }
    }
        response = self.client.put(update_url, data=json.dumps(update_data), content_type='application/json')

    # Validate response status code and content
        self.assertEqual(response.status_code, 500)  # Expecting a 500 Internal Server Error
        self.assertFalse(response.data['success'])   # Assuming 'success' flag is False
        self.assertIn('message', response.data)       # Check for error message in response



    def test_delete_employee(self):
        employee_id = self.employee.pk
        url = reverse('employee-detail', kwargs={'pk': employee_id})
        response = self.client.delete(url)

        # Check if the response status code is 204 No Content
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Assert that the employee record has been deleted from the database
        self.assertFalse(Employee.objects.filter(pk=employee_id).exists())

    def test_retrieve_employee(self):
        employee_id = self.employee.pk  # Use 'pk' instead of 'id'
        url = reverse('employee-detail', kwargs={'pk': employee_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.employee.name)
        self.assertEqual(response.data['email'], self.employee.email)
        # Include assertions for other fields as needed


    