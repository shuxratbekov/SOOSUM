from rest_framework.serializers import ModelSerializer
from .models import *


class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class DiscountSerializer(ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class AboutProductSerializer(ModelSerializer):
    class Meta:
        model = AboutProduct
        fields = "__all__"


class AboutCompanySerializer(ModelSerializer):
    class Meta:
        model = AboutCompany
        fields = "__all__"


class WhoUseSerializer(ModelSerializer):
    class Meta:
        model = WhoUse
        fields = ('id', 'title_uz', 'title_ru')


class HowToUseSerializer(ModelSerializer):
    class Meta:
        model = HowToUse
        fields = "__all__"


class FactSerializer(ModelSerializer):
    class Meta:
        model = Fact
        fields = "__all__"
