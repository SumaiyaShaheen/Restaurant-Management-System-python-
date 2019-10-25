from Tkinter import*
import random
import time;

root = Tk()
root.geometry('1600x800+0+0')
root.title('RESTURANT MANAGEMENT SYSTEM')
root.configure(bg='blue')

class Main():
    @staticmethod
    def qexit():
        root.destroy()

    @staticmethod
    def reset():
        rand.set(0)
        chargha_biryani.set(0)
        malai_kofta.set(0)
        chicken_karahi.set(0)
        chicken_chapli_kabbab.set(0)
        Subtotal.set(0)
        Total.set(0)
        Service_Charge.set(0)
        beef_steak_sandwich.set(0)
        Tax.set(0)
        cost.set(0)
        crump_chicken_burger.set(0)
        Beef_nihari.set(0)
        herbed_cheese_sticks.set(0)
        crispy_fluffy_fish.set(0)
        black_pepper_prawns.set(0)
        mix_berry_chiller.set(0)
        Herbal_tea.set(0)
        lime_drink.set(0)
        bread_pudding.set(0)
        fruit_tart.set(0)
        pistaicecream.set(0)
        


    @staticmethod
    def total():
        x=random.randint(12980, 50876)
        randomRef = str(x)
        rand.set(randomRef)

        co_of_charghaBiryani =float(chargha_biryani.get())
        co_of_malai_kofta= float(malai_kofta.get())
        co_of_chicken_karahi= float(chicken_karahi.get())
        co_of_chicken_chapli_kabbab= float(chicken_chapli_kabbab.get())
        co_of_crump_chicken_burger= float(crump_chicken_burger.get())
        co_of_beef_steak_sandwich= float(beef_steak_sandwich.get())
        co_of_Beef_nihari= float(Beef_nihari.get())
        co_of_herbed_cheese_sticks= float(herbed_cheese_sticks.get())
        co_of_crispy_fluffyfish = float(crispy_fluffy_fish.get())
        co_of_blackpepper_prawns = float(black_pepper_prawns.get())
        co_of_mix_berryChiller=float(mix_berry_chiller.get())
        co_of_Herbal_tea = float(Herbal_tea.get())
        co_of_lime_drink = float(lime_drink.get())
        co_of_brePudding=float(bread_pudding.get())
        co_of_fruitTart=float(fruit_tart.get())
        CofPistaIceCream = float(pistaicecream.get())

        Co_of_CharghaBiryani = co_of_charghaBiryani*395
        Co_of_Malai_Kofta = co_of_malai_kofta * 250
        Co_of_ChickenKarahi = co_of_chicken_karahi *450
        Co_of_Chicken_chapliKabbab = co_of_chicken_chapli_kabbab * 250
        Co_of_Crump_chickenBurger = co_of_crump_chicken_burger * 450
        Co_of_Beef_Steak_Sandwich = co_of_beef_steak_sandwich * 350
        Co_of_BeefNihari = co_of_Beef_nihari * 400
        Co_of_Herbed_CheeseSticks = co_of_herbed_cheese_sticks * 300
        Co_of_Crispy_fluffyfish = co_of_crispy_fluffyfish * 900
        Co_of_Blackpepper_Prawns = co_of_blackpepper_prawns *750
        Co_of_Mix_BerryChiller = co_of_mix_berryChiller * 335
        Co_of_Herbaltea = co_of_Herbal_tea * 175
        Co_of_Lime_Drink = co_of_lime_drink * 300     
        Co_of_BrePudding =co_of_brePudding * 395
        Co_of_FruitTart= co_of_fruitTart * 300
        Co_of_PistaiceCream = CofPistaIceCream * 175

        costofmeal = "Rs.",str('%.2f'% (Co_of_Herbed_CheeseSticks + Co_of_Beef_Steak_Sandwich + Co_of_Crump_chickenBurger + Co_of_Chicken_chapliKabbab + Co_of_Lime_Drink + Co_of_ChickenKarahi + Co_of_Malai_Kofta + Co_of_BeefNihari + Co_of_Mix_BerryChiller+ Co_of_Crispy_fluffyfish + Co_of_Blackpepper_Prawns + Co_of_Herbaltea+ Co_of_CharghaBiryani + Co_of_PistaiceCream + Co_of_FruitTart + Co_of_BrePudding))
        PayTax=(Co_of_Herbed_CheeseSticks + Co_of_Beef_Steak_Sandwich + Co_of_Lime_Drink + Co_of_Crump_chickenBurger +Co_of_Chicken_chapliKabbab + Co_of_ChickenKarahi + Co_of_Malai_Kofta + Co_of_BeefNihari + Co_of_Mix_BerryChiller + Co_of_Crispy_fluffyfish + Co_of_Blackpepper_Prawns + Co_of_Herbaltea + Co_of_CharghaBiryani + Co_of_FruitTart + Co_of_PistaiceCream  +  Co_of_BrePudding)*0.33
        Totalcost=(Co_of_Herbed_CheeseSticks + Co_of_Beef_Steak_Sandwich + Co_of_Crump_chickenBurger +Co_of_Chicken_chapliKabbab + Co_of_Lime_Drink + Co_of_ChickenKarahi + Co_of_Malai_Kofta + Co_of_BeefNihari + Co_of_Mix_BerryChiller + Co_of_Crispy_fluffyfish + Co_of_Blackpepper_Prawns + Co_of_Herbaltea + Co_of_CharghaBiryani +  Co_of_FruitTart + Co_of_PistaiceCream +  Co_of_BrePudding)
        Ser_Charge=((Co_of_Herbed_CheeseSticks + Co_of_Beef_Steak_Sandwich + Co_of_Crump_chickenBurger +Co_of_Chicken_chapliKabbab + Co_of_Lime_Drink + Co_of_ChickenKarahi + Co_of_Malai_Kofta + Co_of_BeefNihari + Co_of_Mix_BerryChiller + Co_of_Crispy_fluffyfish + Co_of_Blackpepper_Prawns + Co_of_Herbaltea + Co_of_CharghaBiryani  + Co_of_FruitTart + Co_of_PistaiceCream  +  Co_of_BrePudding)/99)
        Service="Rs.",str('%.2f'% Ser_Charge)
        OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
        PaidTax="Rs.",str('%.2f'% PayTax)

        Service_Charge.set(Service)
        cost.set(costofmeal)
        Tax.set(PaidTax)
        Subtotal.set(costofmeal)
        Total.set(OverAllCost)
    def func(self):
        self.receipt
  
    
