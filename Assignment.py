class P:
    def __init__(self):
        self.inp = ""
        
    def input_s(self):
        self.inp = input("Enter a string ")
      
    def details(self):
        x = self.inp[1::2]
        print (x)

R=P()
R.input_s()
R.details()

        



