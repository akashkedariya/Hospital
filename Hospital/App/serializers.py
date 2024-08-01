from rest_framework import serializers
from .models import Medical_shop, Doctor_prescription, medicine_distribution



class Medical_shopSerializer(serializers.ModelSerializer) :
    
    class Meta :
        model = Medical_shop
        fields = ["tablet_id","tablet_name","company","price","quantity"]

    # def create(self, validated_data):
    #     print('=======validated_data========',validated_data['price'])
    #     # Customize a field value
    #     validated_data['price'] = 500 + validated_data['price']
    #     validated_data['quantity'] = validated_data['price'] + validated_data['quantity']
    #     return super().create(validated_data)

        


class Doc_presSerializer(serializers.ModelSerializer):

    class Meta :
        model = Doctor_prescription
        fields = ['patient','prescription','adviced','provide']    


class medicine_distributionSerializer(serializers.ModelSerializer):
    class Meta :
        model = medicine_distribution
        fields = ['patient','medicine','total_price']
