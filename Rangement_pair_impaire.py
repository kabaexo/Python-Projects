#programmeur: yassmine rezgui 
#
#
#exercice:rangemet de tableau pair w impair


#remplir tab1
t1 = [1, 2, 3, 4, 5, 642, 52, 11, 89, 16]
t2 = []


for element in t1: #loop = 1 2 3 4 5 642 52 11 89 16
    if element % 2 == 0:
        t2.append(element)
       
#lehné liste t2 feha les nombre paire deja mnadhmin 2,4,642,52,16



for element in range(len(t1)-1, -1, -1):# range (len(t1)-1,-1,-1) => 9,8,7,6,5,4,3,2,1 
    if t1[element] % 2 != 0: #lehné nekhdhou t1[9] = 16 t1[8] = 89 n7ottou ba3d ekher noumrou fel t1 illi houa 2,4,642,52,16, <-89, wba3d t1[7] = 11  2,4,642,52,16,89, <-11 etc  
        t2.append(t1[element])       
       

print(t2)



#remarque  = ken nhebbou nekhdmou bel les elements  kima for loula najmou nesta3mlou reversed(t1) ta3tina 16,89,11,52,642,5,4,3,2,1
# for element in reversed(t1):