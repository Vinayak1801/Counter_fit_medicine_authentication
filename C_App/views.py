from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from web3 import Web3, HTTPProvider
import qrcode
import json
# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
compiled_contract_path = r"D:\blockchain\node_modules\.bin\build\contracts\Structreq.json"
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x5302D2fB1964e6F55f53119E90b1A5f5B54F1Ce1'
from C_App.models import *

def login(request):
    return render(request,'indexlogin.html')
def logincode(request):
    uname=request.POST['textfield']
    pswd=request.POST['textfield2']
    try:
        ob=login_table.objects.get(username=uname,password=pswd)
        if ob.type=="admin":
            request.session['lid'] = ob.id
            return HttpResponse('''<script> alert("Welcome");window.location='/admin_home'</script>''')
        elif ob.type == "distributor":
            request.session['lid'] = ob.id
            return HttpResponse('''<script> alert("Welcome");window.location='/distr'</script>''')
        elif ob.type == "shop":
            request.session['lid'] = ob.id
            return HttpResponse('''<script> alert("Welcome");window.location='/shop_shop'</script>''')
        else:
            return HttpResponse('''<script> alert("Invalid");window.location='/'</script>''')
    except:
        return HttpResponse('''<script> alert("Invalid");window.location='/'</script>''')

def logout(request):
    request.session.clear()
    return redirect('/')

def admin_home(request):
    return render(request,'Admin/adminindex.html')


def mng_data(request):
    ob = dataset_table.objects.all()
    return render(request,'Admin/manage dataset.html',{'val':ob})
def add_question(request):
    Question = request.POST['textfield']
    Answer = request.POST['textfield2']

    question_obj = dataset_table()
    question_obj.question = Question
    question_obj.answer = Answer
    question_obj.save()

    return HttpResponse('''<script> alert("Question added");window.location='/mng_data'</script>''')


def deletequestion(request,id):
    ob=dataset_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert("Deleted");window.location='/mng_data'</script>''')



def mng_data2(request):
    return render(request,'Admin/manage dataset2.html')


def adddataset(request):
    a=request.POST['textfield']
    b=request.POST['textfield2']
    ob=dataset_table()
    ob.question=a
    ob.answer=b
    ob.save()
    return HttpResponse('''<script> alert("added");window.location='/mng_data'</script>''')


def mng_prdt(request):
    ob = stock_table.objects.all()
    return render(request,'Admin/manage product.html',{'val':ob})


def search_prdt(request):
    cate=request.POST['select']
    ob = stock_table.objects.filter(PRODUCT__category=cate)
    return render(request,'Admin/manage product.html',{'val':ob})


def search_prdt_distri(request):
    cate=request.POST['select']
    ob = product_table.objects.filter(category__istartswith=cate)
    product_ids = ob.values_list('id', flat=True)
    ob1 = request_from_distributor.objects.filter(PRODUCT_id__in=product_ids)
    return render(request,'Distributor home/view request status.html',{'val':ob1})

def search_status_distri(request):
    cate=request.POST['select']
    ob = product_table.objects.filter(PRODUCT__category=cate)

    return render(request,'Distributor home/View product and send request.html',{'val':ob})

def deleteproduct(request,id):
    ob=product_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert("Deleted");window.location='/mng_prdt'</script>''')




def mng_prdt2(request):
    return render(request,'Admin/manage product2.html')

