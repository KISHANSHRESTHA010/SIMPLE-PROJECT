class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def __add__(self,other):#__sub__(-),__trudiv__(/),__eq(==),__mul__(*)
        return(self.x+other.x,self.y+other.y)
    
    def __str__(self):#Makes the points readable i.e string
        return(f"{self.x},{self.y}")


p1=point(3,4)
p2=point(1,2)

result=p1+p2

print(result)