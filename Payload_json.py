# from DEV_project.Variables import *
import openpyxl
import json
import requests
import Python.QA_auotomation.Functions as func_var
import _thread

# from DEV_project.Register_Brand import url_one,url_two

loc = 'C:\\Users\\inter\\PycharmProjects\\Projects\\Python\\DEV_project\\WP_brands.xlsx'  # the path to the sheet file of the brands
book = openpyxl.load_workbook(loc)
sh = book.active
locations = {}
test_loc = {}

# email = func_var.email_generator(8)  # Email generator
# login_name = func_var.login_name_generator(6)  # Login name generator
# password = func_var.password_generator()

zip_code = func_var.zip_code_generator()  # Zip code generator
mobile = func_var.mobile_generator()  # Mobile generator
city = func_var.city_generator(6)  # City generator
fname = func_var.city_generator(5)
lname = func_var.city_generator(5)

# print('User: ', 'qqtst_tech_fr')
# print('Pass: ', 'Aa123456')
# print('Email: ', 'technoc@mailinator.com')

# Registration at WP brands
# threadLock = threading.Lock()
errorbrand_api = []
errorbrand_wp = []
def registration(user, pas, email, log_output, brand):
    login_name = user
    password = pas
    my_mail = str(email) + '@mailinator.com'

    for a, b, c in sh:  # a: brand name, b: brand URL, c: WP or API
        brand_exist = []
        locations[a.value] = b.value, c.value
        my_dict_brand = dict(locations.items())

        # Registration at WP brands
        brand_exist.append(str(brand))
        if c.value == 'WP':  # c.value

            payload_stage_one = {
                'Login': login_name,
                'Email': my_mail,
                'Password': password,
                'confirmpsw': password,
                'currency': 'EUR',
                'bonusCode': '',
                'over18': '1',
                'TNCVersion': '17092014_16',
                'TNCType': 'TNC'
            }

            dict_json_one = json.dumps(payload_stage_one, indent=4)

            payload_stage_two = {
                'fname': fname,
                'Country': 'FR',
                'lname': lname,
                'city': city,
                'birthdate': '01/02/1990',
                'address': 'dfhdfh',
                'gender': 'male',
                'zipcode': zip_code,
                'Lang': 'en',
                'mobile': mobile,
            }

            dict_json_two = json.dumps(payload_stage_two, indent=4)

            s = requests.Session()

            try:
                # Stages of the registration
                response_one = s.post(
                    'https://www.' + str(brand) + '/wp-content/plugins/GS_ajax/GS_ajax.php?action=GS_ajaxRegisterUser&lang=en&stage=1',
                    data=payload_stage_one)  # b.value
                response_two = s.post(
                    'https://www.' + str(brand) + '/wp-content/plugins/GS_ajax/GS_ajax.php?action=GS_ajaxRegisterUser&lang=en&stage=-1',
                    data=payload_stage_two)  # b.value

                if str(brand) in brand_exist:
                    _thread.start_new_thread(log_output.insert('end', str(brand + '=Completed ----> API\n')), ())  # a.value
                    break

                else:
                    _thread.start_new_thread(log_output.insert('end', str(brand + '=Completed ----> WP\n')), ()) # a.value
                # list_registered.append(b.value)

            except IOError as e:
                errorbrand_wp.append(a.value)
                continue


        # Registration at API brands

        elif c.value == 'API':  # c.value

            try:
                # Stages of the registration
                url_one = "https://gss." + str(brand) + "/player/1.26/player/registration/1/step1"  # b.value
                url_two = "https://gss." + str(brand) + "/player/1.26/player/registration/1/step2"  # b.value

                payload_stage_one = {
                    'bonusCode': '',
                    'btag': '',
                    'email': my_mail,
                    'language': 'en',
                    'loginName': login_name,
                    'over18': 'True',
                    'password': password,
                    'currency': 'EUR',
                    'signTNC': 'True',
                    'aff_extra_param': ''
                }
                headers = {'content-type': 'application/json', 'Accept': '*/*',
                           'access-control-allow-credentials': 'true',
                           'access-control-expose-headers': 'x-auth-token, Date'}
                r_one = requests.post(url_one, data=json.dumps(payload_stage_one), headers=headers)
                payload_stage_two = {
                    'auth_token': r_one.text[29:-2],
                    'firstName': fname,
                    'lastName': lname,
                    'birthDate': '30/10/1925',
                    'gender': 'M',
                    'language': 'en',
                    'country': 'FR',
                    'city': city,
                    'address': 'en',
                    'zipCode': zip_code,
                    'mobileNumber': mobile,
                    'aff_extra_param': ''
                }

                r_two = requests.post(url_two, data=json.dumps(payload_stage_two), headers=headers)
                # list_registered += b.value

                if str(brand) in brand_exist:
                    _thread.start_new_thread(log_output.insert('end', str(brand + '=Completed ----> API\n')), ()) # a.value
                    break
                else:
                    _thread.start_new_thread(log_output.insert('end', str(brand + '=Completed ----> API\n')), ()) # a.value

            except IOError as e:
                errorbrand_api.append(a.value)  # a.value
                continue

    _thread.start_new_thread(log_output.insert('end', '\nError with the register(API):\n'), ())
    for i in str(errorbrand_api):
        _thread.start_new_thread(log_output.insert('end', str(i)), ())

    _thread.start_new_thread(log_output.insert('end', '\nError with the register(WP):\n'), ())
    for x in str(errorbrand_wp):
        _thread.start_new_thread(log_output.insert('end', str(x)), ())
    #log_output.insert('end', str(errorbrand_wp) + '\n')