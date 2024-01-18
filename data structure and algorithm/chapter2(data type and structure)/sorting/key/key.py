# (key argument )

d = {"two":"two", "three":"one","one":1,"four":4,"six":6,"five":5}


sorting = [d[i] for i in sorted(d,key = d.__getitem__)]
 
# this sorts the list according to the rules  
print("sorting:",sorting)

# in list comprehension form 

sorting = [value for(key,value) in sorted(d.items()) ]
print("sorting:",sorting)
