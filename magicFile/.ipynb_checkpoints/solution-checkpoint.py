import os.path
import tempfile

class File():
    
    def __init__(self, path_to_file, file = None):
        self.path     = os.path.realpath(path_to_file)
        self.fileName = os.path.basename(self.path)
        
        if not(file==None):
            self.path = file.name
            self.file = file
            
        if not(os.path.exists(self.path)):
            print('w')
            self.f = open(self.path, 'w+')
        else:
            print('a')
            self.f = open(self.path, 'a')
        
    def __str__(self):
        return self.path
    
    def write(self, str):
        f = open(self.path, 'w')
        return f.write(str)
    
    def read(self):
        f = open(self.path,'r')
        f.seek(0)
        return f.read()
    
    def __add__(self, otherFile):
        resultFile = tempfile.NamedTemporaryFile(mode='w+')
        result     = File(resultFile.name, file = resultFile)
        result.write(self.read()+otherFile.read())
        return File(resultFile.name, file = resultFile)
    
    def __getitem__(self,index):
        with open(self.path, 'r') as f:
            content = f.read()
            result = content.split('\n')
            
            if result[-1] == '':
                result = result[0:-1]

            return result[index] + '\n'