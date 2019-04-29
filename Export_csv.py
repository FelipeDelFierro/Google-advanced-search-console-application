import pandas as pd 
import time 
week= (time.strftime("%W"))
hour_path = (time.strftime("%H_%M_%S"))
def export_csv(ListResults):
    count = len(ListResults)
    try:
        if count >0:
            pd.DataFrame(ListResults).to_csv('results_'+ week +'_' + hour_path +'.csv', index=True,encoding='utf-8-sig', mode='w')
            print("Export success! go to folder where is this script.The name of the file is: "+'results_'+ week +'_' + hour_path +'.csv')    
    except Exception as e :
        print(str(e))