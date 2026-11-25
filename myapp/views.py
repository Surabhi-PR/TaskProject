from django.shortcuts import render
from django.views.generic import View
import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@method_decorator(csrf_exempt, name = 'dispatch')
class BMIView(View):
    def post(self, request):
        data = json.loads(request.body)
        h = data.get("height")
        w = data.get("weight")

        # convert height from cm to meter
        height = h / 100

        # calculate bmi
        bmi = w / (height ** 2)

        result = {
            "Height" : data.get("height"),
            "Weight" : w,
            "BMI" : round(bmi, 2)
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt, name = 'dispatch')
class AgeView(View):
    def post(self, request):
        data = json.loads(request.body)
        birth = data.get("birth_year")
        current = data.get("current_year")
        age = current - birth
        result = {
            "Birth Year" : birth,
            "Current Year" : current,
            "Age" : age
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt, name = 'dispatch')
class PercentageView(View):
    def post(self, request):
        data = json.loads(request.body)
        obtained = data.get("obtained_marks")
        total = data.get("total_marks")
        percentage = (obtained / total) * 100
        result = {
            "Obtained Marks" : obtained,
            "Total Marks" : total,
            "Percentage" : percentage
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt, name = 'dispatch')
class SimpleInterestView(View):
    def post(self, request):
        data = json.loads(request.body)
        p = data.get("principal")
        r = data.get("rate")
        t = data.get("time")
        simple_interest = (p * r * t) / 100
        result = {
            "Principal" : p,
            "Rate" : r,
            "Time" : t,
            "Simple Interest" : simple_interest
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt, name = 'dispatch')
class ElectricityBillView(View):
    def post(self, request):
        data = json.loads(request.body)
        u = data.get("units")
        r = data.get("rate")
        bill = u * r
        result = {
            "Units" : u,
            "Rate" : r,
            "Bill" : bill
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt, name = 'dispatch')
class DiscountView(View):
    def post(self, request):
        data = json.loads(request.body)
        p = data.get("price")
        d = data.get("discount_percentage")
        discount_amount = (p * d) / 100
        final_price = p - discount_amount
        result = {
            "Price" : p,
            "Discount Percentage" : d,
            "Discount Amount" : discount_amount,
            "Final Price" : final_price


        }
        return JsonResponse(result)

@method_decorator(csrf_exempt, name = 'dispatch')
class ProfitView(View):
    def post(self, request):
        data = json.loads(request.body)
        cost = data.get("cost_price")
        selling = data.get("selling_price")
        profit = selling - cost
        result = {
            "Cost Price" : cost,
            "Selling Price" : selling,
            "Profit" : profit
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt, name = 'dispatch')
class SalaryView(View):
    def post(self, request):
        data = json.loads(request.body)
        basic = data.get("basic_salary")
        b = data.get("bonus")
        d = data.get("deduction")
        net_salary = basic + b - d
        result = {
            "Basic Salary" : basic,
            "Bonus" : b,
            "Deduction" : d,
            "Net Salary" : net_salary
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt, name = 'dispatch')
class TimeConverterView(View):
    def post(self, request):
        data = json.loads(request.body)
        h = data.get("hours")
        minutes = h * 60
        seconds = h * 3600
        result = {
            "Hours" : h,
            "Minutes" : minutes,
            "Seconds" : seconds
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt, name = 'dispatch')
class FuelCostView(View):
    def post(self, request):
        data = json.loads(request.body)
        d = data.get("distance")
        m = data.get("mileage")
        fuel = data.get("fuel_price")
        fuel_required = d / m
        total_cost = fuel_required * fuel
        result = {
            "Distance" : d,
            "Mileage" : m,
            "Fuel Price" : fuel,
            "Fuel Required" : fuel_required,
            "Total Cost" : total_cost
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt, name = 'dispatch')
class ProductProfitView(View):
    def post(self, request):
        data = json.loads(request.body)
        cost = data.get("cost_price")
        selling = data.get("selling_price")
        q = data.get("quantity")
        total_cost = cost * q
        total_sales = selling * q
        profit = total_sales - total_cost
        result = {
            "Cost Price" : cost,
            "Selling Price" : selling,
            "Quantity" : q,
            "Total Cost" : total_cost,
            "Total Sales" : total_sales,
            "Profit" : profit
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt, name = 'dispatch')
class WorkSalaryView(View):
    def post(self, request):
        data = json.loads(request.body)
        hours = data.get("hours_worked")
        regular = data.get("regular_hours")
        rate = data.get("hourly_rate")
        overtime = data.get("overtime_rate")
        regular_pay = regular * rate
        overtime_hours = hours - regular
        overtime_pay = overtime_hours * overtime
        total_salary = regular_pay + overtime_pay
        result = {
            "Hours Worked" : hours,
            "Regular Hours" : regular,
            "Hourly Rate" : rate,
            "Overtime Rate" : overtime,
            "Regular Pay" : regular_pay,
            "Overtime Hours" : overtime_hours,
            "Overtime Pay" : overtime_pay,
            "Total Salary" : total_salary
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt, name = 'dispatch')
class AgeDaysView(View):
    def post(self, request):
        data = json.loads(request.body)
        age = data.get("age")
        months = age * 12
        weeks = age * 52
        days = age * 365
        result = {
            "Age" : age,
            "Months" : months,
            "Weeks" : weeks,
            "Days" : days
        }
        return JsonResponse(result)