def game (p1,p2):
   
    if (p1=='R' and p2=='S') or (p1=='S' and p2=='P') or (p1=='P' and p2=='R') :
        return 'p1'
    
    elif p2==p1 :
        return 'Draw'
        
    else :
        return 'p2'
    
