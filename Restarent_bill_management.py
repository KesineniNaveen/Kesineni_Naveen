from tkinter import *
import random
import time
import datetime
from tkinter import messagebox, ttk

root=Tk()
root.geometry("1550x850+0+0")
root.title("Restaurant Management System")
root.configure(background='black')

#FRAMES



Tops = Frame(root, width=1550, height=80, bd=12, relief="raise")
Tops.pack(side = TOP)
lblTitle = Label(Tops, font=("arial", 50, 'bold'), text="             Restaurant Management System          ")
lblTitle.grid(row=0, column=0)


#DATE TIME


localtime=time.asctime(time.localtime(time.time()))
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,bd=10,anchor='w')
lblInfo.grid(row=1,column=0)



BottomMainFrame = Frame(root, width=1550, height=770, bd=12, relief="raise")
BottomMainFrame.pack(side=BOTTOM)

f1 = Frame(BottomMainFrame, width=500, height=770, bd=12, relief=SUNKEN)
f1.pack(side=LEFT)

f1top = Frame(f1, width=500, height=570, bd=12, relief="raise")
f1top.pack(side=TOP)
f1bottom = Frame(f1, width=500, height=200, bd=12, relief="raise")
f1bottom.pack(side=BOTTOM)


f2 = Frame(BottomMainFrame, width=400, height=770, bd=12, relief=SUNKEN)
f2.pack(side=LEFT)
f2Top = Frame(f2, width=400, height=350, bd=4, relief="raise")
f2Top.pack(side=TOP)
f2Bottom = Frame(f2, width=400, height=450,bd=4, relief="raise")
f2Bottom.pack(side=BOTTOM)

f3 = Frame(BottomMainFrame, width=400, height=770, bd=12, relief=SUNKEN)
f3.pack(side=RIGHT)

f3top = Frame(f3, width=400, height=770, bd=12, relief="raise")
f3top.pack(side=TOP)
f3bottom = Frame(f3, width=400, height=100, bd=12, relief="raise")
f3bottom.pack(side=BOTTOM)


#VARIABLES


Receipt_Ref = StringVar()
DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%y"))


var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var100 = IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var100.set(0)

#BOTTOM FRAME : FRAME 1 VARIABLE


varTea = StringVar()
varBlackTea = StringVar()
varGreenTea = StringVar()
varChai = StringVar()
varLemonTea = StringVar()
varCoffee = StringVar()
varBlackCoffee = StringVar()
varColdCoffee = StringVar()

varTea.set(0)
varBlackTea.set(0)
varGreenTea.set(0)
varChai.set(0)
varLemonTea.set(0)
varCoffee.set(0)
varBlackCoffee.set(0)
varColdCoffee.set(0)

#BOTTOM FRAME : FRAME 2 TOP FRAME VARIABLES


varSamosa = StringVar()
varMomo = StringVar()
varVadaPav = StringVar()
varDosa = StringVar()
varVada = StringVar()

varSamosa.set(0)
varMomo.set(0)
varVadaPav.set(0)
varDosa.set(0)
varVada.set(0)

#BOTTOM FRAME : FRAME 2 BOTTOM FRAME VARIABLES


varTotal = StringVar()
varCGST = StringVar()
varSGST = StringVar()
varServiceCharge = StringVar()
varPay = StringVar()
varPM = StringVar()
varTotal.set(0)
varCGST.set(0)
varSGST.set(0)
varServiceCharge.set(0)
varPay.set(0)

#BOTTOM FRAME : FRAME 3 VARIABLES


varMango = StringVar()
varOrange = StringVar()
varGrapes = StringVar()
varPineApple = StringVar()
varWaterMelon= StringVar()
varBuiscut = StringVar()
varSaltBuiscut = StringVar()
varSugarBuiscut = StringVar()
varOsmaniyaBuiscut = StringVar()

varMango.set(0)
varOrange.set(0)
varGrapes.set(0)
varPineApple.set(0)
varWaterMelon.set(0)
varBuiscut.set(0)
varSaltBuiscut.set(0)
varSugarBuiscut.set(0)
varOsmaniyaBuiscut.set(0)



# Button Functions

def iExit():
    qExit = messagebox.askyesno("Restaurant Management","Do you want to quit ?")
    if qExit > 0:
        root.destroy()
        return
        


def Reset():
    varTea.set(0)
    varBlackTea.set(0)
    varGreenTea.set(0)
    varChai.set(0)
    varLemonTea.set(0)
    varCoffee.set(0)
    varBlackCoffee.set(0)
    varColdCoffee.set(0)
    varSamosa.set(0)
    varMomo.set(0)
    varVadaPav.set(0)
    varDosa.set(0)
    varVada.set(0)
    varTotal.set(0)
    varCGST.set(0)
    varSGST.set(0)
    varServiceCharge.set(0)
    varPay.set(0)
    varMango.set(0)
    varOrange.set(0)
    varGrapes.set(0)
    varPineApple.set(0)
    varWaterMelon.set(0)
    varBuiscut.set(0)
    varSaltBuiscut.set(0)
    varSugarBuiscut.set(0)
    varOsmaniyaBuiscut.set(0)
    
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)


    txtTea.configure(state=DISABLED)
    txtBlackTea.configure(state=DISABLED)
    txtGreenTea.configure(state=DISABLED)
    txtChai.configure(state=DISABLED)
    txtLemonTea.configure(state=DISABLED)
    txtCoffee.configure(state=DISABLED)
    txtBlackCoffee.configure(state=DISABLED)
    txtColdCoffee.configure(state=DISABLED)
    txtSamosa.configure(state=DISABLED)
    txtMomo.configure(state=DISABLED)
    txtVadaPav.configure(state=DISABLED)
    txtDosa.configure(state=DISABLED)
    txtVada.configure(state=DISABLED)
    txtTotal.configure(state=DISABLED)
    txtCGST.configure(state=DISABLED)
    txtSGST.configure(state=DISABLED)
    txtServiceCharge.configure(state=DISABLED)
    txtPay.configure(state=DISABLED)
    txtMango.configure(state=DISABLED)
    txtOrange.configure(state=DISABLED)
    txtGrapes.configure(state=DISABLED)
    txtPineApple.configure(state=DISABLED)
    txtWaterMelon.configure(state=DISABLED)
    txtBusict.configure(state=DISABLED)
    txtSaltBusict.configure(state=DISABLED)
    txtSugarBusict.configure(state=DISABLED)
    txtOsmaniyaBuiscut.configure(state=DISABLED)
    
    

# RECEIPT FUNCTION

