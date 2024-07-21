import numpy as np
import pandas as pd

contact_book={}

def Search_name(name):
    search={}
    for key in contact_book:
        if contact_book[key][0]==name:
            search[key]=contact_book[key]
    print("Searching....")
    if len(search)==0:
        print(f"Name {name} is not present in contact book.")
        print(f"Sreach name {name} has been successfully completed....")
        return 
    details=pd.DataFrame(search) 
    details=details.T
    details.columns=["Name","Phone no.","Email","Address"]
    details.reset_index(drop=True,inplace=True)
    print(details)
    print(f"Sreach name {name} has been successfully completed....")



while True:
    operation=int(input("Enter\n1-Add contact\n2-View contact\n3-Search contact\n4-Updata contact\n5-Delete contact\n6-Exit/Stop\n--->"))
    if operation==1:
        name=input("Enter name: ")
        phone=int(input("Enter phone number: "))
        email=input("Enter email: ")
        address=input("Enter Address: ")
        contact_book[phone]=[name,phone,email,address]
        print("Contact details has been successfully added....")
    elif operation==2:
        details=pd.DataFrame(contact_book) 
        details=details.T
        details.columns=["Name","Phone no.","Email","Address"]
        details.reset_index(drop=True,inplace=True)
        print(details)   
    elif operation==3:
        op=int(input("Enter\n1-By Name\n2-By Phone number\n--->"))
        if op==1:
            name1=input("Enter name: ")
            Search_name(name1) 
        elif op==2:
            phone_no=int(input("Enter phone number: "))
            print("Searching....")
            if phone_no in contact_book:
                print("Name: ",contact_book[phone_no][0]) 
                print("Phone no: ",contact_book[phone_no][1]) 
                print("Email: ",contact_book[phone_no][2]) 
                print("Address: ",contact_book[phone_no][3])
            else:
                print("Invalid Phone number.")
            print(f"Searching has been successfully completed....")
    elif operation==4:
        up_name=input("Enter name you want to updata: ")
        up_phone=int(input("Enter phone number you want to updata: "))
        ope=int(input("Enter\n1-Updata name\n2-Updata Phone number\n3-Updata Email\n4-Updata Address\n--->"))
        if ope==1:
            new_name=input("Enter new name: ")
            contact_book[up_phone][0]=new_name
        elif ope==2:
            new_phone=input("Enter new phone number: ")
            contact_book[up_phone][1]=new_phone
        elif ope==3:
            new_email=input("Enter new email: ")
            contact_book[up_phone][2]=new_email
        elif ope==4:
            new_address=input("Enter new address: ")
            contact_book[up_phone][3]=new_address
        else:
            print("Invalid Input!")
        if ope>=1 and ope<=4:
            print("Contact details has been successfully added....")
    elif operation==5:
        delete_name=input("Enter name you want to delete contact details: ")
        delete_phone=int(input("Enter phone number you want to delete contact details: ")) 
        if delete_phone in contact_book:
            contact_book.pop(delete_phone) 
            print(f"{delete_name} details has been successfully deleted....")
        else:
            print("Invalid input!")      
    elif operation==6:
        print("Closing the program....")
        break
    else:
        print("INVALID INPUT!")