def add_product(request):
    print(request.POST,"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    ProductName = request.POST['textfield']
    Price = request.POST['textfield2']
    Stock = request.POST['textfield3']
    Category = request.POST['textfield4']
    Image = request.FILES['file']
    ManufactureDate = request.POST['datefield']
    ExpiryDate = request.POST['datefield2']
    fss = FileSystemStorage()
    image_file = fss.save(Image.name, Image)

    product_obj = product_table()
    product_obj.product_name = ProductName
    product_obj.image = image_file
    product_obj.price = Price
    product_obj.category = Category
    product_obj.manufactufre_date = ManufactureDate
    product_obj.expiry_date = ExpiryDate
    product_obj.save()

    stock_obj = stock_table()
    stock_obj.stock  = Stock
    stock_obj.PRODUCT = product_obj
    stock_obj.save()
    return HttpResponse('''<script> alert("product added");window.location='/mng_prdt'</script>''')


def edit_prdt(request,id):
    request.session['ed']=id
    ob=stock_table.objects.get(PRODUCT__id=id)
    ob1=product_table.objects.get(id=ob.id)
    return render(request,'Admin/edit_prdct.html',{"val":ob1,'val1':ob})

def edit_product(request):
   try:
       ProductName = request.POST['textfield']
       Price = request.POST['textfield2']
       Stock = request.POST['textfield3']
       Category = request.POST['textfield4']
       Image = request.FILES['file']
       ManufactureDate = request.POST['datefield']
       ExpiryDate = request.POST['datefield2']
       fss = FileSystemStorage()
       image_file = fss.save(Image.name, Image)

       product_obj = product_table.objects.get(id=request.session['ed'])
       product_obj.product_name = ProductName
       product_obj.image = image_file
       product_obj.price = Price
       product_obj.category = Category
       product_obj.manufactufre_date = ManufactureDate
       product_obj.expiry_date = ExpiryDate
       product_obj.save()

       stock_obj = stock_table.objects.get(id=request.session['ed'])
       stock_obj.stock = Stock
       stock_obj.PRODUCT = product_obj
       stock_obj.save()
       return HttpResponse('''<script> alert("product updated");window.location='/mng_prdt'</script>''')
   except:
       ProductName = request.POST['textfield']
       Price = request.POST['textfield2']
       Stock = request.POST['textfield3']
       Category = request.POST['textfield4']

       product_obj = product_table.objects.get(id=request.session['ed'])
       product_obj.product_name = ProductName
       product_obj.price = Price
       product_obj.category = Category
       product_obj.save()

       stock_obj = stock_table.objects.get(id=request.session['ed'])
       stock_obj.stock = Stock
       stock_obj.PRODUCT = product_obj
       stock_obj.save()
       return HttpResponse('''<script> alert("product added");window.location='/mng_prdt'</script>''')


def send_reply(request,id):
    request.session['ab']=id
    return render(request,'Admin/send reply.html')
def sendreply(request):
    reply=request.POST['textfield']

    ob=complaint_table.objects.get(id=request.session['ab'])
    ob.reply=reply
    ob.save()
    return HttpResponse('''<script> alert("Reply sent");window.location='/view_complnt'</script>''')


def ver_distr(request):
    ob=distributor_table.objects.all()
    return render(request,'Admin/Verify distributor.html',{'val':ob})


def accept_distributor(request,id):
    obj = login_table.objects.get(id=id)
    obj.type = "distributor"
    obj.save()
    return HttpResponse('''<script> alert("accepted");window.location='/ver_distr'</script>''')

def reject_distributor(request,id):
    obj = login_table.objects.get(id=id)
    obj.type = "Rejected"
    obj.save()
    return HttpResponse('''<script> alert("rejected");window.location='/ver_distr'</script>''')


def ver_prdct(request):
    ob = request_from_distributor.objects.all()
    return render(request,'Admin/verify product request.html',{'val':ob})


def search_prdct(request):
    prdt = request.POST['select']
    ob = request_from_distributor.objects.filter(PRODUCT__product_name__istartswith=prdt)
    return render(request,'Admin/verify product request.html',{'val':ob})

def search_shop(request):
    name = request.POST['select']
    ob = request_from_distributor.objects.filter(PRODUCT__product_name__istartswith=name)
    return render(request,'Admin/verify product request.html',{'val':ob})



def accept_product(request,id):
    obj = request_from_distributor.objects.get(id=id)
    obj.status = "Accept"
    obj.save()
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    for i in range(int(obj.quantity)):
        ob = distributor_product_table()
        ob.PRODUCT = product_table.objects.get(id=obj.PRODUCT.id)
        ob.DISTRIBUTOR = distributor_table.objects.get(id=obj.DISTRIBUTOR.id)
        ob.status = "available"
        ob.date = datetime.now()
        ob.save()

        #     blockchain connection
        ob1 = qrcode.QRCode(
            version=1,  # The QRcode version (1-40), higher is a larger code.
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H).
            box_size=10,  # The size of each box in the QRcode.
            border=4,  # The border size around the QRcode.
        )
        # Add data to the QRcode
        ob1.add_data(str(ob.id))
        ob1.make(fit=True)

        # Create a PIL (Python Imaging Library) image from the QRcode data
        ob1 = ob1.make_image(fill_color="black", back_color="white")
        # Save the image to a file or display it
        ob1.save("media/qr/" + str(ob.id) + ".png")
        blocknumber = web3.eth.get_block_number()
        try:
            message2 = contract.functions.addreq(blocknumber + 1, str(request.session['lid']),
                                                 str(ob.DISTRIBUTOR.id),
                                                 str(ob.id), str(1),
                                                 str(datetime.today()), 'distributer request'
                                                 ).transact({'from': web3.eth.accounts[0]})
        except Exception as e:
            print(e,"========================================")
            print(e,"========================================")
            print(e,"****************************************")

    return HttpResponse('''<script> alert("accepted");window.location='/ver_prdct'</script>''')