z=Main()


Tops = Frame(root, width =1600,height =200, bd=10,bg = 'white', relief = 'raise')
Tops.pack(side = TOP)
 
f1 = Frame(root, width =800,height =600, bd=8,bg = 'white', relief = 'groove')
f1.pack(side = LEFT)

f2 = Frame(root, width =800,height =600, bd=8,bg = 'white', relief = 'groove')
f2.pack(side = RIGHT)

Tops.configure(background='purple')
f1.configure(background='green')
f2.configure(background='black')

#===f1
f1a = Frame(f1, width=600, height=400, bd=8, relief="raise")
f1a.pack(side=TOP)

f1b = Frame(f1, width=100, height=200, bd=8, relief="raise")
f1b.pack(side=BOTTOM)

#===f2
f2a = Frame(f2, width=600, height=400, bd=8, relief="raise")
f2a.pack(side=TOP)

f2b = Frame(f2, width=100, height=200, bd=8, relief="raise")
f2b.pack(side=BOTTOM)


#============================time===================================
localtime = time.asctime(time.localtime(time.time()))
#============================Info===================================

lblInfo = Label(Tops, font =('arial',48, 'bold'),text = '@RESTAURANT MANAGEMENT SYSTEM@', bd=20, anchor='w')
lblInfo.grid(row =0, column=0)

lblInfo = Label(Tops, font =('arial',20, 'bold'),text = localtime , bd=10, anchor='w')
lblInfo.grid(row =1, column=0)

