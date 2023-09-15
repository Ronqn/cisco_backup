from netmiko import ConnectHandler
import getpass
import csv
import subprocess

def ping(address):
    return subprocess.run(['ping',address,'-n','2'],stdout=subprocess.DEVNULL)

user = input("Enter the SSH username : ")
passwd = getpass.getpass('Enter the password : ')

with open('switches.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        csv_hostname = row[0]
        csv_device = row[1]

        alive = ping(csv_device)

        if alive.returncode==0:
            net_connect = ConnectHandler(
                device_type="cisco_ios",
                host=csv_device,
                username=user,
                password=passwd
            )

            hostname_output = net_connect.send_command("show conf | i hostname")
            device_hostname = csv_hostname.replace('hostname ','')

            running_config = net_connect.send_command("show run")

            with open(f"{device_hostname}.txt", "w") as config_file:
                config_file.write(running_config)

            net_connect.disconnect()
            print("The running config of " + csv_hostname + " has been successfully saved.")
        else:
            print("The host " + csv_hostname + " " + csv_device + " did not respond to the ping... The config failed to save.")