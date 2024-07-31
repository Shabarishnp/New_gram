from django.shortcuts import render,redirect
from django.http import HttpResponse
import pymongo
from .models import *
from django.conf import settings
from django.core.mail import send_mail


my_client = pymongo.MongoClient(settings.DB_NAME)
dbname = my_client['Gram_Panchayat']
category_name = dbname["Category_Details"]
scheme_name=dbname["Scheme_Details"]
registration_table=dbname['User_Registration_Table']
eligibility_table=dbname['Eligibility_Table']
apply_table=dbname["Apply_Table"]
# Create your views here.

def Home(request):
    return render(request,'index.html')

def LoginPage(request):
    return render(request, 'loginpage.html')

def LoginDetails(request):
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['pswd']
        if username=="admin@gmail.com" and password=="admin":
            '''sch=[]
            Number_Of_reg_c=[]
            schemes=scheme_name.find()
            for s in schemes:
                    sch.append(s['schemename'])
            for i in sch:
                Number=str(apply_table.count_documents({'schemename':i}))
                Number_Of_reg_c.append(Number)
            print(sch)
            scheme={"schemename":[sch]}
            Num={"Num":[Number_Of_reg_c]}
            print(Number_Of_reg_c)
            #books= zip(sch,Number_Of_reg_c)
            books=[{"sch":sch,"Num":Number_Of_reg_c}]
            d={'Scheme':sch,"Num":Number_Of_reg_c}'''
            #scheme_count=apply_table.aggregate([{"$group":{'schemename':"$schemename",'count':{'$sum:1'}}}])
            mistries=scheme_name.distinct('ministry')
            sche_count=[]
            for i in mistries:
                count=scheme_name.count_documents({'ministry':i})
                sche_count.append(count)
            print(sche_count)
            print(mistries)
            reg_count=registration_table.find().count()
            app_count=apply_table.find().count()
            scheme_count=scheme_name.find().count()
            category_count=category_name.find().count()
            zipped_data=zip(mistries,sche_count)
            p={'reg_count':reg_count,'app_count':app_count,'scheme_count':scheme_count,'category_count':category_count,'zipped_data':zipped_data}
            return render(request, 'adminpage.html',p)
       
        elif registration_table.count_documents({'emailid': username, 'password':password}):
                request.session['emailid']=username
                return render(request,'userpage.html')
        else:
                 message="Invalid Username or Password"
                 error=True
                 d={'message':message,'error':error}
                 return render(request,'loginpage.html',d)




def AddCategory(request):
    return render(request, 'addcategory.html')


def AddScheme(request):
    category_d=category_name.find()
    d={'category_d':category_d}
    return render(request, 'addscheme.html',d)

def FilterBene(request):
    scheme_d=scheme_name.find()
    print(scheme_d)
    d={'scheme_d':scheme_d}
    return render(request, 'filterbene.html',d)

def Add_Category(request):
    error=False
    if request.method=="POST":
        categoryID=request.POST['categoryID']
        category=request.POST['category']
        myquery={'categoryid':categoryID}
        mydoc=category_name.find(myquery)
        if category_name.count_documents({'categoryid':categoryID}):
            message="Data already exists"
            error=True
            d={'message':message,'error':error}
            return render(request, 'addcategory.html',d)
        else:
            category1= {
                'categoryid':categoryID,
                'category':category
            }
            
            category_name.insert_one(category1)
            category_d=category_name.find()
            d={'category_d':category_d}
            return render(request, 'view_category.html',d)

def View_Category(request):
    category_d=category_name.find()
    d={'category_d':category_d}
    return render(request, 'view_category.html',d)


def View_Scheme(request):
    scheme_d=scheme_name.find()
    d={'scheme_d':scheme_d}
    return render(request,"view_scheme.html",d)

def State_Uts(request):
    return render(request,'state_uts.html')

def Home_Categories(request):
    category_d=category_name.find()
    d={'category_d':category_d}
    return render(request,'home_categories.html',d)

def Home_Ministeries(request):
    scheme_d=scheme_name.find().distinct('ministry')
    d={'scheme_d':scheme_d}
    print(d)
    return render(request,'home_ministeries.html',d)

def Home_Eligibility(request):
    return render(request,'home_eligiblity.html')


