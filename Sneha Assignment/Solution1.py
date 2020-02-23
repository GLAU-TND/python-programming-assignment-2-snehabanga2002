ls = list(map(str,input(").split()))
ans = []
ans.append(ls[0])
x = 0
while(True):
    if(x==len(ls)):
        break;
    last = ans[x][-1]
    for i in range(len(ls)):
        if ls[i]!="" and ls[i][0]==last:
            ans.append(ls[i])
            ls[i]=""
            x+=1;
            break
print(ans)



INPUT:
    chair height racket touch tunic
 OUTPUT:
    ['chair','racket','touch','height','tunic']
    
