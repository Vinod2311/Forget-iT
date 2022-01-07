import datetime
import storeFileFB

#Upload file to Firebase with current time
def upload(filename):
    currentTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    f = open(f"./data/{filename}.txt", "w")
    f.write(f"It is safe to leave. Time:{currentTime}")
    f.close()
    fileLoc = f'./data/{filename}.txt' # set location of image file and current time
    
    storeFileFB.store_file(fileLoc)
    storeFileFB.push_db(fileLoc, currentTime)