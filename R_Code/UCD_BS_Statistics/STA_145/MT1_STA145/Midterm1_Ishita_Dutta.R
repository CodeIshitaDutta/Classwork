


#===========================================================================================================# STA 145 Bayesian Statistical Inference - Exercises - midterm
# Instructor: Jairo Fuquene, Term: Spring/2023
#===========================================================================================================

theta<-seq(0,0.5,len=1000)
theta
VE<-(2*theta-1)/(theta-1)

plot(VE,theta)




theta<-(1-0.3)/(2-0.3)



#===================================================================
# VE versus theta
#===================================================================



#===================================================================
# Prior elicitation 
#===================================================================

E.theta<-0.4118   



 f=function(a){
 	E.theta<-0.4118 
  	cumulative<-pbeta(0.964,a,((1-E.theta)/E.theta)*a)-pbeta(0.005,a,((1-E.theta)/E.theta)*a)-0.95
   	return(cumulative)
 	         } 
 
 a = uniroot(f,lower=0.01,upper=4)$root
 
 b = ((1-E.theta)/E.theta)*a
 


E.theta<-a/(a+b)

E.theta

a1 <- 1
b1 <- 1

a1
b1

w1 = a1 + b1


w1




#===================================================================
# a) Prior likelihood posterior distributions (prior elicitation 1)
#===================================================================

# Data



y<-8
n<-94



theta<-seq(0,1,len=1000)

theta
# Prior --> Following Uniform Dist
## a and b are both 1 on a beta distribution following the prior elicitation
## combine this with the definition of a uniform dist on a beta formula (?)

E_theta_prior <- 1/(b - a) # following prior elicitaion




plot(theta,dbeta(theta,a1,b1),type="l",xlab=expression(theta),
ylab=expression(p(theta)),main="Beta/Binomial model with Uniform Prior, where E(theta)=0.4118, VE=30%",ylim=c(0,24))

# Likelihood

# MLE


MLE<-y/n

MLE

lines(theta,dbeta(theta,y+1,n-y+1),type="l",col=2,lty=2)

# theta^(y)*(1-theta)^(n-y)

a.p1 = a1 + y 
b.p1 = b1 + n - y


# Posterior


lines(theta,dbeta(theta,a.p1,b.p1),type="l",col=3, lty=3)


legend(0.5,20,paste(c("Beta(0.7,1)","Likelihood", "Posterior: Beta(8.7,87)")),lty=c(1,2,3),col=c(1,2,3),cex=0.8)
abline(v=MLE,col=4,lty=2)


#=====================================================
# b) Posterior expectation
#=====================================================


E_theta_posterior1 <- a.p1/(a.p1 + b.p1)
E_theta_posterior1

w <- a1 + b1

eta<- w/(w+n)

E.theta <- a1/(a1 + b1)

eta*E.theta + (1-eta)*MLE



#=====================================================
# b) Posterior probability theta>0.4118
#=====================================================

(1-pbeta(0.4118, a.p1, b.p1))*100 # is smaller than 2.5%. 


#=====================================================
#  c) Credible interval (quantiles)
#=====================================================

theta.credible.interval = qbeta(c(0.025,0.975),a.p1, b.p1)
round(theta.credible.interval,1)


plot(theta,dbeta(theta,a.p1,b.p1),type="l",xlab=expression(theta),
ylab=expression(p(theta)),xlim=c(0,0.3))
abline(v=theta.credible.interval[1],col=3,lwd=2, lty=3)        
abline(v=theta.credible.interval[2],col=3,lwd=2, lty=3)        



# With 95% probability the probability that an ill subject is vaccinated is between 4.2% and 15.6%.

## Credible interval for the vaccine effectiveness

# Transform into a corresponding credible interval for the vaccine effectiveness

VE.credible.interval = rev((1-2*theta.credible.interval)/(1-theta.credible.interval))
round(VE.credible.interval*100,1)


# This Bayesian credible interval from 81.6% to 95.6% of the vaccine effectiveness close to the frequentist confidence interval



#=====================================================
# c) Credible interval (Highest posterior density region)
#=====================================================



library(TeachingDemos)

hpd(qbeta, shape1=a.p1, shape2= b.p1)


plot(theta,dbeta(theta,a.p1,b.p1),type="l",xlab=expression(theta),
ylab=expression(p(theta)),xlim=c(0,0.3))
abline(v=0.03776744,col=3,lwd=2, lty=3)        
abline(v=0.14905619,col=3,lwd=2, lty=3)        


VE.credible.interval = rev((1-2*hpd(qbeta, shape1=a.p1, shape2= b.p1))/(1-hpd(qbeta, shape1=a.p1, shape2= b.p1)))
round(VE.credible.interval*100,1)

#=====================================================
# c) Confidence interval
#=====================================================

c(MLE-1.96*sqrt(MLE*(1-MLE)/n),MLE+1.96*sqrt(MLE*(1-MLE)/n))



#===================================================================
# d) Posterior-predictive distribution
#===================================================================


par(mfrow=c(1,2))

# TailRank package  for Beta-binomial distribution,
#install.packages("extraDistr")
library(extraDistr)
m <- 94 
y <- rbinom(10000, m, MLE) 
y_m <- rbbinom(10000, m, a.p1, b.p1)
plot(table(y)/10000, xlab="" , ylab="Predictions using MLE")
plot(table(y_m)/10000, xlab="" , ylab="Posterior-predictive")



Posterior_mean <- (a.p1)/(a.p1+ b.p1) 

Posterior_mean



mean_predictive <- m*(a.p1)/(a.p1+ b.p1) 

mean_predictive





   
     
        
     
