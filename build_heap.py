# python3
import math

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for index,value in reversed(list(enumerate(data))):
        tek_el = index
        pat = True
        while pat:
            vec = (tek_el+1)//2-1
            if tek_el <1:
              pat = False
              break
            if data[tek_el]<data[vec]:
                swaps.append([vec,tek_el])
                data[tek_el],data[vec]=data[vec], data[tek_el]
                tek_el = vec
            else:
                pat = False
                break
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    veids = input()
    data=[]
    n=0
    if veids =="I" :
       n = int(input())
       data = list(map(int, input().split(" ")))
    elif veids =="F":
        file_Name = input()
        if "a" in file_Name:
            return
        with open("./tests/" + file_Name, "r") as op:
             n = int(op.readline())
             data = list(map(int, op.readline().split(" ")))
    
    # input from keyboard


    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i in swaps:
        print(i[0],i[1])


if __name__ == "__main__":
    main()
