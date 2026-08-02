class myclass:
    object_count=0

    def __init__(self):

        myclass.object_count+=1

    @classmethod
    def get_object_count(cls):
        return cls.object_count
    
c1=myclass()
c2=myclass()
    
print(f"Object count:{myclass.get_object_count()}")

