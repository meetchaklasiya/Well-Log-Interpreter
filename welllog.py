from tkinter import *
from tkinter import filedialog
from threading import Thread
import os
import lasio
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

# from upload import file_path
root1 = Tk()
root1.state('zoomed')
root1.title('Well Log Interpreter')
# print(file_path)
# Prompt the user to select a file using the file dialog
file_path = filedialog.askopenfilename()
    
file_name = os.path.splitext(os.path.basename(file_path))[1]  # Extract the file name without extension
file_name_NEW = os.path.splitext(os.path.basename(file_path))[0]  # Extract the file name without extension
if file_name == ".las":
    las = lasio.read(file_path)
    las.sections.keys()
    las.sections['Version']
            
    df = las.df()
    
       
    fr = Frame(root1)
    fr.grid(row=2,column=0,padx=20)

    Label(fr,text='Well Information',fg='purple').grid(row=1,column=0)
            
    scrollbar1 = Scrollbar(fr,orient=VERTICAL)
    scrollbar1.grid(row=2,column=1,sticky=NS)
            
    mylist = Listbox(fr,yscrollcommand=scrollbar1.set,width=60)
            
    for item in las.sections['Well']:
        mylist.insert(END,f"{item.descr} ({item.mnemonic}): \t\t {item.value}")
            
    mylist.grid(row=2,column=0)
    scrollbar1.config(command=mylist.yview)
            
            
    fr2 = Frame(root1)
    fr2.grid(row=2,column=1)
    Label(fr2,text='Well Log Data',fg='purple').grid(row=1,column=1)
            
    scrollbar2 = Scrollbar(fr2,orient=VERTICAL)
    scrollbar2.grid(row=2,column=2,sticky=NS)
            
    mylist2 = Listbox(fr2,yscrollcommand=scrollbar2.set,width=65)
            
    for count, curve in enumerate(las.curves):
        mylist2.insert(END,f"Curve Code: {curve.mnemonic}, \t Units: {curve.unit}, \t Description: {curve.descr}")
            
    mylist2.grid(row=2,column=1)
    scrollbar2.config(command=mylist2.yview)
            
    fr3 = Frame(root1)
    fr3.grid(row=2,column=2,padx=20)
    Label(fr3,text=f"This Data Set Contains {count+1} Logs",fg='purple',font='calibri 13').grid(row=2,column=2)
        
            
    Label(root1,text='Enter the Curve Code for Logs which you require for Interpretation',font='calibri 14',fg='purple').grid(row=3,column=1,pady=15)
        
    fr4 = Frame(root1)
    fr4.grid(row=4,column=0,)
            
    y_column = Label(fr4,text="Enter the curve code for DEPTH allotted in the above output:",font='calibri 12').grid(row=4,column=0,pady=10,padx=10)
            
    def my_uppery(*args):
        ycolumnvar.set(ycolumnvar.get().upper())
            
    def my_upperx1(*args):
        x1columnvar.set(x1columnvar.get().upper())
        x2columnvar.set(x2columnvar.get().upper())
        x4columnvar.set(x4columnvar.get().upper())
        x5columnvar.set(x5columnvar.get().upper())
            
    def my_upperx2(*args):
        x6columnvar.set(x6columnvar.get().upper())
        x7columnvar.set(x7columnvar.get().upper())
        x8columnvar.set(x8columnvar.get().upper())
        x9columnvar.set(x9columnvar.get().upper())
                
    fr5 = Frame(root1)
    fr5.grid(row=4,column=1)
    ycolumnvar = StringVar()
    ycolumnvar.trace('w',my_uppery)
    ycolumnentry = Entry(fr5,text=ycolumnvar,width=20,font='calibri 12 bold')
    ycolumnentry.grid(row=4,column=1,pady=10)
            
    x1_column =Label(fr4,text="Enter the curve code for Caliper Log allotted in the above output:",font='calibri 12').grid(row=5,column=0,padx=10,pady=10)
            
    x1columnvar = StringVar()
    x1columnvar.trace('w',my_upperx1)
    x1columnentry = Entry(fr5,text=x1columnvar,width=20,font='calibri 12 bold')
    x1columnentry.grid(row=5,column=1,pady=10)
            
    x2_column = Label(fr4,text="Enter the curve code for Gamma Ray log allotted in the above output:",font='calibri 12').grid(row=6,column=0,padx=10,pady=10)

    x2columnvar = StringVar()
    x2columnvar.trace('w',my_upperx1)
    x2columnentry = Entry(fr5,text=x2columnvar,width=20,font='calibri 12 bold')
    x2columnentry.grid(row=6,column=1,pady=10)
                  
    x4_column = Label(fr4,text="Enter the 1st curve code for Resistivity log allotted in the above output:",font='calibri 12').grid(row=8,column=0,padx=10,pady=10)
            
    x4columnvar = StringVar()
    x4columnvar.trace('w',my_upperx1)
    x4columnentry = Entry(fr5,text=x4columnvar,width=20,font='calibri 12 bold')
    x4columnentry.grid(row=8,column=1,pady=10)
            
    x5_column = Label(fr4,text="Enter the 2nd curve code for Resistivity log allotted in the above output:",font='calibri 12').grid(row=9,column=0,padx=10,pady=10)
            
    x5columnvar = StringVar()
    x5columnvar.trace('w',my_upperx1)
    x5columnentry = Entry(fr5,text=x5columnvar,width=20,font='calibri 12 bold')
    x5columnentry.grid(row=9,column=1,pady=10)
            
    x6_column = Label(fr4,text="Enter the 3rd curve code for Resistivity log allotted in the above output:",font='calibri 12').grid(row=10,column=0,padx=10,pady=10)
            
    x6columnvar = StringVar()
    x6columnvar.trace('w',my_upperx2)
    x6columnentry = Entry(fr5,text=x6columnvar,width=20,font='calibri 12 bold')
    x6columnentry.grid(row=10,column=1,pady=10)
            
            
    x7_column = Label(fr4,text="Enter the curve code for Porosity log allotted in the above output:",font='calibri 12').grid(row=11,column=0,padx=10,pady=10)
            
    x7columnvar = StringVar()
    x7columnvar.trace('w',my_upperx2)
    x7columnentry = Entry(fr5,text=x7columnvar,width=20,font='calibri 12 bold')
    x7columnentry.grid(row=11,column=1,pady=10)
            
    x8_column = Label(fr4,text="Enter the curve code for Density log allotted in the above output:",font='calibri 12').grid(row=12,column=0,padx=10,pady=10)
            
    x8columnvar = StringVar()
    x8columnvar.trace('w',my_upperx2)
    x8columnentry = Entry(fr5,text=x8columnvar,width=20,font='calibri 12 bold')
    x8columnentry.grid(row=12,column=1,pady=10)
            
            
    x9_column = Label(fr4,text="Enter the curve code for SP/PEF Log allotted in the above output:",font='calibri 12').grid(row=13,column=0,padx=10,pady=10)
            
    x9columnvar = StringVar()
    x9columnvar.trace('w',my_upperx2)
    x9columnentry = Entry(fr5,text=x9columnvar,font='calibri 12 bold')
    x9columnentry.grid(row=13,column=1,pady=10)

    Label(root1,text='Developed by Meet Chaklasiya , Daksh Joshi & Pariket Pansara',font='calibri 13 bold').grid(row=14,column=0,pady=35)
    
    
    def threading():
        t1 =Thread(target=Plot) 
        t1.start()  
            
    def Plot():
        
        arr = [x1columnvar.get(),x2columnvar.get(),x4columnvar.get(),x5columnvar.get(),x6columnvar.get(),x7columnvar.get(),x8columnvar.get(),x9columnvar.get()] 
                
        content = []
        for i in range(8):
            for x in range(count):
                if df.columns[x] == arr[i]:
                    t = content.append(df.columns[x])
                
        length = len(content)
        z = 7
                
        if ycolumnvar.get()=='DEPT' :
            Label(root1,text=f'{8-length} Curve Code are Wrong, Please Check!!',font='calibri 12').grid(row=5,column=2) 
        else:
            Label(root1,text=f'{9-length} Curve Code are Wrong, Please Check!!',font='calibri 12').grid(row=5,column=2)     
        
        if length==8 and ycolumnvar.get()=='DEPT':
            Label(root1,text=f"Please Wait!! The file will download shortly",font='calibri 12').grid(row=5,column=2)
                    
        # Plotting the curves in subplots
        fig, axs = plt.subplots(1, 4, figsize=(58, 100))

        # Adjust the top margin
        plt.subplots_adjust(top=0.95)
        plt.yticks(fontsize=30)
                
        axs[0].plot(las[x1columnvar.get()], las[ycolumnvar.get()],label=x1columnvar.get(),color='red')
        axs[0].plot(las[x2columnvar.get()], las[ycolumnvar.get()], label=x2columnvar.get(),color='blue')
        axs[0].plot(las[x9columnvar.get()], las[ycolumnvar.get()],label=x9columnvar.get(), color='green')
        axs[0].set_title('TRACK 1 ',fontsize=30)
        axs[0].set_xlabel("Gamma ray  Caliper  SP log",fontsize=30)
        axs[0].invert_yaxis()
        axs[0].grid()
        axs[0].legend(fontsize='30')
        axs[0].tick_params(axis='y',labelsize=35,which='major',pad=5)
        axs[0].tick_params(axis='x',labelsize=30)
        axs[0].legend(fontsize='30')
        axs[0].yaxis.tick_right()

        # Subplot 2: 3 curves
        axs[1].loglog(las[x4columnvar.get()], las[ycolumnvar.get()], label=x4columnvar.get(),color='maroon')
        axs[1].loglog(las[x5columnvar.get()], las[ycolumnvar.get()], label=x5columnvar.get(),color='olive')
        axs[1].loglog(las[x6columnvar.get()], las[ycolumnvar.get()], label=x6columnvar.get(),color='purple')
        axs[1].set_title("TRACK 2",fontsize=30)
        axs[1].set_xlabel("Resistivity Log",fontsize=30)
        axs[1].set_ylabel(ycolumnvar.get(),fontsize=30)
        axs[1].set_yticklabels([]) 
        axs[1].set_xticklabels([10**i for i in range(3)]) 
        axs[1].set_facecolor('white')
        axs[1].invert_yaxis()
        axs[1].grid()
        axs[1].legend(fontsize='30')
        axs[1].tick_params(axis='y',labelsize=30)
        axs[1].tick_params(axis='x',labelsize=30)

        # Subplot 3: 3 curves
        axs[2].plot(las[x7columnvar.get()], las[ycolumnvar.get()], label=x7columnvar.get(),color='orange')
        axs[2].plot(las[x8columnvar.get()], las[ycolumnvar.get()], label=x8columnvar.get(),color='fuchsia')
        axs[2].set_title("TRACK 3",fontsize=30)
        axs[2].set_xlabel("Porosity Log",fontsize=30)
        axs[2].set_xlim(-30, 100)
        axs[2].invert_yaxis()
        axs[2].set_yticklabels([])
        axs[2].grid()
        axs[2].legend(fontsize='30')
        axs[2].tick_params(axis='y',labelsize=30)
        axs[2].tick_params(axis='x',labelsize=30)
                
        # Subplot 6: Color-coded curve
        def interpolate_data(curve_data):
            interpolated_data = []
            for i in range(len(curve_data) - 1):
                avg_value = (curve_data[i] + curve_data[i + 1]) / 2.0
                interpolated_data.extend([curve_data[i], avg_value])
            interpolated_data.append(curve_data[-1])
            return interpolated_data

        def create_color_coded_figure(data):
            curve_data = df[x2columnvar.get()].values
            interpolated_curve_data = interpolate_data(curve_data)
            color_ranges = [(0, 15, 'red'), (15, 35, 'blue'), (35, 60, 'navy'), (60, 100, 'yellow'), (100, 300, 'orange'), (300, 500, 'purple')]
            color_ranges.sort(key=lambda x: x[0])  # Sort the color ranges based on their lower bounds

            colors = []
            for val in data:
                found_color = False
                for r in color_ranges:
                    if r[0] <= val <= r[1]:
                        colors.append(r[2])
                        found_color = True
                        break
                if not found_color:
                    colors.append('green')

            # Plot the data with color coding
            axs[3].barh(range(len(curve_data)), [1] * len(curve_data), color=colors)  # Set the height of all bars to 1
            axs[3].set_title("TRACK 4",fontsize=30)
            axs[3].set_xlabel("Lithology",fontsize=30)
            axs[3].set_yticklabels([])
            axs[3].invert_yaxis()
            yellow_patc = mpatches.Patch(color='yellow',label='Shale')
            blue_patc = mpatches.Patch(color='blue',label='Sandstone')
            navy_patc = mpatches.Patch(color='navy',label='Limestone/Dolomite')
            red_patc = mpatches.Patch(color='red',label='Anhydrite')
            orange_patc = mpatches.Patch(color='orange',label='Organic Rich Shale')
            Others_patc = mpatches.Patch(color='green',label='Others')
            purple_patc = mpatches.Patch(color='purple',label='Sylnite(KCL)')
            axs[3].legend(handles=[yellow_patc,blue_patc,navy_patc,red_patc,orange_patc,purple_patc,Others_patc],fontsize=30)

        curve_data = df[x2columnvar.get()].values
        create_color_coded_figure(curve_data)

        curve_data = df[x2columnvar.get()].values
        interpolated_curve_data = interpolate_data(curve_data)
        create_color_coded_figure(interpolated_curve_data)

        # Adjust the spacing between subplots
        plt.tight_layout(pad=7.5)

        # Add x-axis label at the top
        for ax in axs:
            ax.xaxis.set_label_position('top')
            ax.xaxis.tick_top()
            # Customize the x-axis gridlines
            ax.xaxis.set_major_locator(plt.MultipleLocator(base=60.0))  # Set the grid spacing to 50 units
            # Customize the y-axis gridlines
            ax.yaxis.set_major_locator(plt.MultipleLocator(base=80.0))  # Set the grid spacing to 50 units

                
        well_log_file = f"{file_name_NEW}_Welllog.pdf"  # Generate the output PDF file name
        with PdfPages(well_log_file) as pdf:
            pdf.savefig(fig)
                
        # Close the plot
        plt.close(fig)

        Label(root1,text=f"The PDF file has been saved as {well_log_file}.",font='calibri 11').grid(row=5,column=2)
        
    Button(root1,text='Download PDF',command=threading).grid(row=4,column=2)
else :
    Label(root1,text='Please Select the file with .las extension',font='Calibri 15').grid(row=0,column=0)

root1.mainloop()
