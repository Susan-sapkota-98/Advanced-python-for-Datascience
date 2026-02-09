class DataSample:
    def __init__(self,name,values):
        self.name=name
        self.values=values

    def summary(self):
        return {
            "mean":sum(self.values)/len(self.values),
            "max":max(self.values),
            "min":min(self.values),
            "range":max(self.values)-min(self.values)

        }
    def display(self):
        print(f'Data Sample: {self.name}')
        print("Values:",self.values)

# samples=[
#     DataSample("Sample1",[10,20,30])
#     DataSample("Sample2",[])
# ]