def Add_Scheme(request):
    if request.method=="POST":
        category=request.POST['category']
        schemeid=request.POST['schemeid']
        name=request.POST['name']
        mname=request.POST['mname']
        details=request.POST['details']
        benefits=request.POST['benefits']
        applicationprocess=request.POST['applicationprocess']
        documentsrequired=request.POST['documentrequired']
        state=request.POST['state']
        duedate=request.POST['duedate']
        up=0

        if scheme_name.count_documents({'scehmeid':schemeid}):
            message="data already exists"

        else:

            scheme_1={
                'category':category,
                'schemeid':schemeid,
                'schemename':name,
                'ministry':mname,
                'details':details,
                'benefits':benefits,
                'applicationprocess':applicationprocess,
                'documentsrequired':documentsrequired,
                'state':state,
                'duedate':duedate,
                'up':up
            
            }
            scheme_name.insert_one(scheme_1)
            return redirect('addscheme')
    
def Edit_Scheme(request,pid):
    scheme_d=scheme_name.find_one({'schemeid':pid})
    category_d=category_name.find()
    d={'scheme_d':scheme_d,'category_d':category_d}
    return render(request,'edit_scheme.html',d)


def Update_Scheme(request):
    if request.method=="POST":
        category=request.POST['category']
        schemeid=request.POST['schemeid']
        name=request.POST['name']
        mname=request.POST['mname']
        details=request.POST['details']
        benefits=request.POST['benefits']
        applicationprocess=request.POST['applicationprocess']
        documentsrequired=request.POST['documentrequired']
        state=request.POST['state']
        

        if scheme_name.count_documents({'scehmename':name}):
            message="data already exists"

        else:

            scheme_1={
                'category':category,
                
                'schemename':name,
                'ministry':mname,
                'details':details,
                'benefits':benefits,
                'applicationprocess':applicationprocess,
                'documentsrequired':documentsrequired,
                'state':state
                
            
            }
            scheme_name.update_one({'schemeid':schemeid},{"$set":{'category':category,
                'schemename':name,
                'ministry':mname,
                'details':details,
                'benefits':benefits,
                'applicationprocess':applicationprocess,
                'documentsrequired':documentsrequired,
                'state':state}})
            error=True
            message="Data updated successfully"
            scheme_d=scheme_name.find()
            d={'scheme_d':scheme_d,'error':error,'message':message}
            return render(request,'view_scheme.html',d)

def Delete_Scheme(request,pid):
    myquery={"schemeid":pid}
    scheme_name.delete_one(myquery)
    error=True
    message="Scheme Deleted Successfully"
    scheme_d=scheme_name.find()
    d={'error':error,'message':message,'scheme_d':scheme_d}
    return render(request,'view_scheme.html',d)
    
def Register(request):
    return render(request, 'register.html')

def RegisterUser(request):
    if request.method =="POST":
        fullname=request.POST['fullname']
        emailid=request.POST['emailid']
        phoneno=request.POST['phoneno']
        locality=request.POST['Locality']
        address=request.POST['address']
        full_address=locality+" "+address
        state=request.POST['state']
        zip=request.POST['Zip']
        gender=request.POST['gender']
        dob=request.POST['dob']
        mstatus=request.POST['MStatus']
        aor=request.POST['aor']
        caste=request.POST['caste']
        password=request.POST['password']
        age=request.POST['age']
        ph=request.POST['ph']
        minority=request.POST['minority']
        students=request.POST['student']
        empstatus=request.POST['empstatus']
        currempstatus=request.POST['currempstatus']
        occupation=request.POST['occupation']
        category=request.POST['category']
        annualincome=request.POST['annualincome']
        if registration_table.count_documents({'emailid': emailid}):
            message="Data already exists"
            error=True
            d={'message':message,'error':error}
            return render(request, 'register.html',d)

        else:
            user={
                'fullname':fullname,
                'emailid':emailid,
                'phoneno':phoneno,
                'fulladdress':full_address,
                'state':state,
                'zip':zip,
                'gender':gender,
                'dob':dob,
                'mstatus':mstatus,
                'aor':aor,
                'caste':caste,
                'password':password,
                'age':age,
                'ph':ph,
                'minority':minority,
                'student':students,
                'empstatus':empstatus,
                'currrmpstatus':currempstatus,
                'occupation':occupation,
                'category':category,
                'annualincome':annualincome
            }
            
            registration_table.insert_one(user)
            subject = 'Welcome to my government scheme.'
            message = f'You have successfully registered to <b>MY GOVERNMENT SCHEME PORTAL</b>. Please note down your login credentials to contine with portal\n\n <b>Email ID: {emailid} \n \n <b>Password:</b>{password}\n\n Thank You.'
            print(message)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [emailid]
            send_mail( subject, message, email_from, recipient_list )
            error=True
            message="You have registered successfully.Login to continue."
            p={'error':error,'message':message}
            return render(request,'loginpage.html',p)


