import re 

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
EMAILS = ["vicente@eni.es","Longaniza@gmail.com"]
class Prueba:

  def __init__(self,email):
    self.email = email


    
  def es_email(self):
    if(re.fullmatch(regex, self.email)):
      rr = False
      for x in range(len(EMAILS)):
        if EMAILS[x]==self.email:
          rr = True

      if rr:
        z = self.email.split("@")
        print("¡Bienvenido "+str(z[0])+"! ")
        raise SystemExit(0)
      else:
        print("Cuenta bloqueada a causa de un ataque ")
        raise SystemExit(0)
        
      
 
    else:
      if self.email =='':
        print("'' es una entrada incorrecta. Introduzca una dirección de correo electrónico ")

      else:
        print("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx ")
  






n=1

while n==1:
  email = input("Introduzca su correo electrónico: ")
  em1 = Prueba(email)
  em1.es_email()





