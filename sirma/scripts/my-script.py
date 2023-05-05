
from companies.models import *
import pandas as pd
from pathlib import Path
from accounts.models import User
li = [['İRTİBAT ŞEKLİ 1', 'KAÇINCI İRTİBAT1', 'İRTİBAT TARİHİ 1', 'İRTİBAT SONUCU1', "İRTİBAT PUANI1"], ['İRTİBAT ŞEKLİ2', 'KAÇINCI İRTİBAT2', 'İRTİBAT TARİHİ 2', 'İRTİBAT SONUCU2', "İRTİBAT PUANI2"], ['İRTİBAT ŞEKLİ3', 'KAÇINCI İRTİBAT3', 'İRTİBAT TARİHİ 3', 'İRTİBAT SONUCU3', "İRTİBAT PUANI3"], ['İRTİBAT ŞEKLİ4', 'KAÇINCI İRTİBAT4', 'İRTİBAT TARİHİ 4', 'İRTİBAT SONUCU4', "İRTİBAT PUANI4"], [
    'İRTİBAT ŞEKLİ5', 'KAÇINCI İRTİBAT5', 'İRTİBAT TARİHİ 5', 'İRTİBAT SONUCU5', "İRTİBAT PUANI5", "İRTİBAT PUANI5"], ['İRTİBAT ŞEKLİ6', 'KAÇINCI İRTİBAT6', 'İRTİBAT TARİHİ6', 'İRTİBAT SONUCU6', "İRTİBAT PUANI6"], ['İRTİBAT ŞEKLİ7', 'KAÇINCI İRTİBAT7', 'İRTİBAT TARİHİ 7', 'İRTİBAT SONUCU7', "İRTİBAT PUANI7"], ['İRTİBAT ŞEKLİ8', 'KAÇINCI İRTİBAT8', 'İRTİBAT TARİHİ 8', 'İRTİBAT SONUCU8', "İRTİBAT PUANI8"]]


# date time
from datetime import datetime

#random
import random

def run():

    # delete all objects
    Company.objects.all().delete()
    Country.objects.all().delete()
    Contact.objects.all().delete()
    ContactType.objects.all().delete()
    ContactResult.objects.all().delete()

    path = Path(__file__).resolve().parent / "df.xlsx"
    file = pd.ExcelFile(path)
    df = pd.read_excel(file, "ARAMA LİSTELERİ V.2", header=1)
    for i in range(len(df)):
        row = df.iloc[i, :]

        # get user
        user = User.objects.get(name="mohamed atia")
        # print(user)

        # create or get country
        con, created = Country.objects.get_or_create(name=row['ÜLKE'])

        # status logic
        status = ""
        if row['ÖNEMLİ'] or row["İLGİLENMİYOR"]:
            status = True
        elif row['İLGİLENMİYOR']:
            status = False

        try:
            comp, created = Company.objects.get_or_create(user=user, name=row['FİRMA ADI'] ,
                                                          country=con, email=row['E-POSTA'] ,
                                                          phone=row['TELEFON NUMARASI'] ,
                                                          website=row['WEB SİTESİ'],
                                                          manager=row['FİRMA YETKLİSİ'] ,
                                                          status=status
                                                          )
        except:
            # deal with duplicated name
            company_name = str(row['FİRMA ADI']) + " " + \
                str(row['ÜLKE']) + " duplicated name "  + str(random.randint(0,1000) )    # there is int or float somewere so we convert it to string
                                                                                     # random number to avoid multi duplicated name  

            print(company_name)
            comp, created = Company.objects.get_or_create(user=user, name=company_name,
                                                          country=con, email=row['E-POSTA'],
                                                          phone=row['TELEFON NUMARASI'],
                                                          website=row['WEB SİTESİ'],
                                                          manager=row['FİRMA YETKLİSİ'],
                                                          status=status
                                                          )
    #   company = ("mahmod atia",row['FİRMA ADI'],row['ÜLKE'],row[ 'E-POSTA'],row['TELEFON NUMARASI'],row['WEB SİTESİ'],row['FİRMA YETKLİSİ'],row['ÖNEMLİ'],row['İLGİLENMİYOR'])

        for contact in li:
            if str(row[contact[0]]) != "nan":

                # get or create contact type
                typ, created = ContactType.objects.get_or_create(
                    contact_type=row[contact[0]])

                # get or create contact type
                result, created = ContactResult.objects.get_or_create(
                    contact_result=row[contact[3]])

                # contact time
                contact_time = row[contact[1]]
                if not isinstance(contact_time, int):
                    contact_time = 0

                # Puan
                if contact_time == row[contact[-1]] == 5:
                    comp.status = True

                # check date
                try:
                    date = (str(row[contact[2]]).split(" ")[0])
                    date_object = datetime.strptime(date, '%Y-%m-%d').date()
                except:
                    date_object = None
                
                # print("date_object", date_object)


                # create new contact
                Contact.objects.create(company=comp,
                                       typ=typ ,
                                       date=date_object ,
                                       result=result ,
                                       )
