from logging import exception
from tkinter import N
from django.shortcuts import render
import pandas as pd 
import sys
from .models import csvfiles,new_data
from .utils import get_plot
from rest_framework.views import APIView
# Create your views here.

class restapi(APIView):
    def post(request):
        csvpath = 'C:\pythons\Bizdata\BIZDATA_BackEnd_TestData.csv'
        data = pd.read_csv(csvpath)
        print(data.head())
        
        for i in range(data.shape[0]):
            print(data['Invoice ID'][i],data['Branch'][i],data['City'][i],data['Customer type'][i],
                data['Gender'][i],data['Product line'][i], data['Unit price'][i],data['Quantity'][i],
                data['Tax 5%'][i],data['Total'][i],data['Date'][i],data['Time'][i], data['Payment'][i],
                data['cogs'][i],data['gross margin percentage'][i], data['gross income'][i],data['Rating'][i])
            
            x = csvfiles.objects.update_or_create(Invoice_ID = data['Invoice ID'][i],Branch =data['Branch'][i],City=data['City'][i],Customer_type=data['Customer type'][i],
                Gender = data['Gender'][i],Product_line = data['Product line'][i], Unit_price = data['Unit price'][i],Quantity = data['Quantity'][i],
                Tax_5pct = data['Tax 5%'][i],Total = data['Total'][i],Date = data['Date'][i],Time = data['Time'][i], Payment = data['Payment'][i],
                cogs = data['cogs'][i],gross_margin_percentage = data['gross margin percentage'][i], gross_income = data['gross income'][i],Rating = data['Rating'][i])
            
            
        value = csvfiles.objects.all().filter(Gender = 'Female')
        
        print(len(value))
        
        data = data[['Date','gross income']]
        data.index = pd.to_datetime(data['Date'])
        data = data.drop(columns=['Date'])
        data_ = data.resample('M').max()
        for i in range(len(data_)):
            x = new_data.objects.update_or_create(date = data_.index[i],gross_income = data_['gross income'][i])
        

        
        bar = get_plot(x = data_['gross income'],data = data_)
        return render(request ,'front-page.html',{'Data':data_.to_html(),'bar':bar})
