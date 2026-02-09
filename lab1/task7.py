class DataSample:
    def __init__(self,name,values):
        self.name=name
        self.values=values

    def normalize(self):
        max_val=max(self.values)
        self.values=[x/max_val for x in self.values]

    def plot(self):
        import matplotlib.pyplot as plt
        plt.plot(self.values,marker='o')
        plt.title(self.name)
        plt.show()