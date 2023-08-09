import pyodbc
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.209.99.244;DATABASE=rmg;UID=isukisespts3vapp8dt;PWD=wsa0str1vpo@8d5ws')



def get_Partner():
    partner = conn.cursor()
    result=[]
    partner.execute("select intBusinessPartnerId, strBusinessPartnerName, strBusinessPartnerCode, strContactNumber from prt.tblBusinessPartner where isActive=1")
    for row in partner.fetchall():
        item={}
        item["intBusinessPartnerId"]=row[0]
        item["strBusinessPartnerName"]=row[1]
        item["strBusinessPartnerCode"]=row[2]
        item["strContactNumber"]=row[3]
        result.append(item)
    return  result