def Receipt():
    roor = Tk()
    roor.geometry("600x700+0+0")

    f1 = Frame(roor, width = 1600, height = 700, bd = 12, relief = "raise")
    f1.pack()
    lblReceipt = Label(f1, font=('arial', 12, 'bold'), text="Receipt", bd=2, anchor='w')
    lblReceipt.grid(row=0, column=0, sticky=W)
    txtReceipt = Text(f1, width=64, height=35, bg="white", bd=8, font=('arial', 11, 'bold'))
    txtReceipt.grid(row=1, column=0)
    txtReceipt.delete("1.0", END)
    x = random.randint(1000, 500890)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)
    
    
    
    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ Receipt_Ref.get() + '\t\t\t' + DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t\t\t' + "No. of Items \n\n")
    txtReceipt.insert(END, 'Tea:\t\t\t\t\t' + varTea.get() + "\n")
    txtReceipt.insert(END, 'BlackTea: \t\t\t\t\t' + varBlackTea.get() + "\n")
    txtReceipt.insert(END, 'GreenTea: \t\t\t\t\t' + varGreenTea.get() + "\n")
    txtReceipt.insert(END, 'Chai: \t\t\t\t\t' + varChai.get() + "\n")
    txtReceipt.insert(END, 'LemonTea: \t\t\t\t\t' + varLemonTea.get() + "\n")
    txtReceipt.insert(END, 'Coffee: \t\t\t\t\t' + varCoffee.get() + "\n")
    txtReceipt.insert(END, 'BlackCoffee: \t\t\t\t\t' + varBlackCoffee.get() + "\n")
    txtReceipt.insert(END, 'ColdCoffee: \t\t\t\t\t' + varColdCoffee.get() + "\n")
    txtReceipt.insert(END, 'Samosa: \t\t\t\t\t' + varSamosa.get() + "\n")
    txtReceipt.insert(END, 'Momo: \t\t\t\t\t' + varMomo.get() + "\n")
    txtReceipt.insert(END, 'VadaPav: \t\t\t\t\t' + varVadaPav.get() + "\n")
    txtReceipt.insert(END, 'Dosa: \t\t\t\t\t' + varDosa.get() + "\n")
    txtReceipt.insert(END, 'Vada: \t\t\t\t\t' + varVada.get() + "\n")
    txtReceipt.insert(END, 'Mango: \t\t\t\t\t' + varMango.get() + "\n")
    txtReceipt.insert(END, 'Orange: \t\t\t\t\t' + varOrange.get() + "\n")
    txtReceipt.insert(END, 'Grapes: \t\t\t\t\t' + varGrapes.get() + "\n")
    txtReceipt.insert(END, 'PineApple: \t\t\t\t\t' + varPineApple.get() + "\n")
    txtReceipt.insert(END, 'WaterMelon: \t\t\t\t\t' + varWaterMelon.get() + "\n")
    txtReceipt.insert(END, 'Buiscut: \t\t\t\t\t' + varBuiscut.get() + "\n")
    txtReceipt.insert(END, 'SaltBuiscut: \t\t\t\t\t' + varSaltBuiscut.get() + "\n")
    txtReceipt.insert(END, 'SugarBuiscut: \t\t\t\t\t' + varSugarBuiscut.get() + "\n")
    txtReceipt.insert(END, 'OsmaniyaBuiscut: \t\t\t\t\t' + varOsmaniyaBuiscut.get() + "\n")
    txtReceipt.insert(END, '\nTotal Cost of Food: \t\t' + varTotal.get() + "\nCGST:\t\t" + varCGST.get() + "\nSGST:\t\t" +
                      varSGST.get() + "\nService Charge:\t\t" + varServiceCharge.get() + "\nTotal Payble amount:\t\t" + varPay.get())
    roor.mainloop()
    
    
    
    