def reject_product(request,id):
    obj = request_from_distributor.objects.get(id=id)

    pr=stock_table.objects.get(id=obj.PRODUCT.id)
    qty=int(pr.stock)+int(obj.quantity)
    pr.stock=qty
    pr.save()


    obj.status = "Reject"
    obj.save()
    return HttpResponse('''<script> alert("rejected");window.location='/ver_prdct'</script>''')


def ver_shop(request):
    ob = shop_table.objects.all()
    return render(request,'Admin/verify shop.html',{'val':ob})

def search_shop(request):
    shp= request.POST['select']
    ob = shop_table.objects.filter(LOGIN__shop_table__shop_name=shp)
    return render(request,'Admin/verify shop.html',{'val':ob})

def accept_shop(request,id):
    obj = login_table.objects.get(id=id)
    obj.type = "shop"
    obj.save()
    return HttpResponse('''<script> alert("accepted");window.location='/ver_shop'</script>''')

def reject_shop(request,id):
    obj = login_table.objects.get(id=id)
    obj.type = "Rejected"
    obj.save()
    return HttpResponse('''<script> alert("rejected");window.location='/ver_shop'</script>''')

def accept_shop_req(request,id):
    obj = request_from_shop.objects.get(id=id)
    obj.status="accepted"
    obj.save()
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    ob = distributor_product_table.objects.filter(DISTRIBUTOR__id=obj.DISTRIBUTOR_request.id,PRODUCT__id=obj.PRODUCT.id, status='Available')
    if len(ob)>=int(obj.quantity):
        for i in range(int(obj.quantity)):
            obp=distributor_product_table.objects.get(id=ob[i].id)
            obp.status="na"
            obp.save()

            obsp=shop_product_table()
            obsp.PRODUCT = obp
            obsp.SHOP = shop_table.objects.get(id=obj.SHOP.id)
            obsp.status = 'Available'
            obsp.date =datetime.today()
            obsp.save()


            blocknumber = web3.eth.get_block_number()
            try:
                message2 = contract.functions.addreq(blocknumber + 1, str(request.session['lid']),
                                                     str(obsp.SHOP.LOGIN.id),
                                                     str(obp.id), str(1),
                                                     str(datetime.today()), 'shop request'
                                                     ).transact({'from': web3.eth.accounts[0]})
            except Exception as e:
                    print(e, "========================================")
                    print(e, "========================================")
                    print(e, "****************************************")



    else:

        obj.status = "Rejected"
        obj.save()

    return HttpResponse('''<script> alert("accepted");window.location='/dist_view_req'</script>''')

def reject_shop_req(request,id):
    obj = request_from_shop.objects.filter(id=id).update(status="rejected")
    return HttpResponse('''<script> alert("rejected");window.location='/dist_view_req'</script>''')

def view_complnt(request):
    ob = complaint_table.objects.all()
    return render(request,'Admin/view complaintand send reply.html',{'val':ob})


def search_complnt(request):
    comp = request.POST['select']
    ob = complaint_table.objects.filter(USER__complaint_table__date=comp)
    return render(request,'Admin/view complaintand send reply.html',{'val':ob})




