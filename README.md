# GVE_Devnet_MerakiMV_UCM_Integration

Automatic process to detect vehicles via Meraki Camera and trigger a phone call.


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
1. Obtain the Meraki API key and add it to `env_var.py` file. You can find details on how to obtain the Meraki API key [here.](https://developer.cisco.com/meraki/api-v1/#authorization)
```
MERAKI_API_KEY= " "
```
2. Add your Network ID and Camera Serial to the `mv_mqtt.py` file. 
```
NETWORK_ID = " "
CAMERA_SERIAL = " "
```
*MQTT Setup*

3. In the Meraki dashboard, go to Cameras > [Camera Name] > Settings > Sense page.

4. Click to Add or Edit MQTT Brokers > New MQTT Broker and add you broker information. For testing/trial you can find public broker at [here](https://github.com/mqtt/mqtt.github.io/wiki/public_brokers).

5. Add the MQTT Server settings to the `env_var.py` file.
```
MQTT_SERVER = " "
MQTT_PORT = " "
```

*CUCM Connection*

6.  Also in the `env_var.py` file, set the values for the following fields:  
```username``` : the CUCM username that is authorized to send XML objects to the phone device  
```password``` : the password corresponding to the CUCM username that is authorized to send XML objects to the phone device  
```base_url``` : the URL on the phone device to send the command to dial where the code will send the XML object; this is typically    "http://XX.XX.XX.XX/CGI/Execute" where XX.XX.XX.XX is the IP address of the IP Phone.   
```phone_number``` : the phone number or extension number to dial when a vehicle is detected.   
You can find more information on the Dial URI, which initiates a new call to a specified number [here.](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/all_models/xsi/9-1-1/CUIP_BK_P82B3B16_00_phones-services-application-development-notes/CUIP_BK_P82B3B16_00_phones-services-application-development-notes_chapter_0101.html#CUIP_RF_DD875CB1_00) For more information about Cisco Unified IP Phone Services App Development please refer to the document [here.](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/all_models/xsi/9-1-1/CUIP_BK_P82B3B16_00_phones-services-application-development-notes/CUIP_BK_P82B3B16_00_phones-services-application-development-notes_chapter_011.html)  


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
