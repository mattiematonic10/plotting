import matplotlib.pyplot as plt

def diction(word):
    d = dict()
    for char in word:
        d[char]=  d.get(char,0) +1
    return d

    
def plot_hist(data):
    plt.hist(data,bins=7)

    plt.ylabel('Counts')
    plt.title('Frequency of letters')

    plt.show()

def plot_dict(d):
    plt.bar(list(d.keys()), d.values())
    plt.ylabel('Counts')
    plt.title('Frequency of letters')
    plt.show()

    