def block_unblock(request):
    ob = distributor_table.objects.exclude(LOGIN__type="pending")
    return render(request,'Admin/block and unblock distributor.html',{'val':ob})

def block_distributor(request,id):
    obj = login_table.objects.get(id=id)
    obj.type = "block"
    obj.save()
    return HttpResponse('''<script> alert("Blocked");window.location='/block_unblock'</script>''')



def unblock_distributor(request,id):
    obj = login_table.objects.get(id=id)
    obj.type = "distributor"
    obj.save()
    return HttpResponse('''<script> alert("Unblocked");window.location='/block_unblock'</script>''')


def view_rating(request):
    ob = feedback_table.objects.all()
    return render(request,'Admin/Viewrating and feedback.html',{'val':ob})

def view_rating_distr(request):
    ob = feedback_table.objects.all()
    return render(request,'Distributor home/view feedback and rating.html',{'val':ob})

def view_rating_distr_search(request):
    search = request.POST['select']
    ob = feedback_table.objects.all()
    return render(request,'Distributor home/view feedback and rating.html',{'val':ob})

def distr(request):
    return render(request,'Distributor home/disindex.html')

def dist_reg(request):
    return render(request,'Distributor home/reg2.html')

def dist_stock(request, id):
    request.session['s_id'] = id
    return render(request,'Distributor home/stock.html')


def stock_update_post(request):
    stock = request.POST['textfield']
    ob = request_from_distributor.objects.get(id=request.session['s_id'])
    ob.quantity = ob.quantity + int(stock)
    ob.save()
    return HttpResponse('''<script> alert("stock added");window.location='/dist_up_stock#about'</script>''')

def dist_up_stock(request):

    obx=stock_table.objects.all()


    ls=[]

    for i in obx:

        oo = distributor_product_table.objects.filter(DISTRIBUTOR__LOGIN__id=request.session['lid'], PRODUCT__id=i.PRODUCT.id, status='Available')

        # ob = request_from_distributor.objects.filter(DISTRIBUTOR__LOGIN__id=request.session['lid'],status='Accept',PRODUCT=i.PRODUCT.id)
        # qt=0
        # for j in ob:
        #     qt=qt+int(j.quantity)

        r={"id":i.id,"pname":i.PRODUCT.product_name,"image":i.PRODUCT.image.url,"price":i.PRODUCT.price,"qt":str(len(oo))}
        ls.append(r)


    # return render(request,'Distributor home/update stock.html',{'val':ob})
    return render(request,'Distributor home/update stock.html',{'val':ls})

def dist_up_stock_search(request):
    search = request.POST['select']


    ob = request_from_distributor.objects.filter(PRODUCT__category__istartswith=search,DISTRIBUTOR__LOGIN__id=request.session['lid'],status='Accept')
    return render(request,'Distributor home/update stock.html',{'val':ob, 'search': search})

def dist_feedback(request):
    ob = feedback_table.objects.all()
    return render(request,'Distributor home/view feedback and rating.html',{'val':ob})

def dist_view_prdt(request):
    ob = stock_table.objects.all()
    return render(request,'Distributor home/View product and send request.html',{'val':ob})

def dist_view_prdt_search(request):
    search = request.POST['select']
    ob = stock_table.objects.filter(PRODUCT__category=search)
    return render(request,'Distributor home/View product and send request.html',{'val':ob, 'search': search})

def dist_view_prdt2(request,id):
    ob=stock_table.objects.get(id=id)
    request.session['stock_id'] = id
    print(ob.PRODUCT.image)
    return render(request,'Distributor home/View product and send request2.html',{"val":ob})

def send_request_destr(request):
    quantity = request.POST['textfield5']
    ob = stock_table.objects.get(id=request.session['stock_id'])

    if ob.stock >=int(quantity):
        ob1 = request_from_distributor()
        ob1.PRODUCT = product_table.objects.get(id=ob.PRODUCT.id)
        ob1.DISTRIBUTOR = distributor_table.objects.get(LOGIN_id=request.session['lid'])
        ob1.status="pending"
        ob1.date=datetime.now()
        ob1.quantity = quantity
        ob1.save()
        ob.stock = ob.stock-int(quantity)
        ob.save()
        return HttpResponse('''<script> alert("Request send successfully");window.location='/dist_view_prdt#about'</script>''')

    else:
        return HttpResponse(
            "<script> alert('Out of stock');window.location='/dist_view_prdt2/"+str(request.session['stock_id'])+"#about'</script>")


