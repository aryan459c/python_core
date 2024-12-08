class recta:
    def __init__(self,leng,width):
        self.leng=leng
        self.width=width
    def area_para(self):
        return (self.leng*self.width)
class square(recta):
    def __init__(self,leng,width,):

        super().__init__(leng,width)



