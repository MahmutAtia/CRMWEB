from companies.models import *
import pandas as pd
from django_pandas.io import read_frame
from datetime import date


def run():
    df = read_frame(Company.objects.filter(user=2).order_by('country'))
    today = date.today()
    df.to_excel(f"All_COMPANIES_TILL_{today}.xlsx")