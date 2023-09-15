# Simple Cisco config backup
This is a simple Python script to backup the running-config of multiple switches contained in a CSV file.

## Prerequisites
Install the Netmiko library with pip.

```python
pip install netmiko
```
## Usage
Create a CSV file named **switches.csv** containing the switch in the following format *hostname,ip address*. 

```
SW-NewYork-01,192.168.25.10
SW-SanFran-01,172.16.0.10
SW-Dallas-01,10.0.0.10
```

The CSV file must be located in the same directory as the Python script.

Execute the script.

The script will check the CSV file, ping the device and if the ping is successful, it saves the running config.

The configuration files will be saved in the same directory as the script.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)