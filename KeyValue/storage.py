import os
import tempfile
import argparse
import json


def get(key,storage_path):
    with open(storage_path, 'r') as f:
        try:
            data = json.load(f)
            values = data[key]
            print(*values, sep=', ')
        except:
            pass

def save(dic,storage_path):
    with open(storage_path, 'r+') as f:
        if os.stat(storage_path).st_size <= 1:
            json.dump(dic,f)
        else:
            data = json.load(f)
            f.seek(0)
            keys, values = zip(*dic.items())

            if keys[0] in data:
                data[keys[0]].append(*dic[keys[0]])
                json.dump(data,f)
            else:
                json.dump({**data,**dic},f)

parser = argparse.ArgumentParser(description='Save and open key-value')
parser.add_argument("--key", help='Key', required=True)
parser.add_argument("--val",nargs='?',const=None)
args = vars(parser.parse_args())

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

inp = {args['key']:[args['val']]}



if not(os.path.exists(storage_path)):
    my_file = open(storage_path, "a+")
    my_file.close()
else:
    pass


if args['val']==None:
    get(args['key'],storage_path)
else:
    save(inp,storage_path)
    
    
# with open(storage_path, 'w') as f:
#     print(inp)
        

    
    