def price_list():
    roo = Tk()
    roo.geometry("600x700+0+0")
    roo.title("Price List")

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tea", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="BlackTea", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="GreenTea", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chai", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="LemonTea", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Coffee", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="BlackCoffee", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ColdCoffee", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Samosa", fg="steel blue", anchor=W)
    lblinfo.grid(row=9, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=9, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Momo", fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15", fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="VadaPav", fg="steel blue", anchor=W)
    lblinfo.grid(row=11, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=11, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Dosa", fg="steel blue", anchor=W)
    lblinfo.grid(row=12, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20", fg="steel blue", anchor=W)
    lblinfo.grid(row=12, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Vada", fg="steel blue", anchor=W)
    lblinfo.grid(row=13, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=13, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Mango", fg="steel blue", anchor=W)
    lblinfo.grid(row=14, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=14, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Orange", fg="steel blue", anchor=W)
    lblinfo.grid(row=15, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=15, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Grapes", fg="steel blue", anchor=W)
    lblinfo.grid(row=16, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20", fg="steel blue", anchor=W)
    lblinfo.grid(row=16, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PineApple", fg="steel blue", anchor=W)
    lblinfo.grid(row=17, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=17, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="WaterMelon", fg="steel blue", anchor=W)
    lblinfo.grid(row=18, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=18, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Buiscut", fg="steel blue", anchor=W)
    lblinfo.grid(row=19, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=19, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="SaltBuiscut", fg="steel blue", anchor=W)
    lblinfo.grid(row=20, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="105", fg="steel blue", anchor=W)
    lblinfo.grid(row=20, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="SugarBuiscut", fg="steel blue", anchor=W)
    lblinfo.grid(row=21, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=21, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="OsmaniyaBuiscut", fg="steel blue", anchor=W)
    lblinfo.grid(row=20, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="105", fg="steel blue", anchor=W)
    lblinfo.grid(row=20, column=3)
    roo.mainloop()








def TotalCost():
    m1 = float(varTea.get())
    m2 = float(varBlackTea.get())
    m3 = float(varGreenTea.get())
    m4 = float(varChai.get())
    m5 = float(varGreenTea.get())
    m6 = float(varCoffee.get())
    m7 = float(varBlackCoffee.get())
    m8 = float(varColdCoffee.get())
    m9 = float(varSamosa.get())
    m10 = float(varMomo.get())
    m11 = float(varVadaPav.get())
    m12 = float(varDosa.get())
    m13 = float(varVada.get())
    m14 = float(varMango.get())
    m15 = float(varOrange.get())
    m16 = float(varGrapes.get())
    m17 = float(varPineApple.get())
    m18 = float(varWaterMelon.get())
    m19 = float(varBuiscut.get())
    m20 = float(varSaltBuiscut.get())
    m21 = float(varSugarBuiscut.get())

    iTotal = (m1*10 + m2*15 + m3*20 + m4*10 + m5*25 + m6*30 + m7*20 + m8*25 + m9*10 + m10*15 + m11*35 + m12*20 + m13*30 + m14*50 + m15*10 + m16*20 +
                 m17*50 + m18*25 + m19*105 + m20*50 + m21*105)

    striTotal = 'Rs',str(iTotal)
    varTotal.set(striTotal)

    cgst = (9/100)*iTotal
    strcgst = 'Rs',str(cgst)
    varCGST.set(strcgst)

    sgst = (9/100)*iTotal
    strsgst = 'Rs',str(sgst)
    varSGST.set(strsgst)

    service_charge = 0.1*iTotal
    strService_charge = "Rs",str(service_charge)
    varServiceCharge.set(strService_charge)

    strPay = 'Rs', str('%.2f'%(iTotal+cgst+sgst+service_charge))
    varPay.set(strPay)







def a():
    if var1.get() == 1:
        txtTea.configure(state=NORMAL)
        varTea.set("")
    elif var1.get() == 0:
        txtTea.configure(state=DISABLED)
        varTea.set("0")

def b():
    if var2.get() == 1:
        txtBlackTea.configure(state=NORMAL)
        varBlackTea.set("")
    elif var2.get() == 0:
        txtBlackTea.configure(state=DISABLED)
        varBlackTea.set("0")

def c():
    if var3.get() == 1:
        txtGreenTea.configure(state=NORMAL)
        varGreenTea.set("")
    elif var3.get() == 0:
        txtGreenTea.configure(state=DISABLED)
        varGreenTea.set("0")

def d():
    if var4.get() == 1:
        txtChai.configure(state=NORMAL)
        varChai.set("")
    elif var4.get() == 0:
        txtChai.configure(state=DISABLED)
        varChai.set("0")

def e():
    if var5.get() == 1:
        txtLemonTea.configure(state=NORMAL)
        varLemonTea.set("")
    elif var5.get() == 0:
        txtLemonTea.configure(state=DISABLED)
        varLemonTea.set("0")


def f():
    if var6.get() == 1:
        txtCoffee.configure(state=NORMAL)
        varCoffee.set("")
    elif var6.get() == 0:
        txtCoffee.configure(state=DISABLED)
        varCoffee.set("0")

def g():
    if var7.get() == 1:
        txtBlackCoffee.configure(state=NORMAL)
        varBlackCoffee.set("")
    elif var7.get() == 0:
        txtBlackCoffee.configure(state=DISABLED)
        varBlackCoffee.set("0")

def h():
    if var8.get() == 1:
        txtColdCoffee.configure(state=NORMAL)
        varColdCoffee.set("")
    elif var8.get() == 0:
        txtColdCoffee.configure(state=DISABLED)
        varColdCoffee.set("0")

def i():
    if var9.get() == 1:
        txtSamosa.configure(state=NORMAL)
        varSamosa.set("")
    elif var9.get() == 0:
        txtSamosa.configure(state=DISABLED)
        varSamosa.set("0")

def j():
    if var10.get() == 1:
        txtMomo.configure(state=NORMAL)
        varMomo.set("")
    elif var10.get() == 0:
        txtMomo.configure(state=DISABLED)
        varMomo.set("0")

def k():
    if var11.get() == 1:
        txtVadaPav.configure(state=NORMAL)
        varVadaPav.set("")
    elif var11.get() == 0:
        txtVadaPav.configure(state=DISABLED)
        varVadaPav.set("0")
        
def l():
    if var12.get() == 1:
        txtDosa.configure(state=NORMAL)
        varDosa.set("")
    elif var12.get() == 0:
        txtDosa.configure(state=DISABLED)
        varDosa.set("0")
        
def m():
    if var13.get() == 1:
        txtVada.configure(state=NORMAL)
        varVada.set("")
    elif var13.get() == 0:
        txtVada.configure(state=DISABLED)
        varVada.set("0")
        
def n():
    if var14.get() == 1:
        txtMango.configure(state=NORMAL)
        varMango.set("")
    elif var14.get() == 0:
        txtMango.configure(state=DISABLED)
        varMango.set("0")
        
def o():
    if var15.get() == 1:
        txtOrange.configure(state=NORMAL)
        varOrange.set("")
    elif var15.get() == 0:
        txtOrange.configure(state=DISABLED)
        varOrange.set("0")
        
def p():
    if var16.get() == 1:
        txtGrapes.configure(state=NORMAL)
        varGrapes.set("")
    elif var16.get() == 0:
        txtGrapes.configure(state=DISABLED)
        varGrapes.set("0")
        
def q():
    if var17.get() == 1:
        txtPineApple.configure(state=NORMAL)
        varPineApple.set("")
    elif var17.get() == 0:
        txtPineApple.configure(state=DISABLED)
        varPineApple.set("0")
        
def r():
    if var18.get() == 1:
        txtWaterMelon.configure(state=NORMAL)
        varWaterMelon.set("")
    elif var18.get() == 0:
        txtWaterMelon.configure(state=DISABLED)
        varWaterMelon.set("0")
        
def s():
    if var19.get() == 1:
        txtBuiscut.configure(state=NORMAL)
        varBuiscut.set("")
    elif var19.get() == 0:
        txtBuiscut.configure(state=DISABLED)
        varBuiscut.set("0")
        
def u():
    if var20.get() == 1:
        txtSaltBusict.configure(state=NORMAL)
        varSaltBusict.set("")
    elif var20.get() == 0:
        txtSaltBusict.configure(state=DISABLED)
        varSaltBusict.set("0")
        



def v():
    if var21.get() == 1:
        txtSugarBusict.configure(state=NORMAL)
        varSugarBusict.set("")
    elif var20.get() == 0:
        txtSugarBusict.configure(state=DISABLED)
        varSugarBusict.set("0")
        
        

def w():
    if var22.get() == 1:
        txtOsmaniyaBuiscut.configure(state=NORMAL)
        varOsmaniyaBuiscut.set("")
    elif var20.get() == 0:
        txtOsmaniyaBuiscut.configure(state=DISABLED)
        varOsmaniyaBuiscut.set("0")
        
        
        

lblMeal = Label(f1top,font=("arial",25,'bold'), text="Teas")
lblMeal.grid(row=0, column=0)

Tea = Checkbutton(f1top, text="Tea", variable=var1, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=a)
Tea.grid(row=1, column=0, sticky = W)
txtTea = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varTea, width=4, justify="right",state=DISABLED)
txtTea.grid(row=1, column=1)

BlackTea = Checkbutton(f1top, text="BlackTea", variable=var2, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=b)
BlackTea.grid(row=2, column=0, sticky = W)
txtBlackTea = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varBlackTea, width=4, justify="right",state=DISABLED)
txtBlackTea.grid(row=2, column=1)

GreenTea = Checkbutton(f1top, text="GreenTea", variable=var3, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=c)
GreenTea.grid(row=3, column=0, sticky = W)
txtGreenTea = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varGreenTea, width=4, justify="right",state=DISABLED)
txtGreenTea.grid(row=3, column=1)

Chai = Checkbutton(f1top, text="Chai", variable=var4, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=d)
Chai.grid(row=4, column=0, sticky = W)
txtChai = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varChai, width=4, justify="right",state=DISABLED)
txtChai.grid(row=4, column=1)

LemonTea = Checkbutton(f1top, text="LemonTea", variable=var5, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=e)
LemonTea.grid(row=5, column=0, sticky = W)
txtLemonTea = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varLemonTea, width=4, justify="right",state=DISABLED)
txtLemonTea.grid(row=5, column=1)

lblSpace = Label(f1top,text="\n")
lblSpace.grid(row=6, column=0)
lblSandwich = Label(f1top,font=("arial",25,'bold'), text="COFFEE")
lblSandwich.grid(row=7, column=0)

Coffee = Checkbutton(f1top, text="Coffee", variable=var6, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=f)
Coffee.grid(row=8, column=0, sticky = W)
txtCoffee = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varCoffee, width=4, justify="right",state=DISABLED)
txtCoffee.grid(row=8, column=1)

BlackCoffee = Checkbutton(f1top, text="BlackCoffee", variable=var7, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=g)
BlackCoffee.grid(row=9, column=0, sticky = W)
txtBlackCoffee = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varBlackCoffee, width=4, justify="right",state=DISABLED)
txtBlackCoffee.grid(row=9, column=1)

ColdCoffee = Checkbutton(f1top, text="ColdCoffee", variable=var8, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=h)
ColdCoffee.grid(row=10, column=0, sticky = W)
txtColdCoffee = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varColdCoffee, width=4, justify="right",state=DISABLED)
txtColdCoffee.grid(row=10, column=1)


btnReceipt=Button(f1bottom,padx=20,pady=2,bd=14,fg="black",font=('arial',16,'bold'),width=16,text="GENERATE RECEIPT", command = Receipt)
btnReceipt.grid(row=0,column=0)


















lblMeal = Label(f2Top,font=("arial",25,'bold'), text="TIFFIN'S")
lblMeal.grid(row=0, column=0)

Samosa = Checkbutton(f2Top, text="Samosa", variable=var9, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=i)
Samosa.grid(row=1, column=0, sticky = W)
txtSamosa = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varSamosa, width=4, justify="right",state=DISABLED)
txtSamosa.grid(row=1, column=1)

