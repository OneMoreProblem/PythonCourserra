import os.path
import tempfile

class File():
    
    def __init__(self, path_to_file):
        self.path = os.path.realpath(path_to_file)
        self.fileName = os.path.basename(self.path)
        if not(os.path.exists(self.path)):
            print('w')
            with open(self.path, 'w+') as f:
                pass
        else:
            print('a')
            with open(self.path, 'a+') as f:
                pass
        
    def __str__(self):
        return self.path
    
    def write(self, str):
        if os.path.exists(self.path):
            f = open(self.path, 'w')
        else:
            f = open(self.path, 'a')
        return f.write(str)
    
    def read(self):
        with open(self.path, 'r') as f:
            return f.read()
    
    def __add__(self, otherFile):
        selfFilename  = os.path.splitext(self.fileName)[0]
        otherFileName = os.path.splitext(otherFile.fileName)[0]
        ext           = os.path.splitext(self.fileName)[1]
        resultFile = File(os.path.realpath(selfFilename+otherFileName+ext))
        resultFile.write(self.read()+otherFile.read())
        return resultFile        
    
#    def __iter__(self):
#        return self
    
    def __getitem__(self,index):
        with open(self.path, 'r') as f:
            content = f.read()
            result = content.split('\n')
            if result[-1] == '':
                result = result[0:-1]
            #if len(result[index])>0:
            return result[index] + '\n'
     #    with open()
     #    result = self.text[index].upper()
     #    return result
        
