# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 08:11:25 2022

@author: HP
"""
import json
import time
def datasent():
    x=2
    if x==1:
        from boltiot import Bolt
        api_key="91a27806-4174-4001-9d24-b42a37a3a513"
        device_id="BOLT5778783"
        mybolt=Bolt(api_key,device_id)
        response1=mybolt.digitalRead('0')
        data=json.loads(response1)
        print(data["value"])
        response2=mybolt.digitalRead('1')
        data1=json.loads(response2)
        print(data1["value"])
        #print(response2)
        response3=mybolt.digitalRead('2')
        data2=json.loads(response3)
        print(data2["value"])
        return int(data["value"])+int(data["value"])+int(data["value"])
        time.sleep(2)
        return int(data["value"])+int(data["value"])-int(data["value"])
    if x==2:
        return 2