Momo = Checkbutton(f2Top, text="Momo", variable=var10, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=j)
Momo.grid(row=2, column=0, sticky = W)
txtMomo = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varMomo, width=4, justify="right",state=DISABLED)
txtMomo.grid(row=2, column=1)

VadaPav = Checkbutton(f2Top, text="VadaPav", variable=var11, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=k)
VadaPav.grid(row=3, column=0, sticky = W)
txtVadaPav = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varVadaPav, width=4, justify="right",state=DISABLED)
txtVadaPav.grid(row=3, column=1)

Dosa = Checkbutton(f2Top, text="Dosa", variable=var12, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=l)
Dosa.grid(row=4, column=0, sticky = W)
txtDosa = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varDosa, width=4, justify="right",state=DISABLED)
txtDosa.grid(row=4, column=1)

Vada = Checkbutton(f2Top, text="Vada", variable=var13, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=m)
Vada.grid(row=5, column=0, sticky = W)
txtVada = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varVada, width=4, justify="right",state=DISABLED)
txtVada.grid(row=5, column=1)


















lblPaymentMethod = Label(f2Bottom, font=("arial", 18, 'bold'), text = "Payment Method", bd=10, width=16, anchor='w')
lblPaymentMethod.grid(row=0,column=0)

cmbPaymentMethod = ttk.Combobox(f2Bottom, textvariable=varPM, state="readonly", font=("arial", 10, 'bold'), width=20)
cmbPaymentMethod['value']=('Cash','Paytm','Master Card','Visa Card','Debit Card')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=0, column=1)

