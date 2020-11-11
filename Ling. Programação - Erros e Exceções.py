#!/usr/bin/env python
# coding: utf-8

# In[27]:


print ('-' * 30)
print ('ERROS E EXCEÇÕES')
print ('-' * 30)


# In[ ]:


#voce acha que esse comando dará erro?


# In[3]:


print('oii')


# In[4]:


print(x)


# In[5]:


x= 2
print(x)


# In[8]:


n = int(input('digite um número:   '))


# In[13]:


a = int(input('Digite o numerador: '))
b = int(input('Digite o denominador: '))
r= a/b
print('o resulto foi: ', r)


# In[14]:


a = int(input('Digite o numerador: '))
b = int(input('Digite o denominador: '))
r= a/b
print('o resulto foi: ', r)


# In[15]:


a = int(input('Digite o numerador: '))
b = int(input('Digite o denominador: '))
r= a/b
print('o resulto foi: ', r)


# In[ ]:


try 
    operação
except 
    o que irá acontecer


# In[18]:


try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r= a/b
    print('o resulto foi: ', r)
except:
    print('Infelizmente tivemos um problema :( ')


# In[20]:


try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r= a/b
    print('o resulto foi: ', r)
except:
    print('Infelizmente tivemos um problema :( ')
finally:
    print('volte sempre, Muito Obrigado!!')


# In[23]:


try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r= a/b
    print('o resulto foi: ', r)
    
except(ValueError, TypeError):
    print('Infelizmente tivemos um problema com o valor digitado :( ')
    
except(ZeroDivisionError):
    print('Infelizmente não é possível dividir um número por zero :( ')
    
except:
    print('Infelizmente tivemos um problema :( ')
finally:
    print('volte sempre, Muito Obrigado!!')


# In[24]:


list= [1,2,3]
print(list[3])


# In[25]:


list= [1,2,3] # psc 0 ,1 , 2
print(list[2])


# In[ ]:




