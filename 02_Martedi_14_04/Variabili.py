# Definizione operatori

# Somma
print(1+5)

# Differenza
print(6-5)

# Moltiplicazione
print(3*2)

# Divisione
print(4/2)

# Potenza
print(3**2)

# Divisione intera
print(7//2)

# Modulo
print(5%2)

# Tipi delle variabili

# Numeri interi
a = 0
b = 1
neg_b = -1
print(type(a), type(b), type(neg_b))

# Floats
c = 3.14
d = -3.14
print(type(c), type(d))

# Stringhe
e = 'Ciao'
f = "3.14"
print(type(e), type(f))

# Possibile estrarre i singoli caratteri da una stringa
s = "Python"
print(s[0])
print(s[1])

# Modificano il comportamento di alcuni operatori
saluto = "Ciao"
nome = "Alice"
messaggio = saluto + " " + nome
print(messaggio)

# Metodi incorporati delle stringhe
msg = "Hello, world!"
print(msg.upper())
print(msg.lower())
print(msg.title())
print(msg.split(','))
print(msg.replace('world', 'Universe'))

# Booleani
g = True
f = False
print(type(g), type(f))

# Operatori di confronto che restituiscono un booleano
x = 5
y = 10

h = x == y
i = x != y
j = x < y 
print(h, type(h))
print(i, type(i))
print(j, type(j))

# Operatori logici
x = 5
y = 10
z = 7

print(x < y and y > z) # Restituisce True se entrambe le condizioni sono True
print(x < y or z > y) # Restituisce True se almeno una delle due condizioni è True
print(not(x < y)) # Restituisce il valore booleano opposto

# Liste
numeri = [1, 2, 3, 4, 5]
nomi = ["Alice", "Mario", "Giuseppe"]
misto = [1, "Alice", True, 4.5]

print(numeri[0]) # Possibile estrarre i singoli valori dalle liste
print(numeri[1])

numeri[2] = 10 # Sono modificabili
print(numeri)

print(nomi, type(nomi))
print(misto, type(misto))

numeri = [3, 1, 4, 2, 5]
print(len(numeri))
numeri.append(6) # Aggiunge il valore specificato tra parentesi alla fine della lista
print(numeri)
numeri.insert(2, 10) # Aggiunge alla posizione indicata dal prmo paramentro, il valore indicato nel secndo paramentro
print(numeri)
numeri.remove(2) # Rimuove il valore indicato dal parametro
print(numeri)
numeri.sort() # Ordina gli elementi della lista
print(numeri)