#status = Label(f1a,font=('arial', 15, 'bold'),width = 16, text="- sumaiya shaheen",bd=2,relief=SUNKEN)
#status.grid(row=8,columnspan=3)

#---------------------------------------------------------------------------------------
rand = StringVar()
chargha_biryani = StringVar()
malai_kofta = StringVar()
chicken_karahi = StringVar()
chicken_chapli_kabbab = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
beef_steak_sandwich = StringVar()
Tax = StringVar()
cost = StringVar()
crump_chicken_burger = StringVar()
Beef_nihari = StringVar()
herbed_cheese_sticks= StringVar()
crispy_fluffy_fish = StringVar()
black_pepper_prawns = StringVar()
mix_berry_chiller = StringVar()
Herbal_tea = StringVar()
lime_drink = StringVar()
bread_pudding=StringVar()
fruit_tart=StringVar()
pistaicecream = StringVar()

rand.set(0)
chargha_biryani.set(0)
malai_kofta.set(0)
chicken_karahi.set(0)
chicken_chapli_kabbab.set(0)
Subtotal.set(0)
Total.set(0)
Service_Charge.set(0)
beef_steak_sandwich.set(0)
Tax.set(0)
cost.set(0)
crump_chicken_burger.set(0)
Beef_nihari.set(0)
herbed_cheese_sticks.set(0)
crispy_fluffy_fish.set(0)
black_pepper_prawns.set(0)
mix_berry_chiller.set(0)
Herbal_tea.set(0)
lime_drink.set(0)
bread_pudding.set(0)
fruit_tart.set(0)
pistaicecream.set(0)

lblbread_pudding = Label(f2a, font=( 'arial' ,16, 'bold' ),text="Bread Pudding",bd=10,anchor='w')
lblbread_pudding.grid(row=0,column=4)
txtbread_pudding = Entry(f2a,font=('arial' ,14,'bold'), textvariable=bread_pudding , bd=6,insertwidth=4 ,justify='right')
txtbread_pudding.grid(row=0,column=5)

lblfruit_tart = Label(f2a, font=( 'arial' ,16, 'bold' ),text="Fruit Tart ",bd=10,anchor='w')
lblfruit_tart.grid(row=1,column=4)
txtfruit_tart = Entry(f2a,font=('arial' ,14,'bold'), textvariable=fruit_tart, bd=6,insertwidth=4 ,justify='right')
txtfruit_tart.grid(row=1,column=5)

lblpistaicecream = Label(f2a, font=( 'arial' ,16, 'bold' ),text="Pista Ice Cream ",bd=10,anchor='w')
lblpistaicecream.grid(row=2,column=4)
txtpistaicecream = Entry(f2a,font=('arial' ,14,'bold'), textvariable=pistaicecream, bd=6,insertwidth=4 ,justify='right')
txtpistaicecream.grid(row=2,column=5)

lblBeef_nihari = Label(f1a, font=( 'arial' ,16, 'bold' ),text=" Beef Nihari",bd=10,anchor='w')
lblBeef_nihari.grid(row=1,column=0)
txtBeef_nihari = Entry(f1a,font=('arial' ,14,'bold'), textvariable=Beef_nihari , bd=6,insertwidth=4 ,justify='right')
txtBeef_nihari.grid(row=1,column=1)


lblreference = Label(f1a, font=( 'arial' ,16, 'bold' ),text="Order No.",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1a,font=('arial' ,14,'bold'), textvariable=rand , bd=6,insertwidth=4, justify='right')
txtreference.grid(row=0,column=1)

lblchargha_biryani = Label(f1a, font=( 'arial' ,14, 'bold' ),text="Chargha Biryani",bd=10,anchor='w')
lblchargha_biryani.grid(row=2,column=0)
txtchargha_biryani = Entry(f1a,font=('arial' ,14,'bold'), textvariable=chargha_biryani , bd=6,insertwidth=4,justify='right')
txtchargha_biryani.grid(row=2,column=1)

