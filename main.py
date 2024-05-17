from tkinter import *
from tkinter import messagebox
import random, os, tempfile,smtplib

# function defination
# checking whether folder exist or not
if not os.path.exists('holiday_projects/billing'):
    os.mkdir('holiday_projects/billing')


def savebill():
    global billnumber
    result = messagebox.askyesno('confirm', 'are you sure you want to save  the bill \n')
    if result:
        bill_content = textArea.get(1.0, END)
        file = open(f'holiday_projects/billing/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('successful', f'bill saved successfully{billnumber}')
        billnumber = random.randint(500, 1000)
    pass


def total():
    # making variable global
    global hairGeillprice, soapValue, faceCreamprice, faceWashprice, faceDetergentprice, faceTowingprice, hairSprayprice, bodyLotionprice
    global totalbill

    # for cosmetics
    soapValue = int(bathSoapEntry.get()) * 30
    faceCreamprice = int(faceCreamEntry.get()) * 40
    faceWashprice = int(faceWashEntry.get()) * 50
    faceDetergentprice = int(faceDetergentEntry.get()) * 20
    faceTowingprice = int(faceToweringEntry.get()) * 70
    hairSprayprice = int(hairSprayEntry.get()) * 60
    hairGeillprice = int(hairGeillEntry.get()) * 55
    bodyLotionprice = int(bodyLotionEntry.get()) * 90

    totalCosmeticprice = soapValue + faceCreamprice + faceWashprice + faceDetergentprice + faceTowingprice + hairSprayprice + bodyLotionprice
    cosmeticPriceEntry.delete(0, END)
    # for inserting totalcosmeticprice into cosmetic field use .insert method

    cosmeticPriceEntry.insert(0, str(totalCosmeticprice) + 'rs')
    cosmetictax = totalCosmeticprice * 0.02
    cosmeticTaxEntry.delete(0, END)
    cosmeticTaxEntry.insert(0, str(cosmetictax) + 'rs')

    # for  grocery
    global riceprice, oilprice, floorprice, sugarprice, breadprice, bisqprice, milkprice, cakeprice
    riceprice = int(riceEntry.get()) * 120
    oilprice = int(oilEntry.get()) * 100
    floorprice = int(floorEntry.get()) * 70
    sugarprice = int(sugarEntry.get()) * 140
    breadprice = int(breadEntry.get()) * 60
    bisqprice = int(bisquitEntry.get()) * 20
    milkprice = int(milkEntry.get()) * 50
    cakeprice = int(cakeEntry.get()) * 30
    totalGroceryprice = riceprice + oilprice + floorprice + sugarprice + breadprice + bisqprice + milkprice + cakeprice
    # for deleting items  if previously inserted
    groceryPriceEntry.delete(0, END)
    groceryPriceEntry.insert(0, str(totalGroceryprice) + 'rs')
    grocerytax = totalGroceryprice * 0.03
    groceryTaxEntry.delete(0, END)
    groceryTaxEntry.insert(0, str(grocerytax) + 'rs')

    # for drinks
    global fantaprice, krestprice, cokeprice, spiritprice, spriteprice, kaneprice, bullsprice, stoneyprice
    fantaprice = int(fantaEntry.get()) * 30
    krestprice = int(krestEntry.get()) * 40
    cokeprice = int(cocaColaEntry.get()) * 30
    spiritprice = int(spiritEntry.get()) * 70
    spriteprice = int(spriteEntry.get()) * 20
    kaneprice = int(kaneEntry.get()) * 70
    bullsprice = int(bullsEntry.get()) * 60
    stoneyprice = int(stoneyEntry.get()) * 40
    totalDrinksprice = fantaprice + kaneprice + krestprice + cokeprice + spiritprice + spriteprice + bullsprice + stoneyprice
    drinksPriceEntry.delete(0, END)
    drinksPriceEntry.insert(0, str(totalDrinksprice) + 'rs')
    drinkstax = totalDrinksprice * 0.19
    drinksTaxEntry.delete(0, END)
    drinksTaxEntry.insert(0, str(drinkstax) + 'rs')

    totalbill = totalDrinksprice + totalCosmeticprice + totalGroceryprice + cosmetictax + grocerytax + drinkstax
    textArea.insert(END, '\n ******************************************************')

    pass


def emails():
    def send_gmail():
        try:
            # code for sending gmail
            nam=smtplib.SMTP('smtp.gmail.com',587)
            nam.starttls() # establishing secure connection
            nam.login(senderEntry.get(),passwordEntry.get())
            # getting message
            message=emailmessagetext.get(1.0,END)
            # reciever address
            reciever_address=recieverEntry.get()
            # sending mail using sendmail()
            nam.sendmail(senderEntry.get(),reciever_address,message)
            nam.quit()
            messagebox.showinfo('sent mail','bill sent successfully',parent=wn)
            wn.destroy() # closes the top level  window

        except:
            messagebox.showerror('error','something happened  while sending the bill\n '
                                         'PLEASE TRY AGAIN ',parent=wn)

        pass
    #  first checks whether text area is empty or not
    if textArea.get(1.0, END) == '\n':
        messagebox.showerror('error', 'empty bill \n enter valid bill   ')

    else:
        wn = Toplevel()
        wn.title('email  confimation window ')
        wn.resizable(False, False)
        wn.grab_set() # for diasbling other window while this is active
        wn.config(bg='brown')
        senderFrame = LabelFrame(wn, text='sender ', font=('arial', 16, 'bold'), bd=7,
                                 fg='white', bg='blue')
        senderFrame.grid(row=0, column=0, padx=40, pady=20)
        senderlabel = Label(senderFrame, text="sender's email", font=('arial', 14, 'bold'), bd=6,
                            fg='white', bg='blue')
        senderlabel.grid(row=0, column=0, padx=11, pady=10)
        senderEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=3, width=30, relief=GROOVE)
        senderEntry.grid(row=0, column=1, padx=11, pady=10)
        # for sender password
        passwordlabel = Label(senderFrame, text='password ', font=('arial', 14, 'bold'), bd=6,
                              fg='white', bg='blue')
        passwordlabel.grid(row=1, column=0, padx=11, pady=10)
        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=3, width=30, relief=RIDGE,show='*')
        passwordEntry.grid(row=1, column=1, padx=11, pady=10)
        # reciepient frame
        reciepientFrame = LabelFrame(wn, text='RECIEVER ', font=('arial', 16, 'bold'), bd=7,
                                     fg='white', bg='blue')
        reciepientFrame.grid(row=1, column=0, padx=40, pady=20)
        # recievers email
        recieverlabel = Label(reciepientFrame, text="reciever's email", font=('arial', 14, 'bold'), bd=6,
                              fg='white', bg='blue')
        recieverlabel.grid(row=0, column=0, padx=11, pady=10)
        recieverEntry = Entry(reciepientFrame, font=('arial', 14, 'bold'), bd=3, width=30, relief=GROOVE)
        recieverEntry.grid(row=0, column=1, padx=11, pady=10)
        # message
        messagelabel = Label(reciepientFrame, text=' reciever password ', font=('arial', 14, 'bold'), bd=6,
                             fg='white', bg='blue')
        messagelabel.grid(row=1, column=0, padx=7, pady=5)
        emailmessagetext = Text(reciepientFrame, font=('arial', 14, 'bold'), bd=3, width=60, relief=SUNKEN, height=15)
        emailmessagetext.grid(row=2, column=0, columnspan=2)
        emailmessagetext.delete(1.0, END)
        emailmessagetext.insert(END, textArea.get(1.0, END).replace('*','').replace('\t \t','\t \t'))  # getting contents of text area   i created before

        # button creation  for sending
        sendButton = Button(wn, text='send', font=('arial', 15, 'bold'), width=18,command=send_gmail)
        sendButton.grid(row=2, column=0, pady=10)

        wn.mainloop()

    pass


