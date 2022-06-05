import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        data = OrderedDict()
        hash1 = OrderedDict()
        result = OrderedDict()
        with open(output_file_name, 'w', newline='', ) as hashfile:
            for i in range(1000, 10000):
                m = hashlib.sha256(str(i).encode()).hexdigest()
                #print(m)
                hash1.update({m: i})
            #print(hash1)
            for row in reader:
                #print(row)
                name = row[0]
                dgst = row[1]
                #print(dgst)
                data.update({dgst : name})
            #print(data)
            for key in data :
                if key in hash1 :
                    #print(data[key],hash1[key])
                    result.update({data[key]:hash1[key]})
            #print(result)
            writer = csv.writer(hashfile,delimiter = ",")
            writer.writerows(result.items())

        hashfile.close()
    csvfile.close()

