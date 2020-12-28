# GVE_Devnet_MerakiMV_UCM_Integration

Automatic process to detect vehicles via Meraki Camera and trigger a phone call.


| :exclamation:  External repository notice   |
|:---------------------------|
| This repository is now mirrored at "PLEASE UPDATE HERE - add External repo URL after code review is completed"  Please inform a https://github.com/gve-sw/ organization admin of any changes to mirror them to the external repo |

## Contacts
* Eda Akturk (eakturk@cisco.com)
* Gerardo Chaves (gchaves@cisco.com)

## Solution Components
*  Python 3.8
*  Meraki MV Camera (2nd generation)
*  CUCM
*  IP Phone
*  MongoDB


## Installation/Configuration

#### Clone the repo :
```$ git clone (link)```

#### *(Optional) Create Virtual Environment :*
Initialize a virtual environment 

```virtualenv venv```

Activate the virtual env

*Windows*   ``` venv\Scripts\activate```

*Linux* ``` source venv/bin/activate```

Now you have your virtual environment setup and ready

#### Install the libraries :

```$ pip install -r requirements.txt```


## Setup: 

*Meraki MV Camera Connection*
1. Obtain the Meraki API key and add it to env_var.py file. You can find details on how to obtain the Meraki API key [here.](https://developer.cisco.com/meraki/api-v1/#authorization)
```
MERAKI_API_KEY= " "
```
2. Add your Network ID and Camera Serial to the mv_mqtt.py file. 
```
NETWORK_ID = " "
CAMERA_SERIAL = " "
```
*MQTT Setup*

3. In the Meraki dashboard, go to Cameras > [Camera Name] > Settings > Sense page.

4. Click to Add or Edit MQTT Brokers > New MQTT Broker and add you broker information. For testing/trial you can find public broker at [here](https://github.com/mqtt/mqtt.github.io/wiki/public_brokers).

5. Add the MQTT Server settings to the env_var.py file.
```
MQTT_SERVER = " "
MQTT_PORT = " "
```

*CUCM Connection*

6.  Add the username, password and base_url for the CUCM. Additionally add the phone number to dial when a vehicle is seen. 
```
username = " "
password = " "
base_url = " "
phone_number = ""
```

*(Optional) Database Connection*

7. Download and Install MongoDB. 

8. Create a collection and add the Database, Cluster and Collection credentials to env_var.py.  
```
Database = " "
Cluster = " "
Collection = " "
```
Now you have completed the setup and are ready to run the script. 

## Usage: 
Run the python script
```
    $ python main.py
```
When a car is detected the a MQTT broker will send a notification to the python program. Once the notification is received a phone call will be made. The number of vehicles will be saved to the database with the timestamps. 


# Screenshots

![/pov.PNG](/pov.PNG)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
