from django.db import models

class login_table(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    type=models.CharField(max_length=30)

class distributor_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    id_proof=models.FileField()

class product_table(models.Model):
    product_name=models.CharField(max_length=100)
    image=models.FileField()
    price=models.FloatField()
    category=models.CharField(max_length=100)
    manufactufre_date=models.DateField()
    expiry_date=models.DateField()

class stock_table(models.Model):
    PRODUCT=models.ForeignKey(product_table, on_delete=models.CASCADE)
    stock=models.IntegerField()

class user_table(models.Model):
    LOGIN=models.ForeignKey(login_table, on_delete=models.CASCADE)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)


class dataset_table(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)



class shop_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    owner_details = models.CharField(max_length=100)




class feedback_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=100)
    rating = models.FloatField()
    date = models.DateField()
    PRODUCT = models.ForeignKey(product_table, on_delete=models.CASCADE)

class complaint_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    date = models.DateField()

class request_from_distributor(models.Model):
    PRODUCT = models.ForeignKey(product_table, on_delete=models.CASCADE)
    DISTRIBUTOR = models.ForeignKey(distributor_table, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    date = models.DateField()



class distributor_product_table (models.Model):
    PRODUCT = models.ForeignKey(product_table, on_delete=models.CASCADE)
    DISTRIBUTOR = models.ForeignKey(distributor_table, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    date = models.DateField()






class request_from_shop(models.Model):
    PRODUCT = models.ForeignKey(product_table, on_delete=models.CASCADE)
    DISTRIBUTOR_request = models.ForeignKey(distributor_table, on_delete=models.CASCADE)
    SHOP = models.ForeignKey(shop_table, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    date = models.DateField()





class shop_product_table (models.Model):
    PRODUCT = models.ForeignKey(distributor_product_table, on_delete=models.CASCADE)
    SHOP = models.ForeignKey(shop_table, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    date = models.DateField()


class order_table(models.Model):
    SHOP = models.ForeignKey(shop_table, on_delete=models.CASCADE)
    USER = models.CharField(max_length=100)
    amount = models.FloatField()
    status = models.CharField(max_length=100)
    date = models.DateField()

class order_details(models.Model):
    ORDER = models.ForeignKey(order_table, on_delete=models.CASCADE)
    PRODUCT = models.ForeignKey(product_table, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class bill_table(models.Model):
    SHOP = models.ForeignKey(shop_table, on_delete=models.CASCADE)
    user = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    amount = models.FloatField()
    status = models.CharField(max_length=100)
    date = models.DateField()


class bil_details(models.Model):
    BILL = models.ForeignKey(bill_table, on_delete=models.CASCADE)
    SHOP_PRODUCT = models.ForeignKey(product_table, on_delete=models.CASCADE)
    quantity = models.IntegerField()
