# The merge sort algorithm consists of three simple steps:
# 1. Recursively sort the left half of the input array.
# 2. Recursively sort the right half of the input array.
# 3. Merge two sorted sub arrays into one.

# A typical problem is sorting a list of numbers into a numerical order. Merge sort works by
# splitting the input into two halves and working on each half in parallel. We can illustrate
# this process schematically with the following diagram

                                # [3,4,6,8]                                                         
   
                        #  [3,4]            [6,8]                   split
   
   
                    # [3]        [4]    [6]       [8]
                    
                    
                        #  [3,4]            [6,8]                   merge (again)
                    
                                # [3,4,6,8]                                                         
                    
def mergesort(A):
    # base case  if the input is one or zero just return 
    if len(A)>1:
        #splitting the input array
        print("splitting :",A)
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        # recursive calls to mergesort  for right and left sub array 
        mergesort(left)                      
        mergesort(right)
        # initializes pointers for left (i) and right (j)  and output arrays (k)
        
        # 3 initialization operations 
        i = j = k = 0
        
        # traverse and merges the sorted array
        
        while i  <len(left ) and j < len(right):
        
        # if left< right  comparison operation 
            if left[i] < right[j]:
           
        # if left< right  assignment  operation 
                A[k]  = left[i]
                i = i+1
            else:
                
                # if right <=left assignment 
                A[k ]= right [j]
                j = j+1
            k = k+1
        while i < len(left):
            # assignment operation 
            A [k] = left[i]
            i = i+1   
            k = k+1   
        
        while j<len(right):
            # assignment operation 
            
            A [k] = right[j]
            j = j+1   
            k = k+1   
            
        print(  'merging :',A)
        return(A)
print(mergesort([9,8,7,6,5,4,3,2,1]))        
                
                              