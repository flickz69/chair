import json
import os
class jsonhelper:
   @staticmethod
   def getvar(a1, a2):
       if os.path.exists(f"{a1}") == False:
         print("json/dat doesn't exist create it")
       else:
           with open(f'{a1}', 'r') as v4:
                  data = json.load(v4)
                  v5 = data.get(f"{a2}")
                  return v5
                  
   @staticmethod
   def check(v6):
       if os.path.exists(f"{v6}") == True:
         print(f"{v6} exists")
       else:
            print(f"{v6} is missing")
    