import matplotlib.pyplot as plt

import numpy as np


data_file="Path"

data=pd.read_excel(data_file)

#time interals for pack carburization (seconds)
tkeys=['500','750','1000','1250','1500','1750','2000','2250','2500','2750','3000']

data_length=len(tkeys)

xdat=[]
ydat=[]

for dset in range(data_length):
    ydat+=[data[f'Unnamed: {7+2*dset}'].dropna(axis=0)]

    xvar=data[f'Unnamed: {6+2*dset}'].dropna(axis=0)

    if xvar[0] < 1:
        xvar*=1000

    xdat+=[xvar]


# #position of spines:

# gxmax="graph x max"
# gymax="graph y max"
# gxmin="graph x min"
# gymin="graph y min"

# #xlabel, ylabel, title

# x_label='label'
# y_label='label'
# # t_label='label'
    
##############
#space ticks
tick_num=7


xmin=min([min(x) for x in xdat])
xmax=max([max(x) for x in xdat])

ymin=min([min(x) for x in ydat])
ymax=max([max(x) for x in ydat])



#get logarithmic scaled tick marks for log plot

xrange= np.logspace(np.log(xmin),np.log(xmax),tick_num, base=np.e)
xlabels=["{:.0f}".format(round(x,2)) for x in xrange]


yrange= np.logspace(np.log(ymin),np.log(ymax),tick_num, base=np.e)
ylabels=["{:.0f}".format(round(x,2)) for x in yrange]



plt.ylabel("Hardness (Knoop)", fontsize=14)
plt.xlabel("Depth From Surface"+r" $(\mu m)$", fontsize=14)


ax=plt.gca()

#colors chosen to make each dataset seem as noticable as possible 
custom_colors = ['#e6194B', '#3cb44b', '#ffe119', '#000000', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080']


#plot data
for dset in range(data_length):
    ax.plot(np.array(xdat[dset]), np.array(ydat[dset]), color=custom_colors[dset], label=f'{tkeys[dset]}'+' s', linewidth=3)

ax.legend(loc='upper right', ncol=2, title='Pack Carburization Duration')


#log scale each axis (can also use plt.loglog())

plt.yscale('symlog')
plt.xscale('symlog')



plt.xticks(ticks=xrange, labels=xlabels, fontsize=8)
plt.yticks(ticks=yrange, labels=ylabels, fontsize=8)



plt.grid('on')
#save/show fig

plt.savefig("out_path", dpi=1200)

plt.show()
