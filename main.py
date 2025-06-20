import requests
import time

class BColors:
    CORRECT = '\033[92m'   
    INCORRECT = '\033[91m'  
    NORMAL = '\033[0m'     

while True:
    x = requests.get('https://bacalaureat.edu.ro/2025/rapoarte/rezultate/frame.html')
    
    if x.status_code == 404:
        print(f"{BColors.INCORRECT}Status: 404 Not Found{BColors.NORMAL}")
    else:
        print(f"{BColors.CORRECT}Status: {x.status_code} OK{BColors.NORMAL}")
    
    time.sleep(10) 
