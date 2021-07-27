def f1(x): return x*2

def f2(x): return x*4

lst = []
for i in  range(16):
    lst.append(f1(f2(i)))
    
print(lst)

print([f1(x)  for x in range (64) if x in [f2(j) for j in range(16)]])
    



def greeting(language):
    if language == 'eng':
        return 'hello world'
    if language== 'fr':
        return 'Bonjour le monde'
    else: return 'language not supported'
                         