def dist_view_req(request):
    ob = request_from_shop.objects.filter(status="pending")
    return render(request,'Distributor home/view request for product from shop.html',{'val':ob})

def dist_view_req_search(request):
    search = request.POST['select']
    ob = request_from_shop.objects.filter(status="pending", PRODUCT__category__istartswith=search )
    return render(request,'Distributor home/view request for product from shop.html',{'val':ob, 'search': search})

def dist_view_req_stat(request):
    ob = request_from_distributor.objects.filter(DISTRIBUTOR__LOGIN=request.session["lid"])
    return render(request,'Distributor home/view request status.html',{'val':ob})

def dist_home(request):
    return render(request,'Distributor home/disindex.html')

def shop_add_bill(request):

    print(request.session['lid'],'================')
    ob = bill_table.objects.filter(SHOP__LOGIN__id=request.session['lid'])
    print(ob,"+++++++++++")
    return render(request,'Shop home/add and manage bill.html',{'val':ob})

def shop_view_product_bill(request,id):
    # ob = order_details.objects.filter(ORDER__id=id)
    ob = bil_details.objects.filter(BILL__id=id)
    return render(request,'Shop home/add and manage bill_view.html',{'val':ob})

def shop_add_bill1(request):
    return render(request,'Shop home/add and manage bill1.html')

def shop_add_bill2(request):
    ob=shop_product_table.objects.filter(SHOP__LOGIN__id=request.session['lid'])
    r=[]
    cat=[]
    print(ob,"")
    for i in ob:
        r.append(i.PRODUCT.PRODUCT.id)
        if i.PRODUCT.PRODUCT.category not in cat:
            cat.append(i.PRODUCT.PRODUCT.category )
    print(r)
    ob = product_table.objects.filter(id__in=r)
    for i in ob:
        ob1=shop_product_table.objects.filter(PRODUCT__PRODUCT__id=i.id,SHOP__LOGIN__id=request.session['lid'],status='Available')
        i.s=len(ob1)
    print(ob)
    return render(request,'Shop home/add and manage bill2.html',{'val':ob,"cat":cat})

def shop_add_bill2s(request):
    s=request.POST['c']
    ob=shop_product_table.objects.filter(SHOP__LOGIN__id=request.session['lid'],PRODUCT__PRODUCT__category__startswith=s)
    r=[]
    cat=[]
    for i in ob:
        r.append(i.PRODUCT.id)
        if i.PRODUCT.PRODUCT.category not in cat:
            cat.append(i.PRODUCT.PRODUCT.category)
    ob = product_table.objects.filter(id__in=r)
    for i in ob:
        ob1=shop_product_table.objects.filter(PRODUCT__PRODUCT__id=i.id,SHOP__LOGIN__id=request.session['lid'],status='Available')
        i.s=len(ob1)
    return render(request,'Shop home/add and manage bill2.html',{'val':ob,"cat":cat,"c":s})

def bill2(request,id):
    request.session['oo']=id
    ob = stock_table.objects.get(id=id)
    return render(request,'Shop home/bill2.html',{'val':ob})


def finish_bill(request):

    return render(request,'Shop home/billfinish.html')


def finish_bill1(request):
    name=request.POST['n']
    phone=request.POST['p']
    ob=bill_table.objects.filter(SHOP__LOGIN__id=request.session['lid'],status='bill')






    if len(ob)==1:
        obb=ob[0]

        obb.status='completed'

        obb.user=name
        obb.phone=phone
        obb.save()

        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
        ob1=bil_details.objects.filter(BILL__id=obb.id)
        for i in ob1:
            obs=shop_product_table.objects.filter(SHOP__LOGIN__id=request.session['lid'],PRODUCT__PRODUCT__id=i.SHOP_PRODUCT.id,status='Available')
            for j in range(int(i.quantity)):
                obp=shop_product_table.objects.get(id=obs[j].id)
                obp.status="na"
                obp.save()
                blocknumber = web3.eth.get_block_number()
                try:
                    message2 = contract.functions.addreq(blocknumber + 1, str(request.session['lid']),
                                                         str(name),
                                                         str(obp.PRODUCT.id), str(1),
                                                         str(datetime.today()), 'shop bill'
                                                         ).transact({'from': web3.eth.accounts[0]})
                except Exception as e:
                    print(e, "========================================")
                    print(e, "========================================")
                    print(e, "****************************************")
    else:
        return HttpResponse('''<script> alert("Invalid");window.location='/shop_add_bill2#about'</script>''')

    return HttpResponse('''<script> alert("FINISHED");window.location='/shop_add_bill#about'</script>''')


