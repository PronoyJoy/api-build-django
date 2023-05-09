from rest_framework import serializers
from subapp.models import Person,Region



class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields =['name','city']

class PersonSerializer(serializers.ModelSerializer):
    
    # country = RegionSerializer()
    country = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ['id','name', 'age', 'email', 'country']
        #we can use exclude if we want to exclude any field 
        #depth = 1 #whole data

    def get_country(self,obj):
        country_obj = Region.objects.get(name = obj.country.name)
        return {'cityname':country_obj.city,'message':'chol ghure ashi'}
    

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError('Age Must be greater than 18')
        return data
    
    def validate(self, data):
        concern ='(){}[]|`¬¦!"£$%^&*"<>:;#~_-+=,@'
        
        if any (char in concern for char in data['name']):
            raise serializers.ValidationError('Special is Not Allowed') 
        return data
    


        