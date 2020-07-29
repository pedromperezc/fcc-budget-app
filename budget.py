class Category:    
    #Es llamado cuando el objeto es creado
    def __init__(self,category):
        self.category = category
        self.ledger = list()
        
    def deposit (self,amount ,descri=''):
        self.amount = amount
        self.descri = descri
        self.ledger.append ({"amount": self.amount, "description": self.descri})
        
    def withdraw (self,amount ,descri=''):
        cant = 0
        self.amount = amount
        self.descri = descri
        
        #determino el total
        if self.check_funds(self.amount):
            self.ledger.append ({"amount": -1 * self.amount, "description": self.descri})
            return True
        return False      

    def get_balance (self):
        cant = 0
        for i in (range(len(self.ledger))):
           cant = cant + (self.ledger[i]["amount"])
        return cant

    def transfer (self,amount ,category):
        self.amount = amount
        
        # verifico si tengo saldo en cuenta      
        if self.check_funds (self.amount):
            self.withdraw (self.amount, "Transfer to "+ category.category )
            category.deposit(amount, "Transfer from " + self.category)
            return True
        return False
    
    def check_funds (self,amount):
        self.amount = amount
        cant = 0
        for i in (range(len(self.ledger))):
           cant = cant + (self.ledger[i]["amount"])
        if cant >= self.amount:
            return True
        return False
    
    def __str__(self):
        total = 0 
        string = p = '{:^30}'.format(self.category).replace (" ", "*") + '\n'
        for i in range(len(self.ledger)):
            cant = self.ledger[i]["amount"]
            total = total + cant
            cant = "{:.2f}".format(cant)
            cant = cant[0:7]
            description =  (self.ledger[i]["description"])
            string = string + description[0:23]
            s = '{:>'+ str(30-len(description[0:23])) + '}'
            cant = s.format(cant)
            string = string + cant + '\n'
        total = "{:.2f}".format(total)
        string = string + "Total: "+ total
        return string
       
def create_spend_chart(*args):
    lista = list ()
    lista = args[0]
    names = list()
    suma = list ()
    for category in lista:
        names.append(category.category)
    
    suma = dict()
    string = ""
    for i in range(len(lista)):
        lista_categoria = lista[i].ledger
        con = 0
        for j in range (len(lista_categoria)):
            
            if lista_categoria[j]["amount"] < 0:
                con = con + (lista_categoria[j]["amount"] * -1)
        suma[lista[i].category] = con
    #calculo porcentajes
    suma_total = 0
    for key, value in suma.items(): 
        suma_total = suma_total + value

        
    # actualizo a porcentajes
    for key, value in suma.items(): 
        suma[key] = ((suma[key] / suma_total * 100) // 10 ) * 10
    string = "Percentage spent by category"+"\n"
    

    #armo los porcentajes
    for i in range (100,0,-10):
        
        string = string + '{:>3}'.format(str(i)) + "| "
        for j in range(len(names)):
            if suma[names[j]] >= i:
                string = string + "o  " 
            else:
                string = string + "   "
        string = string + "\n"
    if i > 10:
        string = string + "\n"
    else:
        string = string + "  0| o  o  o  "+"\n" + "    ----------" +"\n"
    
    #calculo la longitud de la maxima descripción
    l_maxima = 0
    for key, value in suma.items(): 
        if len(key) > l_maxima:
            l_maxima = len(key)
    for i in range (l_maxima):
        string = string + '     '
        for key, value in suma.items(): 
            palabra = key
            if len(key) > i:
                string = string + palabra[i]+ "  "
            else:
                string = string + "   "
        string = string + "\n"
    string = string[:-2]
    string = string + " "    
    return string

