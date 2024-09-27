def footer(data):



    footer = {
        "company1": f'''   
Witam!

Z poważaniem

{data["user_fullname"]}
Company name - departement
tel.: {data["user_phone"]}
fax  +48 (32) 750 10 60
email: {data['user_email']}
_____________________________________

rest of the footer
''',
        "company2": f'''
Witam!

Z poważaniem

{data["user_fullname"]}
Company name - departement
tel.: {data["user_phone"]}
email: {data["user_email"]}
_____________________________________

Rest of the footer
'''

    }   
    return footer[data["user_company"]]