def addbill(request):
    quantity=request.POST['textfield']
    ob=bill_table.objects.filter(SHOP__LOGIN__id=request.session['lid'],status='bill')
    if len(ob)==0:
        obb=bill_table()
        obb.SHOP=shop_table.objects.get(LOGIN__id=request.session['lid'])
        obb.status='bill'
        obb.date=datetime.today()
        obb.amount=0
        obb.user=''
        obb.phone=0
        obb.save()
    else:
        obb=ob[0]


    ob=bil_details()
    ob.SHOP_PRODUCT=product_table.objects.get(id=request.session['oo'])
    ob.quantity=quantity
    ob.BILL=obb
    ob.save()
    obb.amount=int(quantity)*int(product_table.objects.get(id=request.session['oo']).price)
    obb.save()
    return HttpResponse('''<script> alert("Added");window.location='/shop_add_bill2#about'</script>''')



def bill3(request):
    ob = product_table.objects.all()
    return render(request,'Shop home/bill3.html',{'val':ob})

def add_bill_post(request):
    pass

def shop_shop(request):
    return render(request,'Shop home/shopindx.html')

def shop_view_distri(request):
    ob = distributor_table.objects.filter(LOGIN__type="distributor")
    return render(request,'Shop home/view distributor.html',{'val':ob})


def shop_view_distrisearch(request):
    name=request.POST['select']
    ob = distributor_table.objects.filter(name=name)
    return render(request,'Shop home/view distributor.html',{'val':ob})

def shop_view_distri1(request,id):
    ok = product_table.objects.all()
    cat=[]
    for i in ok:
        if i.category not in cat:
            cat.append(i.category)
    print("$$$$$$$$$$$$", id)
    request.session['gid']=id
    ob = distributor_product_table.objects.filter(DISTRIBUTOR__id=id,status='Available')
    r=[]
    for i in ob:
        r.append(i.PRODUCT.id)

    ob=product_table.objects.filter(id__in=r)
    for i in ob:
        oo=distributor_product_table.objects.filter(DISTRIBUTOR__id=id,PRODUCT__id=i.id,status='Available')
        i.stock=len(oo)
    return render(request, 'Shop home/checkproduct.html',{'val':ob,'val1':cat})

def send_shop_request(request,id):
    request.session['destr_pro'] = id
    return render(request, "Shop home/sendrequest.html")


def request_sent_shop(request):
    quantity = request.POST['textfield']

    oo = distributor_product_table.objects.filter(PRODUCT=request.session['destr_pro'], status='Available')

    if len(oo)>int(quantity):
        ob = request_from_shop()

        ob.PRODUCT = product_table.objects.get(id=request.session['destr_pro'])
        ob.DISTRIBUTOR_request = distributor_table.objects.get(id=request.session['gid'])
        ob.quantity = quantity
        ob.SHOP = shop_table.objects.get(LOGIN_id=request.session['lid'])
        ob.status = "pending"
        ob.date = datetime.now()
        ob.save()
        return HttpResponse('''<script> alert("Request send successfully");window.location='/shop_view_distri#about'</script>''')
    else:
        return HttpResponse(
            '''<script> alert("out of stock");window.location='/shop_view_distri#about'</script>''')