lblmalai_kofta = Label(f1a, font=( 'arial' ,16, 'bold' ),text="Malai Kofta",bd=10,anchor='w')
lblmalai_kofta.grid(row=3,column=0)
txtmalai_kofta = Entry(f1a,font=('arial' ,14,'bold'), textvariable=malai_kofta , bd=6,insertwidth=4 ,justify='right')
txtmalai_kofta.grid(row=3,column=1)


lblchicken_karahi = Label(f1a, font=( 'arial' ,16, 'bold' ),text="Chicken Karahi",bd=10,anchor='w')
lblchicken_karahi.grid(row=4,column=0)
txtchicken_karahi = Entry(f1a,font=('arial' ,14,'bold'), textvariable=chicken_karahi , bd=6,insertwidth=4 ,justify='right')
txtchicken_karahi.grid(row=4,column=1)


lblchicken_chapli_kabbab = Label(f1a, font=( 'arial' ,11, 'bold' ),text="Chicken Chapli Kabbab",bd=10,anchor='w')
lblchicken_chapli_kabbab.grid(row=5,column=0)
txtchicken_chapli_kabbab = Entry(f1a,font=('arial' ,14,'bold'), textvariable=chicken_chapli_kabbab , bd=6,insertwidth=4 ,justify='right')
txtchicken_chapli_kabbab.grid(row=5,column=1)


lblcrump_chicken_burger = Label(f1a, font=( 'arial' ,12, 'bold' ),text="Crump Chicken Burger",bd=10,anchor='w')
lblcrump_chicken_burger.grid(row=6,column=0)
txtcrump_chicken_burger = Entry(f1a,font=('arial' ,14,'bold'), textvariable=crump_chicken_burger , bd=6,insertwidth=4 ,justify='right')
txtcrump_chicken_burger.grid(row=6,column=1)

#--------------------------------------------------------------------------------------
lblbeef_steak_sandwich = Label(f1a, font=( 'arial' ,11, 'bold' ),text="Beef Steak Sandwich",bd=10,anchor='w')
lblbeef_steak_sandwich.grid(row=0,column=2)
txtbeef_steak_sandwich = Entry(f1a,font=('arial' ,14,'bold'), textvariable=beef_steak_sandwich , bd=6,insertwidth=4,justify='right')
txtbeef_steak_sandwich.grid(row=0,column=3)

lblherbed_cheese_sticks = Label(f1a, font=( 'arial' ,11, 'bold' ),text="Herbed Cheese Sticks",bd=10,anchor='w')
lblherbed_cheese_sticks.grid(row=1,column=2)
txtherbed_cheese_sticks = Entry(f1a,font=('arial' ,14,'bold'), textvariable=herbed_cheese_sticks , bd=6,insertwidth=4 ,justify='right')
txtherbed_cheese_sticks.grid(row=1,column=3)


lblcrispy_fluffy_fish = Label(f1a, font=( 'arial' ,13, 'bold' ),text="Crispy Fluffy Fish",bd=10,anchor='w')
lblcrispy_fluffy_fish.grid(row=2,column=2)
txtcrispy_fluffy_fish = Entry(f1a,font=('arial' ,14,'bold'), textvariable=crispy_fluffy_fish , bd=6,insertwidth=4,justify='right')
txtcrispy_fluffy_fish.grid(row=2,column=3)


lblblack_pepper_prawns = Label(f1a, font=( 'arial' ,12, 'bold' ),text="Black Pepper Prawns",bd=10,anchor='w')
lblblack_pepper_prawns.grid(row=3,column=2)
txtblack_pepper_prawns = Entry(f1a,font=('arial' ,14,'bold'), textvariable=black_pepper_prawns , bd=6,insertwidth=4,justify='right')
txtblack_pepper_prawns.grid(row=3,column=3)

lblmix_berry_chiller = Label(f1a, font=( 'arial' ,14, 'bold' ),text="Mix Berry Chiller",bd=10,anchor='w')
lblmix_berry_chiller.grid(row=4,column=2)
txtmix_berry_chiller = Entry(f1a,font=('arial' ,14,'bold'), textvariable=mix_berry_chiller , bd=6,insertwidth=4,justify='right')
txtmix_berry_chiller.grid(row=4,column=3)

