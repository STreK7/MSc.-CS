install.packages("tm")
require("tm")
install.packages("devtools")
require("devtools")
readinteger <- function()
{
n <- readline(prompt="Enter value of k-1:") 
k<-as.integer(n)
u1 <- readLines("C:/msc.txt")
Shingle<-0
i <-0
while(i<nchar(u1)-k+1)
{
Shingle[i] <- substr(u1, start=i, stop=i+k)
print(Shingle[i])
i=i+1
}
}
if(interactive())readinteger()
