from companies.models import *
import pandas as pd
from django_pandas.io import read_frame
from datetime import date
from django.db.models import Case, When, Value, CharField


def run():
    objs = Company.objects.filter(user=2).order_by('country').annotate(
    status_case=Case(
        When(status=1, then=Value('Important')),
        When(status=0, then=Value('Not Interested')),
        default=Value('Normal'),
        output_field=CharField()
    ) )
    df = read_frame(objs)
    today = date.today()
    df.to_excel(f"All_COMPANIES_TILL_{today}.xlsx")