lblHerbal_tea = Label(f1a, font=( 'arial' ,14, 'bold' ),text="Herbal Tea",bd=10,anchor='w')
lblHerbal_tea.grid(row=5,column=2)
txtHerbal_tea = Entry(f1a,font=('arial' ,14,'bold'), textvariable=Herbal_tea , bd=6,insertwidth=4,justify='right')
txtHerbal_tea.grid(row=5,column=3)

lbllime_drink = Label(f1a, font=( 'arial' ,16, 'bold' ),text="Lime Drink",bd=10,anchor='w')
lbllime_drink.grid(row=6,column=2)
txtlime_drink = Entry(f1a,font=('arial' ,14,'bold'), textvariable=lime_drink , bd=6,insertwidth=4,justify='right')
txtlime_drink.grid(row=6,column=3)

lblcost = Label(f2b, font=( 'arial' ,16, 'bold' ),text="cost",bd=10,anchor='w')
lblcost.grid(row=2,column=4)
txtcost = Entry(f2b,font=('arial' ,14,'bold'), textvariable=cost , bd=6,insertwidth=4,justify='right')
txtcost.grid(row=2,column=5)

lblService_Charge = Label(f2b, font=( 'arial' ,16, 'bold' ),text="Service Charge",bd=10,anchor='w')
lblService_Charge.grid(row=3,column=4)
txtService_Charge = Entry(f2b,font=('arial' ,14,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,justify='right')
txtService_Charge.grid(row=3,column=5)

lblTax = Label(f2b, font=( 'arial' ,16, 'bold' ),text="Tax",bd=10,anchor='w')
lblTax.grid(row=4,column=4)
txtTax = Entry(f2b,font=('arial' ,14,'bold'), textvariable=Tax , bd=6,insertwidth=4,justify='right')
txtTax.grid(row=4,column=5)


lblSubtotal = Label(f2b, font=( 'arial' ,16, 'bold' ),text="Subtotal",bd=10,anchor='w')
lblSubtotal.grid(row=5,column=4)
txtSubtotal = Entry(f2b,font=('arial' ,14,'bold'), textvariable=Subtotal , bd=6,insertwidth=4 ,justify='right')
txtSubtotal.grid(row=5,column=5)

lblTotal = Label(f2b, font=( 'arial' ,16, 'bold' ),text="Total",bd=10,anchor='w')
lblTotal.grid(row=6,column=4)
txtTotal = Entry(f2b,font=('arial' ,14,'bold'), textvariable=Total , bd=6,insertwidth=4 ,justify='right')
txtTotal.grid(row=6,column=5)

#====================================== Buttons ==================================


btnTotal=Button(f1b,padx=4,pady=4, bd=10 ,fg="black",font=('arial' ,16,'bold'),width=10,height=1, text="TOTAL", bg="white",command=z.total)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1b,padx=4,pady=4, bd=10 ,fg="black",font=('arial' ,16,'bold'),width=10, text="RESET", bg="white",command=z.reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1b,padx=4,pady=4, bd=10 ,fg="black",font=('aral' ,16,'bold'),width=10, text="EXIT", bg="white",command=z.qexit)
btnexit.grid(row=7, column=3)

