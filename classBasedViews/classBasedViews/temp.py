def find_min_marks(ar, n):
    marks.sort()
    
    
    
    ar.sort() 
    print(ar)
    ans=ar[0]
    prev=ar[0]
    for i in range(1,n):
        if(ar[i]>prev):
            ans+=ar[i]
        elif(prev >= ar[i]):
            ar[i]=prev+1 
            ans+=ar[i] 
        prev=ar[i] 
            
            
    return ar
    
if __name__ == '__main__':
    marks = [1,4,5,4,5, 4,4, 5, 5]
    print(find_min_marks(marks, len(marks)))