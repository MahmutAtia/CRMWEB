from companies.models import *
import pandas as pd
from django_pandas.io import read_frame
from datetime import date


def run():
    objs = Company.objects.filter(user=2, status=1).order_by('country')
    df = read_frame(objs)
    today = date.today()
    df.to_excel(f"All_IMPORTANT_COMPANIES_TILL_{today}.xlsx")