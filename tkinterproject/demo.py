import socket
# take the server name
host = 'www.travelyaari.com'
try:
    #know the ip address of the website
    addr = socket.gethostbyname(host)
    print('IP Address:'+addr)
except socket.gaierror:  #if get address info error occurs
    print ('The website does not exist')
