#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Tyres:             # class-1
    def __init__(self,brand,belted_bias,opt_pressure):
        self.brand      =brand
        self.belted_bias=belted_bias
        self.opt_pressure=opt_pressure
        
    def __str__(self):    # __str__ is used to give name to method and it also execute.
        return("Tyre: \n \tBrand:"+self.brand+"\n \tBelted-Bias:"+str(self.belted_bias)+"\n \tOpt-Pressure:"+str(self.opt_pressure))

class Engine:             # class-2
    def __init__(self,fuel_type,capacity):
        self.fuel_type=fuel_type
        self.capacity=capacity
    
    def __str__(self):
        return("Engine: \n \tFuel-Type:"+self.fuel_type+"\n \tCapacity:"+str(self.capacity))

class Body:               # class-3
    def __init__(self,size):
        self.size=size
        
    def __str__(self):
        return("Body: \n \tsize"+self.size)

class Car:                  # class car = encapsulation means tyre+body+engine=car
    def __init__(self,tyres,engine,body):
        self.tyres=tyres
        self.engine=engine
        self.body=body
        
    def __str__(self):
        return str(self.tyres)+ '\n' +str(self.engine)+ '\n' +str(self.body)
    
    t= Tyres('Bridgestone',True,34)
    e= Engine('Desel',2.2)
    b= Body('SUV')
    
    c= Car(t, e, b)
    print(c)


# In[ ]:




