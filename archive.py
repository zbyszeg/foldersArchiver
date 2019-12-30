import datetime
import os
import shutil

class FoldersArchiver:
    def __init__(self):
        self.now = datetime.datetime.now()
        self.year = self.now.year
        self.month = self.now.month
        self.day = self.now.day
        self.hour = self.now.hour
        self.minute = self.now.minute
        self.second = self.now.second
        
        if self.month == 1:
            self.beforeMonth = 11
            self.year -= 1
        elif self.month == 2:
            self.beforeMonth = 12
            self.year -= 1
        else:
            # self.beforeMonth = self.month - 2
            self.beforeMonth = self.month
        
        self.sYear = str(self.year)
        self.sShortYear = self.now.strftime("%y")
        self.sMonth = str(self.month)
        self.sBeforeMonth = str(self.beforeMonth)
        self.sDay = str(self.day)
        self.sHour = str(self.hour)
        self.sMinute = str(self.minute)
        self.sSecond = str(self.second)

        self.mainDir = "r:\\"
        # self.mainDir = "/home/zbyszek/python/p"
    
    def archive(self):
        for (root, dirs, files) in os.walk(self.mainDir):
            log = open(self.sShortYear + self.sMonth + self.sDay + '_' + self.sHour + '-' + self.sMinute + '-' + self.sSecond + '.log', 'a+')
            for folder in dirs:
                if folder.startswith(self.sShortYear + self.sBeforeMonth + '_'):
                    if self.sYear in root:
                        pass
                    else:
                        source = os.path.join(root, folder)
                        target = os.path.join(root, self.sYear)
                        if os.path.isdir(target) == False:
                            os.makedirs(target)
                        try:
                            shutil.move(source, target)
                            print(os.path.join(root, folder) + "\tmoved")
                            log.write(os.path.join(root, folder) + "\tmoved\n")
                        except:
                            print("ERROR!\t" + os.path.join(root, folder) + "\thasn't moved!")
                            log.write("ERROR!\t" + os.path.join(root, folder) + "\thasn't moved!\n")
            log.close()
