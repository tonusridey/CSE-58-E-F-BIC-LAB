def h_d(s1,s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count
        
def a_p_m(pattern, text, d):
     positions = []
     k = len(pattern)


     for i in range(len(text) - k + 1):
        substring = text[i:i+k]

        if h_d(pattern, substring) <= d:
            positions.append(i)

     return positions 
pattern = input("enter pattern: ")
text = input("enter text: ")
d = int(input("enter d: "))  

print(a_p_m(pattern, text, d))