def View_Scheme_State(request,pid):
    scheme_d=scheme_name.find({'state' : pid})
    print(scheme_d)
    d={'scheme_d':scheme_d}
    return render(request,"state_scheme.html",d)

def User_Page(request):
    return render(request,'userpage.html')

def Add_Eligibility(request,pid):
    scheme_d=scheme_name.find_one({'schemeid' : pid})
    print(scheme_d)
    d={'scheme_d':scheme_d}
    return render(request,"add_eligibility.html",d)

def Add_Eligibility_Value(request):
    if request.method =="POST":
        schemeid=request.POST['schemeid']
        state=request.POST['state']
        gender=request.POST['gender']
        mstatus=request.POST['MStatus']
        aor=request.POST['aor']
        caste=request.POST['caste']
        ph=request.POST['ph']
        minority=request.POST['minority']
        students=request.POST['student']
        empstatus=request.POST['empstatus']
        currempstatus=request.POST['currempstatus']
        occupation=request.POST['occupation']
        category=request.POST['category']
        annualincome=request.POST['annualincome']
        mage=request.POST['mage']
        maxage=request.POST['maxage']

        if eligibility_table.count_documents({'schemeid': schemeid}):
            message="Data already exists"
            error=True
            d={'message':message,'error':error}
            return render(request, 'register.html',d)
        else:
            scheme={
                'schemeid':schemeid,
                'state':state,
                'gender':gender,
                'mstatus':mstatus,
                'aor':aor,
                'caste':caste,
                'mage':mage,
                'maxage':maxage,
                'ph':ph,
                'minority':minority,
                'student':students,
                'empstatus':empstatus,
                'currrmpstatus':currempstatus,
                'occupation':occupation,
                'category':category,
                'annualincome':annualincome
            }
            up=1
            myquery={"schemeid":schemeid}
            newvalue={"$set":{"up":up}}
            scheme_name.update_one(myquery,newvalue)
            eligibility_table.insert_one(scheme)
            scheme_d=scheme_name.find()
            d={'scheme_d':scheme_d}
            return render(request,'view_scheme.html',d)
def View_Beneficiary(request,pid):
    print(pid)
    scheme_d=scheme_name.find_one({'schemeid':pid})
    eligibity_d=eligibility_table.find_one({'schemeid':pid})
    print(eligibity_d)
    user_d=registration_table.find()
    useremailid=[]
    name=[]
    state=[]
    dob=[]
    for u in user_d:
        if u['state']==eligibity_d['state'] and u['gender']==eligibity_d['gender'] and u['mstatus']==eligibity_d['mstatus'] and u['aor']==eligibity_d['aor'] and u['caste']==eligibity_d['caste'] and u['ph']==eligibity_d['ph'] and u['minority']==eligibity_d['minority'] and u['student']==eligibity_d['student'] and u['empstatus']==eligibity_d['empstatus'] and u['currrmpstatus']==eligibity_d['currrmpstatus'] and u['occupation']==eligibity_d['occupation'] and u['category']==eligibity_d['category'] and u['annualincome']==eligibity_d['annualincome'] and u['age']>=eligibity_d['mage'] and u['age']<=eligibity_d['maxage']:
            useremailid.append(u['emailid'])
            name.append(u['fullname'])
            state.append(u['state'])
            dob.append(u['dob'])
    zipped_data=zip(useremailid,name,state,dob)
    d={'zipped_data':zipped_data,'scheme_d':scheme_d}
    return render(request, 'beneficiary_list.html',d)

def Mail_All(request,pid):
    scheme_d=scheme_name.find({"schemeid":pid})
    
    eligibity_d=eligibility_table.find_one({'schemeid':pid})
    scheme_d=scheme_name.find_one({"schemeid":pid})
    d={'scheme_d':scheme_d}
    #print(user_d)
    print(eligibity_d["state"])
    user_d=registration_table.find({"state":eligibity_d['state'],'gender':eligibity_d["gender"],'mstatus':eligibity_d["mstatus"],'aor':eligibity_d["aor"],'caste':eligibity_d["caste"],'ph':eligibity_d["ph"],'minority':eligibity_d["minority"],'student':eligibity_d["student"],'empstatus':eligibity_d["empstatus"],'currrmpstatus':eligibity_d["currrmpstatus"],'occupation':eligibity_d["occupation"],'category':eligibity_d["category"],'annualincome':eligibity_d["annualincome"]})
    schemename=scheme_d["schemename"]

    
    for u in user_d: 
            user_emailid=u["fullname"]
            subject = 'Welcome to my government scheme.'
            message = f'Hi {user_emailid} As per your details provided during registration you are eligible for the following scheme:\n \n {schemename} Please login to apply.'
            print(message)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [u["emailid"]]
            send_mail( subject, message, email_from, recipient_list )
    return redirect('filterbene')



