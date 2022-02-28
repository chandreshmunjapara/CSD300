
import diretion_gene as d
import  math
val =1/65536
sum=0
count=0
for i in range(256):
   for j in range(256):
      if d.temp_host[i][j]==d.stego[i][j]:
         count+=1
      sum+=((d.temp_host[i][j]-d.stego[i][j])**2)
print(count)