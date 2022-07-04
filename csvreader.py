
import os


# with open('dummy.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
    
#     for line in csv_reader:
#         linex = [float(x) for x in line]
#         predict(linex)
        
filename="abc.txt"
now=os.getcwd()
print(os.path.join(now,filename))