def clear():
    bathSoapEntry.delete(0,END)
    bathSoapEntry.insert(0,0)
    fantaEntry.delete(0,END)
    fantaEntry.insert(0,0)
    faceToweringEntry.delete(0,END)
    faceToweringEntry.insert(0,0)
    floorEntry.delete(0,END)
    floorEntry.insert(0,0)
    breadEntry.delete(0,END)
    breadEntry.insert(0,0)
    entryBills.delete(0,END)
    entryBills.insert(0,0)
    bisquitEntry.delete(0,END)
    bisquitEntry.insert(0,0)
    hairGeillEntry.delete(0,END)
    hairGeillEntry.insert(0,0)
    hairSprayEntry.delete(0,END)
    hairSprayEntry.insert(0,0)
    faceWashEntry.delete(0,END)
    faceWashEntry.insert(0,0)
    faceDetergentEntry.delete(0,END)
    faceDetergentEntry.insert(0,0)
    spiritEntry.delete(0,END)
    spiritEntry.insert(0,0)
    spriteEntry.delete(0,END)
    spriteEntry.insert(0,0)
    kaneEntry.delete(0,END)
    kaneEntry.insert(0,0)
    krestEntry.delete(0,END)
    krestEntry.insert(0,0)
    bullsEntry.delete(0,END)
    bullsEntry.insert(0,0)
    riceEntry.delete(0,END)
    riceEntry.insert(0,0)
    oilEntry.delete(0,END)
    oilEntry.insert(0,0)
    cakeEntry.delete(0,END)
    cakeEntry.insert(0,0)
    sugarEntry.delete(0,END)
    sugarEntry.insert(0,0)
    cocaColaEntry.delete(0,END)
    cocaColaEntry.insert(0,0)

    cosmeticTaxEntry.delete(0,END)
    groceryTaxEntry.delete(0,END)
    drinksTaxEntry.delete(0,END)
    cosmeticPriceEntry.delete(0,END)
    groceryPriceEntry.delete(0,END)
    drinksPriceEntry.delete(0,END)
    # clearing name ,contact and bill number field

    entryName.delete(0,END)
    entryContact.delete(0,END)
    entryBills.delete(0,END)
    # clearing everything from bill area
    textArea.delete(1.0,END)
    pass


