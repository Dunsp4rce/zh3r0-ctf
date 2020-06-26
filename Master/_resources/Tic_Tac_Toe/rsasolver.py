import math
import binascii

def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x

prod = 156935655500198733255923805969370297538115753312746380213875723177744608509780722798549730106834861986575848272630355804840179947615966722051370804273521733290376009020885919941338141950993008276537987193794648055241515380150115338397065198086893695560540379329063476893211153270247222670504019722793971516489
sums = 25089219254058723086004960979954103479984362695038160907003438818016936688465630366701002710571334149929206994096775851785636272938202242921638312612784566

phi = prod - sums + 1
e= 65537
d=int(modInverse(e,phi))
c=102778142076243116117419062640171713879684005471846556860689446479305435562766590357152362175278713093609670819423506015563433111872029023117856369287465874159889936283732420732086482645886112577942492103417960605158427793203017078930148395937563028135853490687072326149444788825363901282252753328289332801180
n=int(prod)
#print(int(d))
m=pow(c,d,n)
#print(int(m))
hexm = hex(m)
flag = bytes.fromhex(hexm[2:])
print(flag)


 