from order.models import *
from rest_framework import serializers
from productAPI.models import ProductModel
from authAPI.models import User
from cart.models import CartItem

class ListItemSerializer(serializers.Serializer):
    product=serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=ProductModel.objects.all()
        )
    quantity=serializers.IntegerField()

class OrderSerializer(serializers.Serializer):
    
    product = serializers.ListField(child=ListItemSerializer())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    status = serializers.CharField( max_length=20, default='Pending')

    def create(self, validated_data, *args, **kwargs):
        user = validated_data.pop('user')
        product_data = validated_data.pop('product')

        # Get cart items for the user
        cart_items = CartItem.objects.filter(cart__user=user)

        # Check if cart items exist
        if cart_items.exists():
            # Create the order
            order = Order.objects.create(user=user)

            # Associate order items with the order
            for item_data in product_data:
                product = item_data['product']
                quantity = item_data['quantity']
                OrderItem.objects.create(order=order, product=product, quantity=quantity)

            # Clear cart items
            cart_items.delete()

            return order  # Return the order object after creating it
        else:
            raise serializers.ValidationError('No items in cart for this user')


class LineItemViewSerializer(serializers.Serializer):
    product_id=serializers.PrimaryKeyRelatedField(queryset=ProductModel.objects.all())
    product=serializers.SlugRelatedField(
        slug_field="product_name",
        queryset=ProductModel.objects.all()   
    )
    quantity=serializers.IntegerField()
    

class OrderViewSerializer(serializers.Serializer):
    created_at=serializers.DateTimeField()
    line_item=serializers.SerializerMethodField()
    status = serializers.CharField()


    def get_line_item(self,instance):
        line_item = OrderItem.objects.filter(order=instance)
        return LineItemViewSerializer(line_item,many=True).data
    


