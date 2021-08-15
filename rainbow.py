import hashlib
import csv

with open("codes.csv",newline="") as csvfile:
    reader=csv.reader(csvfile)
    with open ('javab2.csv','w',newline='') as another_file:
        writer=csv.writer(another_file)
        for row in reader:
            name=row[0]
            for password in range(1000,9999):
                password=str(password)
                hs=hashlib.sha256(password.encode()).hexdigest()
                l=[]
                l.append(hs)
                if l == row[1:]:
                    d={}
                    d[name]=password
                    for x,y in d.items():
                        writer.writerow([x,y])
        
        another_file.close()
                        

            

                    




                    

                
                    
                          
        
        