billnumber = random.randint(500, 1000)


def bill():
    textArea.delete(1.0, END)
    if entryName.get() == '' or entryContact.get() == '':
        messagebox.showerror('null error ', 'oops  either of the  field  is empty ,please enter null fields ')


    elif cosmeticPriceEntry.get() == '' and groceryPriceEntry.get() == '' and drinksPriceEntry.get() == '':
        messagebox.showerror('no product error', 'none of the products are selected '
                                                 ' \n please selct atleast one ')

    elif cosmeticPriceEntry.get() == '0 rs' and groceryPriceEntry.get() == '0 rs' and drinksPriceEntry.get() == '0 rs':
        messagebox.showerror('try error', ' null selection')

    else:
        textArea.insert(END, f'\t \t \t welcome {entryName.get()} to Alexia digital ')
        textArea.insert(END, f'\n bill number \t {billnumber} \n')
        textArea.insert(END, f'\n customer name {entryName.get()} \n ')
        textArea.insert(END, f'\n phone number \t {entryContact.get()} \n')
        textArea.insert(END, '\n ******************************************************')
        textArea.insert(END, f'\n  products \t\t quantity \t\t price ')
        textArea.insert(END, '\n ******************************************************')
        # detergents display
        if bathSoapEntry.get() != '0':
            textArea.insert(END, f'bath soap \t \t {bathSoapEntry.get()} \t \t {soapValue} \n ')
        pass
        if hairSprayEntry.get() != '0':
            textArea.insert(END, f'hairSpray \t \t {hairSprayEntry.get()} \t \t {hairSprayprice} \n')

        if faceCreamEntry.get() != '0':
            textArea.insert(END, f'face cream \t \t {faceCreamEntry.get()} \t \t {faceCreamprice} \n')
        pass
        if hairGeillEntry.get() != '0':
            textArea.insert(END, f'hair gel \t \t {hairGeillEntry.get()} \t \t {hairGeillprice} \n')
        pass
        if faceDetergentEntry.get() != '0':
            textArea.insert(END, f'face detergents \t \t {faceDetergentEntry.get()} \t \t {faceDetergentprice} \n')
        pass
        if faceToweringEntry.get() != '0':
            textArea.insert(END, f'face towering  \t \t {faceToweringEntry.get()} \t \t {faceTowingprice} \n')
        pass
        if bodyLotionEntry.get() != '0':
            textArea.insert(END, f'body lotion  \t \t {bodyLotionEntry.get()} \t \t {bodyLotionprice} \n')
        pass
        if faceWashEntry.get() != '0':
            textArea.insert(END, f'face wash \t \t {faceWashEntry.get()} \t \t {faceWashprice} \n')

        # end of detergents
        # grocery

        if riceEntry.get() != '0':
            textArea.insert(END, f'rice  \t \t {riceEntry.get()} \t \t {riceprice} \n')
        if oilEntry.get() != '0':
            textArea.insert(END, f'oil \t \t {oilEntry.get()} \t \t {oilprice} \n')
        if floorEntry.get() != '0':
            textArea.insert(END, f'floor  \t \t {floorEntry.get()} \t \t {floorprice} \n')

        if sugarEntry.get() != '0':
            textArea.insert(END, f'sugar \t \t {sugarEntry.get()} \t \t {sugarprice} \n')
        if breadEntry.get() != '0':
            textArea.insert(END, f'bread \t \t {breadEntry.get()} \t \t {breadprice} \n')
        pass
        if bisquitEntry.get() != '0':
            textArea.insert(END, f'biscuits \t \t {bisquitEntry.get()} \t \t {bisqprice} \n')
        if milkEntry.get() != '0':
            textArea.insert(END, f'milk \t \t {milkEntry.get()} \t \t {milkprice} \n')
        if cakeEntry.get() != '0':
            textArea.insert(END, f'cake  \t \t {cakeEntry.get()} \t \t {cakeprice} \n')

        # end of grocery
        # for drinks

        if fantaEntry.get() != '0':
            textArea.insert(END, f' fantas \t \t {fantaEntry.get()} \t \t {fantaprice} \n')
        if krestEntry.get() != '0':
            textArea.insert(END, f'krest \t \t {krestEntry.get()} \t \t {krestprice} \n')
        if cocaColaEntry.get() != '0':
            textArea.insert(END, f'coke \t \t {cocaColaEntry.get()} \t \t {cokeprice} \n')
        if spiritEntry.get() != '0':
            textArea.insert(END, f'spirit \t \t {spiritEntry.get()} \t \t {spiritprice} \n')

        if spriteEntry.get() != '0':
            textArea.insert(END, f'sprite \t \t {spriteEntry.get()} \t \t {spiritprice} \n')
        if kaneEntry.get() != '0':
            textArea.insert(END, f'kane \t \t {kaneEntry.get()} \t \t {kaneprice} \n')
        if stoneyEntry.get() != '0':
            textArea.insert(END, f'stoney \t \t {stoneyEntry.get()} \t \t {stoneyprice} \n')
        if bullsEntry.get() != '0':
            textArea.insert(END, f'bulls wine \t \t {bullsEntry.get()} \t \t {bullsprice} \n')
        # end drinks
        textArea.insert(END, '\n ******************************************************')
        # checking condition if there no entry ,tax should not display
        if cosmeticTaxEntry.get() != '0.0 rs':
            textArea.insert(END, f'\n cosmetic tax \t \t {cosmeticTaxEntry.get()}')
        if groceryTaxEntry.get() != '0.0 rs':
            textArea.insert(END, f'\n grocery tax \t \t {groceryTaxEntry.get()}')
        if drinksTaxEntry.get() != '0.0 rs':
            textArea.insert(END, f'\n drinks tax \t \t {drinksTaxEntry.get()}')

        textArea.insert(END, f'\n total bill \t \t {totalbill}')
        savebill()

    pass


