#SELECTION SORT IMPLEMENTATION


'''def selectionsort(array,size):


    #for each element in the 
    for ind in range(size):
        min_size=ind

        for i in range(ind+1,size): #setting the range of the elemants to be checked
            #checking whether the element is smaller then the minimum indexed set
            if array[i]<array[min_size] :
                array[i],array[min_size]=array[min_size],array[i]

    print("THE SORTED ARRAY:",array)

if __name__=="__main__":
    size=int(input("Enter the number of list elements"))
    array=[]
    for i in range(size):
        x=int(input("Enter the value to be added:"))
        array.append(x)
    
    selectionsort(array,size)'''



def selectionsort(array,size):

    for index in range(size):
        min_ind=index

        for i in range(min_ind+1,size):
            if array[i]<array[min_ind]:
                array[i],array[min_ind]=array[min_ind],array[i]


    print("the sorted array is:",array)




if __name__=="__main__":
    size=int(input("Enter the number of elements in the array:"))
    array=[]
    for i in range(size):
        x=int(input("Enter your value:"))
        array.append(x)
    print("the array is :",array)
    selectionsort(array,size)
    