#=======================================  Price Class =============================
class PRICE(Main):
    @staticmethod
    def price():
        roo = Tk()
        roo.geometry("465x605+0+0")
        roo.title("Price List")
        roo.configure(bg='powder blue')
        Top = Frame(roo, width =470,height =590, bd=10,bg = 'white', relief = 'raise')
        Top.pack(side = TOP)

        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="ITEM", fg="black", bd=5)
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(Top, font=('arial', 15,'bold'), text="____________", fg="white", anchor=W)
        lblinfo.grid(row=0, column=2)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="PRICE", fg="black", anchor=W)
        lblinfo.grid(row=0, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Beef Nihari",  anchor=W)
        lblinfo.grid(row=1, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="25",  anchor=W)
        lblinfo.grid(row=1, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Chargha Biryani", anchor=W)
        lblinfo.grid(row=2, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="40", anchor=W)
        lblinfo.grid(row=2, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Malai Kofta",  anchor=W)
        lblinfo.grid(row=3, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="35", anchor=W)
        lblinfo.grid(row=3, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Chicken Karahi", anchor=W)
        lblinfo.grid(row=4, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="50",  anchor=W)
        lblinfo.grid(row=4, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Chicken Chapli Kabbab", anchor=W)
        lblinfo.grid(row=5, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="30",anchor=W)
        lblinfo.grid(row=5, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Crump Chicken Burger",  anchor=W)
        lblinfo.grid(row=6, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="35", anchor=W)
        lblinfo.grid(row=6, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Beef Steak Sandwich", anchor=W)
        lblinfo.grid(row=7, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="400",  anchor=W)
        lblinfo.grid(row=7, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Herbed Cheese Sticks",  anchor=W)
        lblinfo.grid(row=8, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="20",  anchor=W)
        lblinfo.grid(row=8, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Crispy Fluffy Fish",  anchor=W)
        lblinfo.grid(row=9, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="50",  anchor=W)
        lblinfo.grid(row=9, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Black Pepper prawns",  anchor=W)
        lblinfo.grid(row=10, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="500",  anchor=W)
        lblinfo.grid(row=10, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Mix Berry Chiller",  anchor=W)
        lblinfo.grid(row=11, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="90",  anchor=W)
        lblinfo.grid(row=11, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Herbal Tea",  anchor=W)
        lblinfo.grid(row=12, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="90",  anchor=W)
        lblinfo.grid(row=12, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Soft Drink with Lime",  anchor=W)
        lblinfo.grid(row=13, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="90",  anchor=W)
        lblinfo.grid(row=13, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Bread Pudding",  anchor=W)
        lblinfo.grid(row=14, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="90",  anchor=W)
        lblinfo.grid(row=14, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Fruit Tart",  anchor=W)
        lblinfo.grid(row=15, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="90",  anchor=W)
        lblinfo.grid(row=15, column=3)

        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Pista Ice Cream",  anchor=W)
        lblinfo.grid(row=16, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="90",  anchor=W)
        lblinfo.grid(row=16, column=3)
#==============================tax and service charges===============================================
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Tax",  anchor=W)
        lblinfo.grid(row=17, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="0.33", anchor=W)
        lblinfo.grid(row=17, column=3)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="Servive Charges", anchor=W)
        lblinfo.grid(row=18, column=0)
        lblinfo = Label(Top, font=('arial', 15, 'bold'), text="1/99",  anchor=W)
        lblinfo.grid(row=18, column=3)
        roo.mainloop()
x=PRICE()

btnprice=Button(f1b,padx=4,pady=4, bd=10 ,fg="black",font=('arial' ,16,'bold'),width=10, text="PRICE", bg="white",command=x.price)
btnprice.grid(row=7, column=0)

#======================================= Receipt Class ============================================

class RECEIPT(Main):
    @staticmethod
    def receipt():
        ro = Tk()
        ro.geometry("480x690+0+0")
        ro.title("Receipt")
        ro.configure(bg='powder blue')
        Topp = Frame(ro, width =470,height =490, bd=10,bg = 'white', relief = 'raise')
        Topp.pack(side = TOP)
        

        co_of_charghaBiryani =float(chargha_biryani.get())
        co_of_malai_kofta= float(malai_kofta.get())
        co_of_chicken_karahi= float(chicken_karahi.get())
        co_of_chicken_chapli_kabbab= float(chicken_chapli_kabbab.get())
        co_of_crump_chicken_burger= float(crump_chicken_burger.get())
        co_of_beef_steak_sandwich= float(beef_steak_sandwich.get())
        co_of_Beef_nihari= float(Beef_nihari.get())
        co_of_herbed_cheese_sticks= float(herbed_cheese_sticks.get())
        co_of_crispy_fluffyfish = float(crispy_fluffy_fish.get())
        co_of_blackpepper_prawns = float(black_pepper_prawns.get())
        co_of_mix_berryChiller=float(mix_berry_chiller.get())
        co_of_Herbal_tea = float(Herbal_tea.get())
        co_of_lime_drink = float(lime_drink.get())
        co_of_brePudding=float(bread_pudding.get())
        co_of_fruitTart=float(fruit_tart.get())
        CofPistaIceCream = float(pistaicecream.get())

        Co_of_CharghaBiryani = co_of_charghaBiryani*395
        Co_of_Malai_Kofta = co_of_malai_kofta * 200
        Co_of_ChickenKarahi = co_of_chicken_karahi *450
        Co_of_Chicken_chapliKabbab = co_of_chicken_chapli_kabbab * 50
        Co_of_Crump_chickenBurger = co_of_crump_chicken_burger*50
        Co_of_Beef_Steak_Sandwich = co_of_beef_steak_sandwich*35
        Co_of_BeefNihari = co_of_Beef_nihari*400
        Co_of_Herbed_CheeseSticks = co_of_herbed_cheese_sticks*20
        Co_of_Crispy_fluffyfish = co_of_crispy_fluffyfish * 900
        Co_of_Blackpepper_Prawns = co_of_blackpepper_prawns *750
        Co_of_Mix_BerryChiller = co_of_mix_berryChiller * 335
        Co_of_Herbaltea = co_of_Herbal_tea * 175
        Co_of_Lime_Drink = co_of_lime_drink * 300     
        Co_of_BrePudding =co_of_brePudding * 395
        Co_of_FruitTart= co_of_fruitTart * 300
        Co_of_PistaiceCream = CofPistaIceCream * 75

        PayTax=(Co_of_Herbed_CheeseSticks + Co_of_Beef_Steak_Sandwich + Co_of_Lime_Drink + Co_of_Crump_chickenBurger +Co_of_Chicken_chapliKabbab + Co_of_ChickenKarahi + Co_of_Malai_Kofta + Co_of_BeefNihari + Co_of_Mix_BerryChiller + Co_of_Crispy_fluffyfish + Co_of_Blackpepper_Prawns + Co_of_Herbaltea + Co_of_CharghaBiryani + Co_of_FruitTart + Co_of_PistaiceCream  +  Co_of_BrePudding)*0.33
        Totalcost=(Co_of_Herbed_CheeseSticks + Co_of_Beef_Steak_Sandwich + Co_of_Crump_chickenBurger +Co_of_Chicken_chapliKabbab + Co_of_Lime_Drink + Co_of_ChickenKarahi + Co_of_Malai_Kofta + Co_of_BeefNihari + Co_of_Mix_BerryChiller + Co_of_Crispy_fluffyfish + Co_of_Blackpepper_Prawns + Co_of_Herbaltea + Co_of_CharghaBiryani +  Co_of_FruitTart + Co_of_PistaiceCream +  Co_of_BrePudding)
        Ser_Charge=((Co_of_Herbed_CheeseSticks + Co_of_Beef_Steak_Sandwich + Co_of_Crump_chickenBurger +Co_of_Chicken_chapliKabbab + Co_of_Lime_Drink + Co_of_ChickenKarahi + Co_of_Malai_Kofta + Co_of_BeefNihari + Co_of_Mix_BerryChiller + Co_of_Crispy_fluffyfish + Co_of_Blackpepper_Prawns + Co_of_Herbaltea + Co_of_CharghaBiryani  + Co_of_FruitTart + Co_of_PistaiceCream  +  Co_of_BrePudding)/99)

        OverAllCost=float( PayTax + Totalcost + Ser_Charge)
    
        lblinfoo = Label(Topp, font=('arial', 15, 'bold'), text="ITEM", fg="black", bd=5)
        lblinfoo.grid(row=0, column=0)
        lblinfoo = Label(Topp, font=('arial', 15,'bold'), text="_________", fg="white", anchor=W)
        lblinfoo.grid(row=0, column=2)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Price", fg="black", anchor=W)
        lblinfo.grid(row=0, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Beef Nihari", anchor=W)
        lblinfo.grid(row=1, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_BeefNihari,  anchor=W)
        lblinfo.grid(row=1, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Chargha Biryani",  anchor=W)
        lblinfo.grid(row=2, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_CharghaBiryani, anchor=W)
        lblinfo.grid(row=2, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Malai Kofta",  anchor=W)
        lblinfo.grid(row=3, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text= Co_of_Malai_Kofta, anchor=W)
        lblinfo.grid(row=3, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Chicken Karahi",  anchor=W)
        lblinfo.grid(row=4, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_ChickenKarahi,  anchor=W)
        lblinfo.grid(row=4, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Chicken Chapli Kabbab",  anchor=W)
        lblinfo.grid(row=5, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_Chicken_chapliKabbab, anchor=W)
        lblinfo.grid(row=5, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Crump Chicken Burger",  anchor=W)
        lblinfo.grid(row=6, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_Crump_chickenBurger, anchor=W)
        lblinfo.grid(row=6, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Beef Steak Sandwich",  anchor=W)
        lblinfo.grid(row=7, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_Beef_Steak_Sandwich, anchor=W)
        lblinfo.grid(row=7, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Herbed Cheese Sticks", anchor=W)
        lblinfo.grid(row=8, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_Herbed_CheeseSticks, anchor=W)
        lblinfo.grid(row=8, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Crispy Fluffy Fish", anchor=W)
        lblinfo.grid(row=9, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_Crispy_fluffyfish, anchor=W)
        lblinfo.grid(row=9, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Black Pepper Prawns ",  anchor=W)
        lblinfo.grid(row=10, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_Blackpepper_Prawns , anchor=W)
        lblinfo.grid(row=10, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Mix Berry Chiller",  anchor=W)
        lblinfo.grid(row=11, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_Mix_BerryChiller,  anchor=W)
        lblinfo.grid(row=11, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Herbal Tea", anchor=W)
        lblinfo.grid(row=12, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_Herbaltea,  anchor=W)
        lblinfo.grid(row=12, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Lime Drink",  anchor=W)
        lblinfo.grid(row=13, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_Lime_Drink,  anchor=W)
        lblinfo.grid(row=13, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Herbal Tea", anchor=W)
        lblinfo.grid(row=14, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_Herbaltea,  anchor=W)
        lblinfo.grid(row=14, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Bread Pudding",  anchor=W)
        lblinfo.grid(row=15, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_BrePudding,  anchor=W)
        lblinfo.grid(row=15, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Fruit Tart",  anchor=W)
        lblinfo.grid(row=16, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_FruitTart, anchor=W)
        lblinfo.grid(row=16, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Pista icecream", anchor=W)
        lblinfo.grid(row=17, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Co_of_PistaiceCream, anchor=W)
        lblinfo.grid(row=17, column=3)
    #==============================tax and service charges===============================================
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Cost",  anchor=W)
        lblinfo.grid(row=18, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Totalcost,  anchor=W)
        lblinfo.grid(row=18, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Pay Tax",  anchor=W)
        lblinfo.grid(row=19, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=PayTax,  anchor=W)
        lblinfo.grid(row=19, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Service Charge",  anchor=W)
        lblinfo.grid(row=20, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=Ser_Charge, anchor=W)
        lblinfo.grid(row=20, column=3)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text="Total Cost", anchor=W)
        lblinfo.grid(row=21, column=0)
        lblinfo = Label(Topp, font=('arial', 15, 'bold'), text=OverAllCost, anchor=W)
        lblinfo.grid(row=21, column=3)



        ro.mainloop()
y=RECEIPT()
btnreceipt=Button(f1b,padx=4,pady=4, bd=10 ,fg="black",font=('arial' ,16,'bold'),width=10, text="RECEIPT", bg="white",command=y.receipt)
btnreceipt.grid(row=7, column=4)


y.func()

root.mainloop()