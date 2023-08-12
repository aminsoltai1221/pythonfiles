import ghasedakpack
import json
with open("score-table", "r") as js:
    data = js.read()
    print(data)

# message = f"Hi, {name} Dear! your score is {score}"
# APIKEY = "dab20691840e48319e5d7172d3451f282c3ff19ecabb434c9e15c181d83e7289"
# sms = ghasedakpack.Ghasedak(APIKEY)
# sms.send({'message':message, 'receptor' : '09901491003', 'linenumber': '300002525'})







# # # import ghasedak
# message = "تست ارسال وب سرویس قاصدک"
# receptor = "09901491003"
# linenumber = "300002525"
# sms = ghasedakpack.Ghasedak("dab20691840e48319e5d7172d3451f282c3ff19ecabb434c9e15c181d83e7289")
# sms.send({ 
#         'message': message,  
#         'receptor' : receptor, 
#         'linenumber': linenumber 
#         })