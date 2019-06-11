"""Sample solutions from various students"""

# no need to manually unzip the .npz and load each file separately, too much work!
# just use np.load() on the .npz file
a = np.load('x.npy')
b = np.load('y.npy')
t = np.load('t.npy')


# no need to rename
a = d['x']
b = d['y']
t = d['t']


# no need to iterate over array contents, either with a for loop or with list comprehension,
# use array operations instead:
def absdiff(a, b):
    output = []
    for i in range (len(a)):
        result = a[i]-b[i]
        c = abs(result)
        output.append(c)
    return output

def absdiff(a,b):
    """returns the absolute value of the difference between
    two sequences (arrays, lists, or tuples)"""
    diff = [a[i] -b[i] for i in range(len(a))]
    return abs(np.array(diff))


# what's missing?
def absdiff(a, b):
    """Returns the difference of arrays, list or tuple"""
    return np.array(a) - np.array(b)


# don't be afraid to overwrite existing variable names if you don't need the original
# values any more:
def absdiff(a, b):
    """Take two sequencies of values a,b of identical lengths and returns an array
    of the absolute difference of each number"""
    A = np.array(a)
    B = np.array(b)
    return abs(A-B)


# don't get the plot arguments mixed up! do these look like a function of t on the x axis?
plt.plot(x, t)
plt.plot(y, t)


# what does this do?
plt.hist(x, bins=30)
plt.hist(y, bins=30)
plt.hist(absd, bins=30)


# changes location and shape of the legend, to prevent overlap
plt.legend(loc=2, ncol=2)


# lots of people forgot to actually plot a legend!


# what does this do?
np.savez('t_absd.npz', t='t', absd='absd')


# what does this do?
np.savez('t_absd.npz', t, absd)
