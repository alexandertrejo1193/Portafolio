library(BatchGetSymbols)
library("fPortfolio")
library("timeSeries")
library("quantmod")
library("dplyr")
library("PerformanceAnalytics")
library("tidyverse")
library("corrplot")
library("tidyquant")
library(purrr)

GETMYSYMBOL <- function(x) {
  getSymbols(x,, periodicity = 'monthly',auto.assign = F,from =as.Date("2022-01-01") ,to =as.Date("2023-01-01") )}
activos <- c("AAPL","AMZN","META")
Activos<- map(activos,GETMYSYMBOL)%>% map(Cl) %>% reduce(merge.xts) %>% na.omit()
precios <- na.omit(Activos)
precios
rendimientos <- ROC(precios,type="discrete")[-1]
colnames(rendimientos) <- c("Apple","Amazon","Meta")
rendimientos

volatilidadApple <- var(rendimientos[,1])**(1/2)
volatilidadAmazon<- var(rendimientos[,2])**(1/2)
volatilidadMeta<- var(rendimientos[,3])**(1/2)
volatilidad <- rbind(c(volatilidadApple,volatilidadAmazon,volatilidadMeta))
colnames(volatilidad) <- c("Apple","Amazon","Meta")
volatilidad

volatilidadApplep <- var(precios[,1])**(1/2)
volatilidadAmazonp<- var(precios[,2])**(1/2)
volatilidadMetap<- var(precios[,3])**(1/2)
volatilidadp <- rbind(c(volatilidadApplep,volatilidadAmazonp,volatilidadMetap))
colnames(volatilidadp) <- c("Apple","Amazon","Meta")
volatilidadp

yapple=c()
yamazon=c()
ymeta=c()

Apple <- as.vector(precios[,1])
Amazon <- as.vector(precios[,2])
Meta <- as.vector(precios[,3])
termino <- length(precios[,1])-1
for (i in 1:termino){
  if(Apple[i]<Apple[i+1]){
    yapple <- c(yapple,1)
  }else{
    yapple <- c(yapple,0)
  }
  if(Amazon[i]<Amazon[i+1]){
    yamazon <- c(yamazon,1)
  }else{
    yamazon <- c(yamazon,0)
  }
  if(Meta[i]<Meta[i+1]){
    ymeta <- c(ymeta ,1)
  }else{
    ymeta <- c(ymeta ,0)
  }
}

yapple
yamazon
ymeta

papple <-sum(yapple)/length(yapple)
pamazon <- sum(yamazon) /length(yamazon)
pmeta <- sum(ymeta) /length(ymeta)

papple
pamazon
pmeta

t <- 1
n <- 12
dt <- t/n

uapple <- exp(volatilidadApplep*((dt)**(1/2)))
uamazon <-exp(volatilidadAmazonp*((dt)**(1/2)))
umeta <- exp(volatilidadMetap*((dt)**(1/2)))

uapple 
uamazon
umeta 

dapple <- exp(-volatilidadApplep*((dt)**(1/2)))
damazon <-exp(-volatilidadAmazonp*((dt)**(1/2)))
dmeta <-exp(-volatilidadMetap*((dt)**(1/2)))

dapple 
damazon 
dmeta

capple <-c()  
camazon <- c()
cmeta <- c()

capple1 <-c()  
camazon1 <- c()
cmeta1 <- c()

activosLR <- c("^IRX")
ActivosLR<- map(activosLR,GETMYSYMBOL)%>% map(Cl) %>% reduce(merge.xts) %>% na.omit()
preciosLR <- na.omit(ActivosLR)
tasaLR <- preciosLR[12,1]
delta <- log(1+tasaLR)

funC<- function(k){
  for(i in 1:11){
    capple1 <- choose(n,i)(papplei)((1-papple)*(n-i))
    max(Apple[1]uapplei*dapple*(n-i)-k,0)
    camazon1 <- choose(n,i)(pamazoni)((1-pamazon)*(n-i))
    max(Apple[1]uamazoni*damazon*(n-i)-k,0)
    cmeta1 <- choose(n,i)(pmetai)((1-pmeta)*(n-i))
    max(Apple[1]umetai*dmeta*(n-i)-k,0)
  }
  capple <- sum(capple1)*exp(-delta*t)
  camazon <- sum(camazon1)*exp(-delta*t)
  cmeta <- sum(cmeta1)*exp(-delta*t)
  
  return(c(capple,camazon,cmeta))
}
funC(150)