library(extraDistr)
n <- 10000
y <- rnorm(n,5,1)
## nu0 and s02 are the parameters for prior of 1/sigma^2
s02 <- 1
nu0 <- 1
## mu0 and k0 are the parameters for prior
mu0 <- 2
k0 <- 2
## Now we calculate the parameters for posterior distribution
## parameters for posterior of sigma^2

## parameters for posterior of theta
kn <- k0+n
nun = nu0 + n
mun = (k0 * mu0 + n * mean(y)) / kn
s2 <- var(y)
s2n = (1 / nun) * (nu0 * s02 + (n - 1) * s2 + (k0 * n / kn) * (mean(y) - mu0)^2)
s2.postsample <- 1/rgamma(n,nun/2,s2n*nun/2)
theta.postsample <- rnorm(n,mun,sqrt(s2.postsample /kn))

library(invgamma)
hist(s2.postsample,prob = TRUE,nclass=40,main="Histogram of sigma^2")
x2 <- seq(min(s2.postsample), max(s2.postsample), length = 40)
fun <- dinvgamma(x2, nun/2,s2n*nun/2, log = FALSE)
lines(x2, fun, col = 2, lwd = 2)
hist(theta.postsample,prob = TRUE,nclass=40,main="Histogram of theta")
x2 <- seq(min(theta.postsample), max(theta.postsample), length = 40)
fun2 <- dlst(x2, df=nun,mu= mun,sigma=sqrt(s2n/kn), log = FALSE)
lines(x2, fun2, col = 2, lwd = 2)

