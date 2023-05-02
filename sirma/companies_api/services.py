from companies.models import *
from django_pandas.io import read_frame # **important to convert queryset to pandas df
import pandas as pd


class Stats:
    def __init__(self):
        self.df_company = read_frame(Company.objects.all())
        self.df_contacts = read_frame(Contact.objects.values('id','company_id' ,'typ_id__contact_type',  'date', 'result_id'))
        self.df_contacts.rename(columns={"company_id":"name"}, inplace=True)
        self.df_merge = pd.merge(df_company,df_contacts ,on="name")


    def get_CountryToConmpny(self):
         counts =  self.df_company[["country","name"]].groupby("country").aggregate("count")

         li = []
         for row in counts.iterrows():
             li.append({"country" : row[0], "company_count":row[1][0]})

         return li





def serv():
    df_company = read_frame(Company.objects.all())
    df_contacts = read_frame(Contact.objects.values('id','company_id' ,'typ_id__contact_type',  'date', 'result_id'))
    df_contacts.rename(columns={"company_id":"name"}, inplace=True)
    df_merge = pd.merge(df_company,df_contacts ,on="name")
    return df_company,df_contacts,df_merge



df_company = read_frame(Company.objects.all())
df_contacts = read_frame(Contact.objects.values('id','company_id' ,'typ_id__contact_type',  'date', 'result_id'))
df_contacts.rename(columns={"company_id":"name"}, inplace=True)
df_merge = pd.merge(df_company,df_contacts ,on="name")


stats = {
    "num_of_companies" : df_company.name.count(),
    "country_to_companies" : df_company[["country","name"]].groupby("country").aggregate("count"),
    # "num_of_countries" : df_company["country"].value_counts().to_dict(),
    # "contact_type_count" : df_merge['typ_id__contact_type'].value_counts(),
    # "result_type_count" : df_merge['result_id'].value_counts(),
    # "country_type_count" : (df_merge[["country",'typ_id__contact_type']]).groupby(["country"]).value_counts().to_dict(),
    # "country_result_count" : (df_merge[["country",'result_id']]).groupby(["country",]).value_counts().to_dict()







}

# class Stats:
#     def __init__(self, total, country_company):
#         self.total = total
#         self.country_company = country_company

# stats_1 = Stats(total=stats["num_of_companies"], country_company=stats["country_to_companies"])