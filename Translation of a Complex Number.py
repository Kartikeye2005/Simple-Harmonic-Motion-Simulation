#Roll no.- 2023/13/091
import matplotlib.pyplot as plt 

#Original vertices of the square 
v = [1+1j,-1+1j,-1-1j, 1-1j]
#Translation vector 
translation = eval(input('Enter a Complex Number(inform of x+yj):'))

#Apply the translation parts for plotting 
trans_v = [z + translation for z in v ]

#Extract real and imaginary parts for plotting
org_x = [z.real for z in v]
org_y = [z.imag for z in v]
trans_x = [z.real for z in trans_v]
trans_y = [z.imag for z in trans_v]

#Close the squares by repeatin the first point 
org_x.append(org_x[0])
org_y.append(org_y[0])
trans_x.append(trans_x[0])
trans_y.append(trans_y[0])

# Plotting lines connecting original and translated vertices 
plt.plot([v[0].real,trans_v[0].real],[v[0].imag,trans_v[0].imag],linestyle = '-',color='green')
plt.plot([v[1].real,trans_v[1].real],[v[1].imag,trans_v[1].imag],linestyle = '-',color='green')
plt.plot([v[2].real,trans_v[2].real],[v[2].imag,trans_v[2].imag],linestyle = '-',color='green')
plt.plot([v[3].real,trans_v[3].real],[v[3].imag,trans_v[3].imag],linestyle = '-',color='green')

#plotting the original and translated squares 
plt.plot(org_x, org_y, label='Original Square',marker='*')
plt.plot(trans_x, trans_y, label='Translated Square',marker='*',color='blue')
plt.grid(True)
plt.legend()
plt.title(f'Translation of Square by T(z) = z + (translation)')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.axis('equal')
plt.show()

#Calculate area of both original and Translated Square
A_1 = (abs(v[1]-v[0]))**2
A_2 = (abs(trans_v[3]-trans_v[0]))**2
#Check the area is equal or not 
if A_1==A_2:
    print(f'The area of both squares are same and the area is = {A_1}')
else:
    print('Area of both square is different')
    