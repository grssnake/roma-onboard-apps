#! /usr/bin/python3

import json
import uuid
import time
import requests
import datetime

url_command_get = 'https://ant..ru/robot/getCommands'
url_command_create = 'https://ant..ru/robot/addCommand'
url_command_update = 'https://ant..ru/robot/setCommandStatus'
url_command_status = 'https://ant..ru/robot/getCommandsStatus'

commands = {
  "face": lambda _cmd: "face_"+_cmd['params'],
  "speak": lambda _cmd: 'speak'
}

def face_on(params):
  print(requests.get(url_command_update, params={'id':cmd[0]['id'],'status':'accepted'}))
  print("face on command executed")
  with open("/tmp/face.start", 'w') as f:
    pass
  time.sleep(5)
  return True

def face_off(params):
  print(requests.get(url_command_update, params={'id':cmd[0]['id'],'status':'accepted'}))
  print("face off command executed")
  with open("/tmp/face.stop", 'w') as f:
    pass
  time.sleep(5)
  return True

def tele_on(params):
  print(requests.get(url_command_update, params={'id':cmd[0]['id'],'status':'accepted'}))
  print("face on command executed")
  with open("/tmp/j.start", 'w') as f:
    pass
  time.sleep(5)
  return True

def tele_off(params):
  print(requests.get(url_command_update, params={'id':cmd[0]['id'],'status':'accepted'}))
  print("face off command executed")
  with open("/tmp/j.stop", 'w') as f:
    pass
  time.sleep(5)
  return True

def speak(params):
  print(requests.get(url_command_update, params={'id':cmd[0]['id'],'status':'accepted'}))
  print("face off command executed")
  with open("/tmp/f.stop", 'w') as f:
    pass
  time.sleep(5)
  return True

for i in range(10):
  response = requests.get(url_command_get)
  print(response.status_code)
  try:
    cmd = response.json()
  
    if response.status_code == 200:
      timestamp = time.time()
      date = datetime.datetime.fromtimestamp(timestamp)
      print(date.strftime('%Y-%m-%d %H:%M:%S') + ': command accepted: ' + str(cmd[0]))
    
      c = commands.get(cmd[0]["name"])
      conmmand = c(cmd[0])
      print(conmmand)
      result = eval(conmmand)(cmd[0])
      print(result)
      if result:
        print("Command: ok")
        print(requests.get(url_command_update, params={'id':cmd[0]['id'],'status':'ok'}))
  except Exception as e:
    print("Somthing wrong")
    print("reason: {0}".format(e))
  time.sleep(5)