def shop_view_distri1search(request):

    pid=request.POST['select']

    ok = product_table.objects.all()
    cat = []
    for i in ok:
        if i.category not in cat:
            cat.append(i.category)

    ob = distributor_product_table.objects.filter(DISTRIBUTOR__id=request.session['gid'], status='Available',PRODUCT__category=pid)
    r = []
    for i in ob:
        r.append(i.PRODUCT.id)

    ob = product_table.objects.filter(id__in=r)
    for i in ob:
        oo = distributor_product_table.objects.filter(DISTRIBUTOR__id=request.session['gid'], PRODUCT__id=i.id, status='Available')
        i.stock = len(oo)

    return render(request, 'Shop home/checkproduct.html',{'val':ob,'val1':cat,'pid':pid})


def shop_view_distri2(request):
    return render(request, 'Shop home/sendrequest.html')

def shop_view_feed(request):

    ob = shop_product_table.objects.filter(SHOP__LOGIN__id=request.session['lid'])
    r = []
    for i in ob:
        r.append(i.PRODUCT.id)

    ob = feedback_table.objects.filter(PRODUCT__id__in=r)
    return render(request,'Shop home/view feedback and rating.html',{'val':ob})

def shop_view_req(request):
    ob = request_from_shop.objects.filter(SHOP__LOGIN=request.session["lid"])
    return render(request,'Shop home/view request status.html',{'val':ob})

def shop_reg(request):
    return render(request,'Shop home/reg1.html')
def shop_register(request):
    shopname=request.POST['textfield']
    address=request.POST['textfield2']
    phone=request.POST['textfield3']
    email=request.POST['textfield4']
    ownername=request.POST['textfield5']
    username=request.POST['textfield6']
    password=request.POST['textfield7']
    obb=login_table()
    obb.username=username
    obb.password=password
    obb.type='pending'
    obb.save()
    ob=shop_table()
    ob.shop_name=shopname
    ob.address=address
    ob.phone=phone
    ob.email=email
    ob.owner_details=ownername
    ob.LOGIN=obb
    ob.save()
    return HttpResponse('''<script> alert("added");window.location='/'</script>''')



def distributor_register(request):
    dname=request.POST['textfield']
    daddress=request.POST['textfield4']
    dphone=request.POST['textfield2']
    demail=request.POST['textfield3']
    idproof=request.FILES['textfield5']
    dusername=request.POST['textfield6']
    dpassword=request.POST['textfield7']

    fs=FileSystemStorage()
    fsave=fs.save(idproof.name,idproof)

    obb=login_table()
    obb.username=dusername
    obb.password=dpassword
    obb.type='pending'
    obb.save()
    ob=distributor_table()
    ob.name=dname
    ob.address=daddress
    ob.phone=dphone
    ob.email=demail
    ob.id_proof=fsave
    ob.LOGIN=obb
    ob.save()
    return HttpResponse('''<script> alert("added");window.location='/'</script>''')





from django.core import serializers
import json
from django.http import JsonResponse
def logincode1(request):
    print(request.POST)
    un = request.POST['uname']
    pwd = request.POST['pswd']
    print(un, pwd)
    try:
        ob = login_table.objects.get(username=un, password=pwd)

        if ob is None:
            data = {"task": "invalid"}
        else:
            print("in user function")
            data = {"task": "valid", "lid": ob.id,"type":ob.type}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    except:
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)


def userregistration(request):
    # params.put("", fname);
    # params.put("", lname);
    # params.put("", gender);
    # params.put("age", age);
    # params.put("", address);
    # params.put("", phone);
    # params.put("email", email);
    # params.put("email", email);

    print(request.POST)
    un = request.POST['username']
    pwd = request.POST['password']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    gender = request.POST['gender']
    lname = request.POST['lname']
    fname = request.POST['fname']
    print(un, pwd)
    try:
        ob = login_table()
        ob.username=un
        ob.password=pwd
        ob.type="user"
        ob.save()


        ob1=user_table()
        ob1.LOGIN=ob
        ob1.fname=fname
        ob1.lname=lname
        ob1.gender=gender
        ob1.address=address
        ob1.phone=phone
        ob1.email=email
        ob1.save()


        data = {"task": "valid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    except Exception as e:
        print(e)
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)


