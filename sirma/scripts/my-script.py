
from companies.models import *
import pandas as pd
from pathlib import Path
from accounts.models import User
li = [['İRTİBAT ŞEKLİ', 'KAÇINCI İRTİBAT', 'İRTİBAT TARİHİ ', 'İRTİBAT SONUCU'],
['İRTİBAT ŞEKLİ.1', 'KAÇINCI İRTİBAT.1', 'İRTİBAT TARİHİ .1', 'İRTİBAT SONUCU.1'],
['İRTİBAT ŞEKLİ.2', 'KAÇINCI İRTİBAT.2', 'İRTİBAT TARİHİ .2', 'İRTİBAT SONUCU.2'],
['İRTİBAT ŞEKLİ.3', 'KAÇINCI İRTİBAT.3', 'İRTİBAT TARİHİ .3', 'İRTİBAT SONUCU.3'],
['İRTİBAT ŞEKLİ.4', 'KAÇINCI İRTİBAT.4', 'İRTİBAT TARİHİ .4', 'İRTİBAT SONUCU.4'],
['İRTİBAT ŞEKLİ.5', 'KAÇINCI İRTİBAT.5', 'İRTİBAT TARİHİ .5', 'İRTİBAT SONUCU.5'],
['İRTİBAT ŞEKLİ.6', 'KAÇINCI İRTİBAT.6', 'İRTİBAT TARİHİ .6', 'İRTİBAT SONUCU.6'],
['İRTİBAT ŞEKLİ.7', 'KAÇINCI İRTİBAT.7', 'İRTİBAT TARİHİ .7', 'İRTİBAT SONUCU.7']]


# date time
from datetime import datetime

#random
import random

def run():

    # delete all objects
   
    path = Path(__file__).resolve().parent / "df.xlsx"
    file = pd.ExcelFile(path)
    df = pd.read_excel(file, "ARAMA LİSTELERİ V.2", header=1)
    print(df.columns)

    for i in range(len(df)):
        row = df.iloc[i, :]

        
        # print(user)

        # create or get country
        con, created = Country.objects.get_or_create(name=row['ÜLKE'])

        if con.name in  ["Irak","Moritanya","Libya","Saudi Arabistan","Filistin","Ürdün"]:


            # get user
            user = User.objects.get(name="mohamed atia")

        else:
            # get user
            user = User.objects.get(name="chris")

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
                str(row['ÜLKE']) + " duplicated name "  + str(random.randint(1000,100000) )    # there is int or float somewere so we convert it to string
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
