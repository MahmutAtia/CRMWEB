from companies.models import *
import pandas as pd
from django_pandas.io import read_frame
from datetime import date
from rest_framework import serializers
from django.db.models import Case, When, Value, CharField




def run():
    data = Contact.objects.filter(company__user_id=2).\
    order_by('company__country__name', 'company__name', 'date').annotate(
    status_case=Case(
        When(company__status=1, then=Value('Important')),
        When(company__status=0, then=Value('Not Important')),
        default=Value('Normal'),
        output_field=CharField()
    ) )\
    .values('company__country__name', 'company__name', 'company__phone', 'company__email',
            'status_case', 'typ__contact_type', 'date', 'result__contact_result')
    df = read_frame(data)
    today = date.today()
    df.to_excel(f"All_CONTACTS_TILL_{today}.xlsx")
 