def sendfeedbackcode(request):


    print(request.POST)
    lid = request.POST['lid']
    pid = request.POST['pid']
    fbk = request.POST['fbk']
    rat=request.POST['rat']

    try:
        obp=distributor_product_table.objects.get(id=pid)
        ob = feedback_table()
        ob.USER = user_table.objects.get(LOGIN__id=lid)
        ob.feedback = fbk
        ob.rating = rat
        ob.date = datetime.today()
        ob.PRODUCT = product_table.objects.get(id=obp.PRODUCT.id)

        ob.save()


        data = {"task": "valid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    except Exception as e:
        print(e)
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)


def andviewproducts(request):
    print(request.POST)
    b = request.POST['srno']
    pid=b
    # db = Db()
    r = {}
    # qry = "SELECT * FROM `medicine` WHERE id='"+str(b)+"'"
    # res = db.selectOne(qry)
    data = []
    try:
        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
        blocknumber = web3.eth.get_block_number()
        print(blocknumber)
        sollist=[]
        ulist=[]
        for i in range(blocknumber,4, -1):
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])

            # decoded_input[1]['fid']
            print(decoded_input,"=======")
            if int(decoded_input[1]['mid']) == int(b):

                print(decoded_input,"**************************")
                if decoded_input[1]['status']=='distributer request' or decoded_input[1]['status']=='shop request'\
                        or decoded_input[1]['status']=='shop bill':
                    print("ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
                    print(decoded_input[1])
                    # mid = decoded_input[1]['mid'].split('#')
                    sollist.append(decoded_input[1]['status'])
                    ulist.append([decoded_input[1]['fid'],decoded_input[1]['tid'],decoded_input[1]['date']])
                    # ob=medicine_table.objects.get(id=b)
                    # r['med'] = str(ob.name)
                    # r['mf'] = str(ob.mnf_date)
                    # r['exp'] = ob.exp_date
                    # r['qty'] = ob.stock
                    # r['price'] = ob.price
                    # # r['info'] = decoded_input[1]['fid']+"------------>"+decoded_input[1]['tid']
                    # r['status'] = "ok"
                    # sollist.append(r)
                    # return JsonResponse(r,safe=False)
            # else:
            #         r['status'] = "none"
            #         r['med'] = 0
            #         r['mf'] = 0
            #         r['exp'] = 0
            #         r['qty'] = 0
            #         r['price'] = 0
                    # r['info'] = decoded_input[1]['fid']+"------------>"+decoded_input[1]['tid']
            #         sollist.append(r)
                    # return JsonResponse(r,safe=False)
        print(sollist)
        print(ulist)
        print(r, "+===================")

        if len(sollist)==3:
            print("Original","==============")
            obp=shop_table.objects.get(LOGIN__id=ulist[0][0])

            pharmacy=obp.shop_name+" sell to "+ulist[0][1]+" on "+ulist[0][2].split(".")[0]

            obd = distributor_table.objects.get(LOGIN__id=ulist[1][0])

            distributor=obd.name+" sell to "+obp.shop_name+" on "+ulist[1][2].split(".")[0]


            manufracture="Manufracture sell to "+obd.name+" on "+ulist[2][2].split(".")[0]
            r={}
            obb=distributor_product_table.objects.get(id=b)
            ob = obb.PRODUCT
            b = obb.PRODUCT
            r['med'] = str(ob.product_name)
            md = str(ob.manufactufre_date)
            ed = str(ob.expiry_date)
            pr = str(ob.price)
            print(md,ed,pr,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            r['mf'] = str("")
            r['pid'] = str(pid)

            r['qty'] = 123
            r['price'] = ob.price
            r['img'] = ob.image.url
            r['md'] = str(ob.manufactufre_date)
            r['ed'] =  str(ob.expiry_date)

            r['task'] = "product"
            r['manu'] = manufracture
            r['dis'] = distributor
            r['pha'] = pharmacy
            print(manufracture)
            print(distributor)
            print(pharmacy)
            print(r,"==================")
            # return JsonResponse({"r":r,"md":md, "ed":ed, "pr":pr }, safe=False)
            return JsonResponse(r)
        print("++++++++++++++++++++++++++++++++++++++++++++")
        return JsonResponse({"task":"fake"}, safe=False)
    except Exception as e:

        print("Errorr==",e)
        pass
    return JsonResponse({"task": "fake","pid":b}, safe=False)
