from rest_framework import serializers,reverse, fields
from companies.models import Company,Contact,Country,ContactType,ContactResult
#pandas
import pandas as pd


#

class CompanySerializer(serializers.ModelSerializer):
    contact_url = serializers.HyperlinkedIdentityField(view_name="companies-api:contact-history",
                                                       lookup_field='pk',read_only=True)
    company_url = serializers.HyperlinkedIdentityField(view_name="companies-api:company-details",
                                                       lookup_field='pk',read_only=True)
    country_name = serializers.CharField(source = "country.name",read_only=True)

    country = serializers.CharField(write_only = True)
    class Meta:
        model = Company
        fields = ["id","name" , "country_name", "country" ,"email", "phone", "website", "manager", "status"
                    ,"company_url","contact_url"]

    def create(self, validated_data):

    

        #recieve country input
        country = validated_data.pop("country")
        #get object
        c = Country.objects.get(name= country)
        print("query is ----",type(c))
        #crate company obj
        company = Company(**validated_data)
        # asgin country
        company.country = c
        # obj.user = fields.CurrentUserDefault()

        #get user 
        user = self.context['request'].user
        print(user)

        #assign user
        company.user = user

        company.save()
        return company  
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        c1 = validated_data.get("country")
       # c2 = validated_data.pop("country")
        obj = Country.objects.get(name=c1)
       # print(obj, type(obj))
        instance.country = obj
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.website = validated_data.get('website', instance.website)
        instance.manager = validated_data.get('manager', instance.manager)
        instance.status = validated_data.get('status', instance.status)

        instance.save()

        return instance

    
        c = Country.objects.get(name = instance.country)
        instance.country = validated_data.get('country', c)
      #  instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

    def get_contact_url(self,obj):
        request = self.context.get("request")
        if request is None:
            return None
        company_pk = obj.company__pk
       
        return reverse.reverse("companies-api:contact-history",kwargs={"pk":company_pk},request=request)

    def get_company_url(self,obj):
        request = self.context.get("request")
        if request is None:
            return None
        pk = obj.pk
       
        return reverse.reverse("companies-api:company-details",kwargs={"pk":pk},request=request)


class ContactSerializer(serializers.ModelSerializer):
    contact_url = serializers.HyperlinkedIdentityField(view_name="companies-api:contact-details",
                                                    lookup_field='pk', read_only = True)
    
    company = serializers.CharField(source = "company.name", read_only = True)
    contact_type = serializers.CharField(write_only = True)
    contact_result = serializers.CharField( write_only = True)


    typ = serializers.StringRelatedField() 
    result = serializers.StringRelatedField()
    class Meta:
        model = Contact
        fields = ["company","contact_type", "typ" ,"date" ,"result","contact_result","contact_url"]
        

    def get_contact_url(self,obj):
        request = self.context.get("request")
        if request is None:
            return None
        contact_id =  obj.pk
        
        return reverse.reverse("companies-api:contact-details",kwargs={"pk":contact_id},request=request)
    
    def create(self, validated_data):
        print(validated_data)

    
        #get company id     
        pk = self.context['view'].kwargs.get('pk')   #I couldn't do it somehow else it was tyring
    
        # get company object
        company = Company.objects.get(pk=pk)
        print(company)

        # get contact type
        typ = validated_data["contact_type"]
        print(typ)
        contact_type = ContactType.objects.get(contact_type=typ)
        print(type(contact_type))
        

        # get contact result
        result = validated_data["contact_result"]
        result = ContactResult.objects.get(contact_result=result)
        print(result)

        

        # create object
        contact = Contact.objects.create(company=company,typ=contact_type,date=validated_data["date"],result=result)
        print(contact)

        

        print(contact)
       
        
        return contact
    
    def update(self, instance, validated_data):

        #update contact type
        typ = validated_data["contact_type"]
        print(typ)
        contact_type = ContactType.objects.get(contact_type=typ)
        instance.typ = contact_type

        #update contact date
        instance.date = validated_data.get('date', instance.date)

        #update contact result
        result = validated_data["contact_result"]
        result = ContactResult.objects.get(contact_result=result)
        print(result)
        instance.result = result

        instance.save()

        return instance
    
   














   
    
# pandas serializer
# class MyModelSerializer(PandasSerializerMixin, serializers.ModelSerializer):
#     class Meta:
#         model = pandas_stats.get_CountryToConmpny()
#         fields = '__all__'
        
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['pandas_data'] = pd.DataFrame(data['pandas_data']).to_dict('records')
#         return data
      


#dummy serilaizer

class StatsSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    country_company = serializers.JSONField()






class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["name"]

class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactType
        fields = ["contact_type"]

class ContactResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactResult
        fields = ["contact_result"]