lblTotal = Label(f2Bottom, font=("arial", 18, 'bold'), text = "Total", bd=10, width=16, anchor='e')
lblTotal.grid(row=2,column=1)
txtTotal = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varTotal, width=10, justify="right",state=DISABLED)
txtTotal.grid(row=2, column=2)

lblSGST = Label(f2Bottom, font=("arial", 18, 'bold'), text = "SGST @9%", bd=10, width=16, anchor='e')
lblSGST.grid(row=3,column=1)
txtSGST = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varSGST, width=10, justify="right",state=DISABLED)
txtSGST.grid(row=3, column=2)

lblCGST = Label(f2Bottom, font=("arial", 18, 'bold'), text = "CGST @9%", bd=10, width=16, anchor='e')
lblCGST.grid(row=4,column=1)
txtCGST = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varCGST, width=10, justify="right",state=DISABLED)
txtCGST.grid(row=4, column=2)

lblServiceCharge = Label(f2Bottom, font=("arial", 18, 'bold'), text = "Service Charge @10%", bd=10, width=16, anchor='e')
lblServiceCharge.grid(row=5,column=1)
txtServiceCharge = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varServiceCharge, width=10, justify="right",state=DISABLED)
txtServiceCharge.grid(row=5, column=2)
















#======================================================================================================================
#                                     BUTTONS
#======================================================================================================================
btnprice=Button(f2Bottom,padx=20,pady=1, bd=14 ,fg="black",font=('arial' ,16,'bold'),width=5, text="PRICE LIST", command = price_list)
btnprice.grid(row=2, column=0)

