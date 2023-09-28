### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 1 Lab  -- 28:34

#Write a script to define a Python function and use arguments to display a list network server.

def showServer(serversList):
    for servers in serversList: 
        print(servers)

server_list = ['FTP', 'RAS', 'DHCP', 'AD', 'IIS', 'APACHE', 'DNS']
showServer(server_list)