#Name - Kartikeye
#Name - 2023/13/091
import numpy as np 
import matplotlib.pyplot as plt 

def square_wave(x):
    return np.sign(np.sin(x))

def partial_sum(x,n):
    sum = 0
    for i in range(1, n+1, 2):
        sum += (4/(np.pi*i)) * np.sin(i*x)
    return sum 

x = np.linspace(-np.pi,np.pi,1000)

for n in range(1,10,2):
    plt.plot(x, partial_sum(x,n), label=f'n={n}')
    
plt.plot(x, square_wave(x), label='Square wave')
plt.title('Convergence of Fourier series for square wave')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.legend()
plt.grid(True)
plt.show()
