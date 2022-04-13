import os
import logging
import logging.config
import schedule
import time
import shutil
from dirsync import sync

#put paths to source and replica folders in variables
print("Hi, insert path to source folder")
source_path = input()
print("Great, now insert path to replica folder")
replica_path = input()
print("Now insert how often do you want folders to sync (in minutes)")
time_sync_min = input()

while not time_sync_min.isnumeric():
    print("Please insert number (1,2,3..)")
    time_sync_min = input()

#fill lists with folder content
def source_files():
    source = []
    for x in os.listdir(source_path):
        source.append(x)
    return source

def replica_files():
    replica = []
    for y in os.listdir(replica_path):
        replica.append(y)
    return replica
#print(replica)

#Creating and Configuring Logger
logging.basicConfig(filename = "logfile.log",
                    #filemode = "w",
                    format = '%(asctime)s %(message)s',
                    level = logging.INFO
                    )
logger=logging.getLogger()

#sync files to replica folder
def sync_files(x, y):
    dif = list(set(x) - set(y))
    length_dif = len(dif)
    while length_dif >= 1:
        sync(source_path, replica_path, 'sync', verbose=True)
        length_dif = 0

#copy files from source to replica / This way it would synchronize folders everytime, however it would also put a log in log file
#sync(source_path, replica_path, 'diff', verbose=True)
#sync(source_path, replica_path, 'sync', verbose=True)


#delete files from replica folder that are no longer in source folder
def delete_files(x, y):
    dif = list(set(y) - set(x))
    length_dif = len(dif)
    for x in range(length_dif):
        str1 = ""
        str1 = str1.join(dif[x])
        print(str1)
        remove_path = replica_path + "\\" + str1
        print(remove_path)
        logger.info("Deleted file - " + remove_path)
        os.remove(remove_path)

def execute():
    sync_files(source_files(), replica_files())
    delete_files(source_files(), replica_files())

#execute app every time_sync_min minutes
execute()
schedule.every(int(time_sync_min)).minutes.do(execute)

while True:
    schedule.run_pending()
    time.sleep(1)




#sync_files(source, replica)
#delete_files(source, replica)
