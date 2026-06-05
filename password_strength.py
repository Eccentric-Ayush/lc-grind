#Brute Force Approach
def passwordStrength(password):
    marks = 0
    marked = set()
    for i in password:
        if i in set(list('qwertyuiopasdfghjklzxcvbnm')) and i not in marked:
            marks += 1
            marked.add(i)
        elif i in set(list('QWERTYUIOPASDFGHJKLZXCVBNM')) and i not in marked:
            marks += 2
            marked.add(i)
        elif i in set(['0','1','2','3','4','5','6','7','8','9']) and i not in marked:
            marks += 3
            marked.add(i)
        elif i in set(['!', '@', '#', '$']) and i not in marked:
            marks += 5
            marked.add(i)
    return marks