def search():
    for i in os.listdir('holiday_projects/billing/'):
        if i.split('.')[0] == entryBills.get():
            myfile = open(f'holiday_projects/billing/{i}', 'r')
            textArea.delete(1.0, END)
            for data in myfile:
                textArea.insert(END, data)
            myfile.close()
            break  # exits  from the above for loop
    else:
        messagebox.showerror('invalid billnumber', 'you have entered invalid '
                                                   'bill number')


def prints():
    # check whether text area is empty or not
    if textArea.get(1.0, END) == '\n':
        messagebox.showerror('error', 'empty bill\n printing invalid  ')

    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textArea.get(1.0, END))
        os.startfile(file, 'prints')  # prints using the printer


#  end  of functions
# creating object of tkinter
root = Tk()

root.title('ALEXia BILLING SYSTEM')  # adding title
root.iconbitmap('icon.ico')  # setting icon

root.geometry('5000x3000+0+0')  # changing dimension of screen
headingLabel = Label(root, text="Alexia billing management system", font=('times new roman', 30, 'bold'),
                     bg='blue', fg='yellow', bd=12, relief=GROOVE)
# creating an instance of widget
headingLabel.pack(fill=X)

# creating customer filling details
customer_details = LabelFrame(root, text="customer details ", font=('times new roman', 13, 'bold'),
                              fg='green', bd=8, relief=GROOVE, bg='gold')

