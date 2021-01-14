import csv
import sys

arg_count = len(sys.argv)

if arg_count < 3:
    print("""
          #usage
          csv2txt fileName RowName [RowName2 RowName3 ....]
          
          If RowName Contains space usage Double quote(i.e. "Row Name") around it.
          """)
    exit

itr = arg_count - 2
while(itr):
    print(sys.argv[itr+1])
    with open(sys.argv[1]+".csv") as File:
        reader = csv.DictReader(File)
        with open(sys.argv[itr+1]+'.txt', "w") as out:
            for row in reader:
                data = row[sys.argv[itr+1]]
                out.write(data+"\n")
            out.close()
        itr = itr - 1


print("Command Executed Successfully")