btnTotal = Button(f2Bottom, padx=20, pady=1, bd=14, fg="black", font=("arial", 16, 'bold'), width=5,
                  text="TOTAL", command = TotalCost).grid(row=3, column=0)

btnReset=Button(f2Bottom,padx=20,pady=1,bd=14,fg="black",font=('arial',16,'bold'),width=5,text="RESET", command=Reset)
btnReset.grid(row=4,column=0)

btnExit=Button(f2Bottom,padx=20,pady=1,bd=14,fg="black",font=('arial',16,'bold'),width=5,text="EXIT", command = iExit)
btnExit.grid(row=5,column=0)





















#================================================================================
#                       FRAME 3
# ================================================================================

lblDrinks = Label(f3top,font=("arial",25,'bold'), text="Fruits")
lblDrinks.grid(row=0, column=0)

Mango = Checkbutton(f3top, text="Mango", variable=var14, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=n)
Mango.grid(row=1, column=0, sticky = W)
txtMango = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varMango, width=4, justify="right",state=DISABLED)
txtMango.grid(row=1, column=1)

Orange = Checkbutton(f3top, text="Orange", variable=var15, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=o)
Orange.grid(row=2, column=0, sticky = W)
txtOrange = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varOrange, width=4, justify="right",state=DISABLED)
txtOrange.grid(row=2, column=1)

Grapes = Checkbutton(f3top, text="Grapes", variable=var16, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=p)
Grapes.grid(row=3, column=0, sticky = W)
txtGrapes = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varGrapes, width=4, justify="right",state=DISABLED)
txtGrapes.grid(row=3, column=1)

PineApple = Checkbutton(f3top, text="PineApple", variable=var17, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=q)
PineApple.grid(row=4, column=0, sticky = W)
txtPineApple = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varPineApple, width=4, justify="right",state=DISABLED)
txtPineApple.grid(row=4, column=1)

WaterMelon = Checkbutton(f3top, text="WaterMelon", variable=var18, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=r)
WaterMelon.grid(row=5, column=0, sticky = W)
txtWaterMelon = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varWaterMelon, width=4, justify="right",state=DISABLED)
txtWaterMelon.grid(row=5, column=1)

lblSpace = Label(f3top,text="\n\n")
lblSpace.grid(row=6, column=0)

lblShakes = Label(f3top,font=("arial",25,'bold'), text="Buiscut")
lblShakes.grid(row=7, column=0)

Buiscut = Checkbutton(f3top, text="Buiscut", variable=var19, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=s)
Buiscut.grid(row=8, column=0, sticky = W)
txtBuiscut = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varBuiscut, width=4, justify="right",state=DISABLED)
txtBuiscut.grid(row=8, column=1)

SaltBuiscut = Checkbutton(f3top, text="SaltBuiscut", variable=var20, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=u)
SaltBuiscut.grid(row=9, column=0, sticky = W)
txtSaltBusict = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varSaltBuiscut, width=4, justify="right",state=DISABLED)
txtSaltBusict.grid(row=9, column=1)

SugarBuiscut = Checkbutton(f3top, text="SugarBuiscut", variable=var21, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=v)
SugarBuiscut.grid(row=10, column=0, sticky = W)
txtSugarBusicut = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varSugarBuiscut, width=4, justify="right",state=DISABLED)
txtSugarBusicut.grid(row=10, column=1)

#lblSpace = Label(f3top,text="\n\n\n\n\n")
#lblSpace.grid(row=11, column=0)

lblpay = Label(f3bottom, font=("arial", 18, 'bold'), text = "Total Payable Amount", fg="red", bd=10, width=16, anchor='e')
lblpay.grid(row=0, column=0)
txtpay = Entry(f3bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varPay, width=10, justify="right",state=DISABLED)
txtpay.grid(row=0, column=1)

root.mainloop()