customer_details.pack(fill=X)
name = Label(customer_details, text="Name", font=('times new roman', 13, 'bold'), bg='gold',
             fg='blue')
# if you want to add items on a frame nad be visible use .grid() method  instead of pack

name.grid(row=0, column=0, padx=20, pady=2)
entryName = Entry(customer_details, font=('arial', 13, 'bold'), bd=8,
                  width=20)
entryName.grid(row=0, column=1, padx=7)
# for contact
phone = Label(customer_details, text="phoneNumber", font=('times new roman', 14, 'bold'), bg='gold',
              fg='blue')
phone.grid(row=0, column=2, padx=20, pady=2)
entryContact = Entry(customer_details, font=('arial', 14, 'bold'), bd=8,
                     width=20)

entryContact.grid(row=0, column=3, padx=7)
# for billing number
billsNumber = Label(customer_details, text="billing number", font=('times new roman', 14, 'bold'), bg='gold',
                    fg='blue')
billsNumber.grid(row=0, column=4, padx=20, pady=2)
entryBills = Entry(customer_details, font=('arial', 14, 'bold'), bd=8,
                   width=20)
billsNumber = billnumber
entryBills.grid(row=0, column=5, padx=7)

# search button
searchBtn = Button(customer_details, text="search", font=('arial', 12, 'bold'), bd=7, command=search)
searchBtn.grid(row=0, column=6, padx=20, pady=6)
#  crating product frame
productFrame = Frame(root)
productFrame.pack()
# items frame ie cosmetic frame

cosmeticFrame = LabelFrame(productFrame, text='all cosmetics ', font=('arial', 13, 'bold'),
                           fg='gold', bd=8, relief=GROOVE, bg='green')
cosmeticFrame.grid(row=0, column=0, sticky='w')
# creating labels
bathSoapLabel = Label(cosmeticFrame, text='soaps', font=('times new roman', 13, 'bold',
                                                         ), bg='green', fg='white')
bathSoapLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')
bathSoapEntry = Entry(cosmeticFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
bathSoapEntry.insert(0, 0)
bathSoapEntry.grid(row=0, column=1, pady=8, padx=9, sticky='w')
# face cream  item

faceCreamLabel = Label(cosmeticFrame, text='face cream', font=('times new roman', 13, 'bold',
                                                               ), bg='green', fg='white')
faceCreamLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')
faceCreamEntry = Entry(cosmeticFrame, font=('times new roman ', 15, 'bold'), width=10, bd=5)
faceCreamEntry.insert(0, 0)
faceCreamEntry.grid(row=1, column=1, pady=8, padx=10, sticky='w')

# face wash item
faceWashLabel = Label(cosmeticFrame, text='face wash', font=('times new roman', 13, 'bold',
                                                             ), bg='green', fg='white')
faceWashLabel.grid(row=2, column=0, pady=6, padx=10)
faceWashEntry = Entry(cosmeticFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
faceWashEntry.insert(0, 0)
faceWashEntry.grid(row=2, column=1, pady=8, padx=10, sticky='w')
# let me add others
# sticky is used in aligning items from end
faceDetergentLabel = Label(cosmeticFrame, text='Detergents', font=('times new roman', 13, 'bold',
                                                                   ), bg='green', fg='white')
faceDetergentLabel.grid(row=3, column=0, pady=6, padx=10, sticky='w')
faceDetergentEntry = Entry(cosmeticFrame, font=('times new roman ', 15, 'bold'), width=10, bd=5)
faceDetergentEntry.insert(0, 0)
faceDetergentEntry.grid(row=3, column=1, pady=8, padx=10, sticky='w')
# towering items
faceToweringLabel = Label(cosmeticFrame, text='Towels ', font=('times new roman', 13, 'bold',
                                                               ), bg='green', fg='white')
faceToweringLabel.grid(row=4, column=0, pady=6, padx=10, sticky='w')
faceToweringEntry = Entry(cosmeticFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
faceToweringEntry.insert(0, 0)
faceToweringEntry.grid(row=4, column=1, pady=8, padx=10, sticky='w')

# hair spray
hairSprayLabel = Label(cosmeticFrame, text='hair sprays', font=('times new roman', 13, 'bold',
                                                                ), bg='green', fg='white')
hairSprayLabel.grid(row=5, column=0, pady=6, padx=10, sticky='w')
hairSprayEntry = Entry(cosmeticFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
hairSprayEntry.insert(0, 0)
hairSprayEntry.grid(row=5, column=1, pady=8, padx=10, sticky='w')

# hair gells
hairGeillLabel = Label(cosmeticFrame, text='hair Gells ', font=('times new roman', 13, 'bold',
                                                                ), bg='green', fg='white')
hairGeillLabel.grid(row=6, column=0, pady=6, padx=10)
hairGeillEntry = Entry(cosmeticFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
hairGeillEntry.insert(0, 0)
hairGeillEntry.grid(row=6, column=1, pady=8, padx=10, sticky='w')

# for body lotion
bodyLotionLabel = Label(cosmeticFrame, text='Body lotion ', font=('times new roman', 13, 'bold',
                                                                  ), bg='green', fg='white')
bodyLotionLabel.grid(row=7, column=0, pady=6, padx=10, sticky='w')
bodyLotionEntry = Entry(cosmeticFrame, font=('times new roman ', 15, 'bold'), width=10, bd=5)
bodyLotionEntry.insert(0, 0)
bodyLotionEntry.grid(row=7, column=1, pady=8, padx=10, sticky='w')

# creating grocery  frame
groceryFrame = LabelFrame(productFrame, text='all Groceries  ', font=('arial', 13, 'bold'),
                          fg='gold', bd=8, relief=GROOVE, bg='green')
groceryFrame.grid(row=0, column=1, sticky='w')

# creating labels for grocery

riceLabel = Label(groceryFrame, text='Rice ', font=('times new roman', 13, 'bold',
                                                    ), bg='green', fg='white')
riceLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')
riceEntry = Entry(groceryFrame, font=('times new roman ', 15, 'bold'), width=10, bd=5)
riceEntry.insert(0, 0)
riceEntry.grid(row=0, column=1, pady=8, padx=10, sticky='w')

# oil label

oilLabel = Label(groceryFrame, text='  Oil ', font=('times new roman', 13, 'bold',
                                                    ), bg='green', fg='white')
oilLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')
oilEntry = Entry(groceryFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
oilEntry.insert(0, 0)
oilEntry.grid(row=1, column=1, pady=8, padx=10, sticky='w')

# floor

floorLabel = Label(groceryFrame, text='Floor ', font=('times new roman', 13, 'bold',
                                                      ), bg='green', fg='white')
floorLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')
floorEntry = Entry(groceryFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
floorEntry.insert(0, 0)
floorEntry.grid(row=2, column=1, pady=8, padx=10, sticky='w')

# sugar

sugarLabel = Label(groceryFrame, text=' sugar ', font=('times new roman', 13, 'bold',
                                                       ), bg='green', fg='white')
sugarLabel.grid(row=3, column=0, pady=6, padx=10, sticky='w')
sugarEntry = Entry(groceryFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
sugarEntry.insert(0, 0)
sugarEntry.grid(row=3, column=1, pady=8, padx=10, sticky='w')

# bread

breadLabel = Label(groceryFrame, text='bread ', font=('times new roman', 13, 'bold',
                                                      ), bg='green', fg='white')
breadLabel.grid(row=4, column=0, pady=6, padx=10, sticky='w')
breadEntry = Entry(groceryFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
breadEntry.insert(0, 0)
breadEntry.grid(row=4, column=1, pady=8, padx=10, sticky='w')
# others
# biscuit

bisquitLabel = Label(groceryFrame, text='biscuits ', font=('times new roman', 13, 'bold',
                                                           ), bg='green', fg='white')
bisquitLabel.grid(row=5, column=0, pady=6, padx=10, sticky='w')
bisquitEntry = Entry(groceryFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
bisquitEntry.insert(0, 0)
bisquitEntry.grid(row=5, column=1, pady=8, padx=10, sticky='w')
# milk


milkLabel = Label(groceryFrame, text='milk ', font=('times new roman', 13, 'bold',
                                                    ), bg='green', fg='white')
milkLabel.grid(row=6, column=0, pady=6, padx=10, sticky='w')
milkEntry = Entry(groceryFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
milkEntry.insert(0, 0)
milkEntry.grid(row=6, column=1, pady=8, padx=10, sticky='w')

# cakes

cakeLabel = Label(groceryFrame, text=' cakes', font=('times new roman', 13, 'bold',
                                                     ), bg='green', fg='white')
cakeLabel.grid(row=7, column=0, pady=6, padx=10, sticky='w')
cakeEntry = Entry(groceryFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
cakeEntry.insert(0, 0)
cakeEntry.grid(row=7, column=1, pady=8, padx=10, sticky='w')

# creating  drinks frame
# this is where the drinks will be displayed

drinksFrame = LabelFrame(productFrame, text='drinks available  ', font=('arial', 13, 'bold'),
                         fg='gold', bd=8, relief=GROOVE, bg='green')
drinksFrame.grid(row=0, column=2, sticky='w')

# adding labels to drinks frame
# fanta

fantaLabel = Label(drinksFrame, text=' fanta', font=('times new roman', 13, 'bold',
                                                     ), bg='green', fg='white')
fantaLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')
fantaEntry = Entry(drinksFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
fantaEntry.insert(0, 0)
fantaEntry.grid(row=0, column=1, pady=8, padx=10, sticky='w')

# sprite
spriteLabel = Label(drinksFrame, text=' sprite', font=('times new roman', 13, 'bold',
                                                       ), bg='green', fg='white')
spriteLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')
spriteEntry = Entry(drinksFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
spriteEntry.insert(0, 0)
spriteEntry.grid(row=1, column=1, pady=8, padx=10, sticky='w')

# coca cola
cocaColaLabel = Label(drinksFrame, text=' coca cola', font=('times new roman', 13, 'bold',
                                                            ), bg='green', fg='white')
cocaColaLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')
cocaColaEntry = Entry(drinksFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
cocaColaEntry.insert(0, 0)
cocaColaEntry.grid(row=2, column=1, pady=8, padx=10, sticky='w')
# stoney
stoneyLabel = Label(drinksFrame, text=' stoney', font=('times new roman', 13, 'bold',
                                                       ), bg='green', fg='white')
stoneyLabel.grid(row=3, column=0, pady=6, padx=10, sticky='w')
stoneyEntry = Entry(drinksFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
stoneyEntry.insert(0, 0)
stoneyEntry.grid(row=3, column=1, pady=8, padx=10, sticky='w')
# krest
krestLabel = Label(drinksFrame, text=' krest', font=('times new roman', 13, 'bold',
                                                     ), bg='green', fg='white')
krestLabel.grid(row=4, column=0, pady=6, padx=10, sticky='w')
krestEntry = Entry(drinksFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
krestEntry.insert(0, 0)
krestEntry.grid(row=4, column=1, pady=8, padx=10, sticky='w')

# bulls
bullsLabel = Label(drinksFrame, text=' bulls', font=('times new roman', 13, 'bold',
                                                     ), bg='green', fg='white')
bullsLabel.grid(row=5, column=0, pady=6, padx=10, sticky='w')
bullsEntry = Entry(drinksFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
bullsEntry.insert(0, 0)
bullsEntry.grid(row=5, column=1, pady=8, padx=10, sticky='w')

# kane
kaneLabel = Label(drinksFrame, text=' Kane', font=('times new roman', 13, 'bold',
                                                   ), bg='green', fg='white')
kaneLabel.grid(row=6, column=0, pady=6, padx=10, sticky='w')
kaneEntry = Entry(drinksFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
kaneEntry.insert(0, 0)
kaneEntry.grid(row=6, column=1, pady=8, padx=10, sticky='w')

# spirit
spiritLabel = Label(drinksFrame, text=' spirit', font=('times new roman', 13, 'bold',
                                                       ), bg='green', fg='white')
spiritLabel.grid(row=7, column=0, pady=6, padx=10, sticky='w')
spiritEntry = Entry(drinksFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
spiritEntry.insert(0, 0)
spiritEntry.grid(row=7, column=1, pady=8, padx=10, sticky='w')

# creating billing area

# billing frame
billFrame = Frame(productFrame, bd=9, relief=GROOVE)
billFrame.grid(row=0, column=3, padx=10)

# creating labels for bill frame
billAreaLabel = Label(billFrame, text='bill area ', font=('times new roman', 13, 'bold'),
                      bd=8, relief=GROOVE)
billAreaLabel.pack(fill=X)
# for creating text-area ,there is a class called Text ()
scrollbar = Scrollbar(billFrame, orient=VERTICAL)  # creats a scroll bar
scrollbar.pack(side=RIGHT, fill=Y)  # positions the scrollbar at the right side of bill frame
# to connect scrollbar use commandingly and set method in the text area

textArea = Text(billFrame, width=55, height=20, yscrollcommand=scrollbar.set)

textArea.pack()
scrollbar.config(command=textArea.yview)  # used  when you want to see text when you scroll

# creating a  bill menu frame
billMenuFrame = LabelFrame(root, text='bill menu ', font=('arial', 13, 'bold'),
                           fg='gold', bd=8, relief=GROOVE, bg='grey')
billMenuFrame.pack()

# adding labels to billframe

# cosmetic price

cosmeticPriceLabel = Label(billMenuFrame, text=' cosmetic price', font=('times new roman', 13, 'bold',
                                                                        ), bg='green', fg='white')
cosmeticPriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')
cosmeticPriceEntry = Entry(billMenuFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
cosmeticPriceEntry.grid(row=0, column=1, padx=10, pady=6, sticky='w')

# grocery price

groceryPriceLabel = Label(billMenuFrame, text=' Grocery price ', font=('times new roman', 13, 'bold',
                                                                       ), bg='green', fg='white')
groceryPriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')
groceryPriceEntry = Entry(billMenuFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
groceryPriceEntry.grid(row=1, column=1, padx=10, pady=6, sticky='w')

# drinks price
drinksPriceLabel = Label(billMenuFrame, text=' Drinks  price  ', font=('times new roman', 13, 'bold',
                                                                       ), bg='green', fg='white')
drinksPriceLabel.grid(row=0, column=5, pady=6, padx=10, sticky='w')
drinksPriceEntry = Entry(billMenuFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
drinksPriceEntry.grid(row=1, column=5, padx=10, pady=6, sticky='w')

# adding taxes
# cosmetic Tax

cosmeticTaxLabel = Label(billMenuFrame, text='Cosmetis  tax', font=('times new roman', 13, 'bold',
                                                                    ), bg='green', fg='white')
cosmeticTaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky='w')
cosmeticTaxEntry = Entry(billMenuFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
cosmeticTaxEntry.grid(row=0, column=3, padx=10, pady=6, sticky='w')

# grocery tax

groceryTaxLabel = Label(billMenuFrame, text=' Grocery Tax ', font=('times new roman', 13, 'bold',
                                                                   ), bg='green', fg='white')
groceryTaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky='w')
groceryTaxEntry = Entry(billMenuFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
groceryTaxEntry.grid(row=1, column=3, padx=10, pady=6, sticky='w')

# drinks tax
drinksTaxLabel = Label(billMenuFrame, text=' Drinks  Tax  ', font=('times new roman', 13, 'bold',
                                                                   ), bg='green', fg='white')
drinksTaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky='w')
drinksTaxEntry = Entry(billMenuFrame, font=('times new roman ', 13, 'bold'), width=10, bd=5)
drinksTaxEntry.grid(row=2, column=3, padx=10, pady=6, sticky='w')

# creating button frame
buttonFrame = Frame(billMenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)  # rowspan allow button to take a space of 3
#  adding buttons with the help of a Button class

# total button
totalButton = Button(buttonFrame, text='Total', font=('arial', 13, 'bold'), bg='green', fg='white',
                     bd=5, width=8, pady=10, command=total)
totalButton.grid(row=0, column=0, pady=20, padx=5)

#  bills button
billButton = Button(buttonFrame, text='Bill', font=('arial', 13, 'bold'), bg='green', fg='white',
                    bd=5, width=8, pady=10, command=bill)
billButton.grid(row=0, column=1, pady=20, padx=5)

# email button
emailButton = Button(buttonFrame, text='email', font=('arial', 13, 'bold'), bg='green', fg='white',
                     bd=5, width=8, pady=10, command=emails)
emailButton.grid(row=0, column=2, pady=20, padx=5)
# printing button
printButton = Button(buttonFrame, text='print', font=('arial', 13, 'bold'), bg='green', fg='white',
                     bd=5, width=8, pady=10, command=prints)
printButton.grid(row=0, column=3, pady=20, padx=5)
# clear button
clearButton = Button(buttonFrame, text='CLEAR', font=('arial', 13, 'bold'), bg='green', fg='white',
                     bd=5, width=8, pady=7, command=clear)
clearButton.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()