def User_Scheme(request,pid):   
    user_d=registration_table.find_one({'emailid':pid})
    eligibity_d=eligibility_table.find()
    schemeid=[]
    schemename=[]
    details=[]
    applicationprocess=[]
    documentsrequired=[]
    schemeid=[]
    duedate=[]
    applied=[]
    for e in eligibity_d:
        if user_d['state']==e['state'] and user_d['gender']==e['gender'] and user_d['mstatus']==e['mstatus'] and user_d['aor']==e['aor'] and user_d['caste']==e['caste'] and user_d['ph']==e['ph'] and user_d['minority']==e['minority'] and user_d['student']==e['student'] and user_d['empstatus']==e['empstatus'] and user_d['currrmpstatus']==e['currrmpstatus'] and user_d['occupation']==e['occupation'] and user_d['category']==e['category'] and user_d['annualincome']==e['annualincome'] and user_d['age']>=e['mage'] and user_d['age']<=e['maxage']:
            schemeid.append(e['schemeid'])
            scheme_d=scheme_name.find_one({'schemeid':schemeid[0]})
            schemeid.append(scheme_d['schemeid'])
            schemename.append(scheme_d['schemename'])
            details.append(scheme_d['details'])
            applicationprocess.append(scheme_d['applicationprocess'])
            documentsrequired.append(scheme_d['documentsrequired'])
            duedate.append(scheme_d['duedate'])
            if apply_table.count_documents({'emailid':pid,'schemeid':schemeid[0]}):
                apply_d=apply_table.find_one({'emailid':pid,'schemeid':schemeid[0]})
                applied.append(apply_d['up'])
            else:
                applied.append(0)
            print(applied)
            print(schemeid)
    
    zipped_data=zip(schemename,details,applicationprocess,documentsrequired,duedate,schemeid,applied)
    d={"zipped_data":zipped_data}
    return render(request,'scheme_view.html',d)

def Apply_Scheme(request,pid):
    emailid=request.session['emailid']
    user_d=registration_table.find_one({'emailid':emailid})
    scheme_d=scheme_name.find_one({'schemeid':pid})
    fullname=user_d["fullname"]
    #emailid=user_d["emailid"]
    phoneno=user_d["phoneno"]
    schemeid=pid
    schemename=scheme_d["schemename"]
    '''if apply_table.count_documents({'emailid':emailid,'schemename':scheme_name}):
        message="Data already exists"
        error=True
        user_d=registration_table.find_one({'emailid':pid})
        apply_d=apply_table.find_one({'emailid':pid})
        eligibility_d=eligibility_table.find()
        scheme_d=scheme_name.find()
        print(user_d)
        d={'user_d':user_d,'eligibility_d':eligibility_d,'scheme_d':scheme_d,'apply_d':apply_d,'message':message,'error':error}
        return render(request,'scheme_view.html',d)'''
    #else:
    up=1
    apply_u={
            'fullname':fullname,
            'phoneno':phoneno,
            'emailid':emailid,
            'schemeid':pid,
            'schemename':schemename,
            'up':up
        }
    apply_table.insert_one(apply_u)
    message="Applied Successfully"
    error=True
    return redirect('user_scheme',emailid)


def Delete_Category(request,pid):
    category_name.delete_one({'categoryid':pid})
    error=True
    message="Deleted Successfully"
    category_d=category_name.find()
    d={'error':error,'message':message,'category_d':category_d}
    return render(request,'view_category.html',d)

def Edit_Category(request,pid):
    category_d=category_name.find_one({'categoryid':pid})
    d={'category_d':category_d}
    return render(request,'edit_category.html',d)


def Update_Category(request):
    if request.method=="POST":
        categoryID=request.POST['categoryid']
        #print(categoryID)
        category=request.POST['category']
        #print(category)
        if category_name.count_documents({'category':category}):
            message="Data already exists"
            error=True
            category_d=category_name.find()
            d={'category_d':category_d,'error':error,'message':message}
            return render(request, 'view_category.html',d)
        else:
            category_name.update_one({'categoryid': categoryID }, { "$set": {'category': category } })
            error=True
            message="Category Updated Successfully"
            category_d=category_name.find()
            d={'category_d':category_d,'error':error,'message':message}
            return render(request, 'view_category.html',d)

    
def About(request):
    return render(request,'about.html')


        
