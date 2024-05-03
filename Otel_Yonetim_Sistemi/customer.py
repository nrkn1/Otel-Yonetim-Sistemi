from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox



class Mus_Pen:
    def __init__(self,root):
        self.root=root
        self.root.title("Otel Yönetim Sistemi")
        self.root.geometry("1297x552+233+222")
        
        self.var_id=StringVar()      
        self.var_ad=StringVar()
        self.var_cinsiyet=StringVar()
        self.var_tel=StringVar()
        self.var_mail=StringVar()
        self.var_uyruk=StringVar()
        self.var_adres=StringVar()
        self.var_tc=StringVar()

        
        lbl_baslik = Label(self.root,text="MÜŞTERİ BİLGİLERİ")
        lbl_baslik.place(x=0,y=0,width=1297,height=51)
        

        
        labelframeleft=LabelFrame(self.root,text="Müşteri Bilgileri")
        labelframeleft.place(x=5,y=50,width=427,height=491)
                            
        # müşteri id
        lbl_id=Label(labelframeleft,text="Müşteri ID") 
        lbl_id.grid(row=0,column=0)
     
        enty_id=ttk.Entry(labelframeleft,textvariable=self.var_id)
        enty_id.grid(row=0,column=1)
        
        # müşteri ad
        cad=Label(labelframeleft,text="Müşteri Adı:")
        cad.grid(row=1,column=0,sticky=W)
        txtcad=ttk.Entry(labelframeleft,textvariable=self.var_ad)
        txtcad.grid(row=1,column=1)
        
        # cinsiyet
        label_cinsiyet=Label(labelframeleft,text="Cinsiyet:")
        label_cinsiyet.grid(row=3,column=0,sticky=W)
        combo_cinsiyet=ttk.Combobox(labelframeleft,textvariable=self.var_cinsiyet)
        combo_cinsiyet["values"]=("Bay","Bayan")
        combo_cinsiyet.grid(row=3,column=1)
        
        # tel
        lbltel=Label(labelframeleft,text="Telefon Numarası:")
        lbltel.grid(row=5,column=0,sticky=W)
        txttel=ttk.Entry(labelframeleft,textvariable=self.var_tel)
        txttel.grid(row=5,column=1)
        
        # mail
        lblmail=Label(labelframeleft,text="E-Mail:")
        lblmail.grid(row=6,column=0,sticky=W)
        txtmail=ttk.Entry(labelframeleft,textvariable=self.var_mail)
        txtmail.grid(row=6,column=1)
        
        # uyruk                  
        lbluyruk=Label(labelframeleft,text="Uyruk:")
        lbluyruk.grid(row=7,column=0,sticky=W)
        txtuyruk=ttk.Entry(labelframeleft,textvariable=self.var_uyruk)
        txtuyruk.grid(row=7,column=1)
        
        # tc
        lbltc=Label(labelframeleft,text="T.C. Kimlik Numarası:")
        lbltc.grid(row=9,column=0,sticky=W)
        txttc=ttk.Entry(labelframeleft,textvariable=self.var_tc)
        txttc.grid(row=9,column=1)
        
        # adres
        lblAdres=Label(labelframeleft,text="Yaşadığı Ülke:")
        lblAdres.grid(row=10,column=0,sticky=W)
        txtAdres=ttk.Entry(labelframeleft,textvariable=self.var_adres)
        txtAdres.grid(row=10,column=1)
        
        btn_frame=Frame(labelframeleft,bd=2)
        btn_frame.place(x=90,y=400,width=410,height=37)
        
        btnEkle=Button(btn_frame,text="Ekle",command=self.ekle)
        btnEkle.grid(row=0,column=0,padx=1)
        
        btnGuncelle=Button(btn_frame,text="Güncelle",command=self.guncelle)
        btnGuncelle.grid(row=0,column=1,padx=1)
        
        btnSil=Button(btn_frame,text="Sil",command=self.sil)
        btnSil.grid(row=0,column=2,padx=1)
        
        btnSifirla=Button(btn_frame,text="Sıfırla",command=self.sifirla)
        btnSifirla.grid(row=0,column=3,padx=1)
        
       
        Table_Frame=LabelFrame(self.root,bd=2,text="Bilgileri Görüntüle")
        Table_Frame.place(x=435,y=50,width=860,height=490)
        
        lblAraBy=Label(Table_Frame,text="Ara:")
        lblAraBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.ara_var=StringVar()
        combo_Ara=ttk.Combobox(Table_Frame,textvariable=self.ara_var)
        combo_Ara["values"]=("tel","id")
        combo_Ara.grid(row=0,column=1,padx=2)
        
        self.txtAra=StringVar()
        txtAra=ttk.Entry(Table_Frame,textvariable=self.txtAra)
        txtAra.grid(row=0,column=2,padx=2)
        
       
        btnAra=Button(Table_Frame,text="Ara",command=self.ara)
        btnAra.grid(row=0,column=3,padx=1)
        
        btnGoster=Button(Table_Frame,text="Tümünü Göster",command=self.veri)
        btnGoster.grid(row=0,column=4,padx=1)
        
        
        tablo=Frame(Table_Frame)
        tablo.place(x=0,y=50,width=860,height=350)
        
        scroll_x=ttk.Scrollbar(tablo,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tablo,orient=VERTICAL)
        
        self.Musteri_Tablosu=ttk.Treeview(tablo,column=("id","ad","cinsiyet","tel",
                                                                   
       "mail","uyruk","tc","adres"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Musteri_Tablosu.xview)
        scroll_y.config(command=self.Musteri_Tablosu.yview)
      
        self.Musteri_Tablosu.heading("id",text="Müşteri ID")
        self.Musteri_Tablosu.heading("ad",text="İsim")
        self.Musteri_Tablosu.heading("cinsiyet",text="Cinsiyet")
        self.Musteri_Tablosu.heading("tel",text="Telefon No")
        self.Musteri_Tablosu.heading("mail",text="E-Mail")
        self.Musteri_Tablosu.heading("uyruk",text="Uyruk")
        self.Musteri_Tablosu.heading("tc",text="T.C. Kimlik Numarası")
        self.Musteri_Tablosu.heading("adres",text="Yaşadığı Ülke")
    
        self.Musteri_Tablosu["show"]="headings"
        
        
        self.Musteri_Tablosu.column("id",width=100)
        self.Musteri_Tablosu.column("ad",width=100)
        self.Musteri_Tablosu.column("cinsiyet",width=100)
        self.Musteri_Tablosu.column("tel",width=100)
        self.Musteri_Tablosu.column("mail",width=100)
        self.Musteri_Tablosu.column("uyruk",width=100)
        self.Musteri_Tablosu.column("tc",width=100)
        self.Musteri_Tablosu.column("adres",width=100)
        
        self.Musteri_Tablosu.pack(fill=BOTH,expand=1)
        self.Musteri_Tablosu.bind("<ButtonRelease-1>",self.veri_goster)
        self.veri()                   
        
        
    def ekle(self):
        if self.var_tel.get()=="" or self.var_ad.get()=="" or self.var_cinsiyet.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Hata","Lütfen Gerekli Bilgileri Giriniz",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into musteri values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_id.get(),
                                                                                self.var_ad.get(),
                                                                                self.var_cinsiyet.get(),
                                                                                self.var_tel.get(),
                                                                                self.var_mail.get(),
                                                                                self.var_uyruk.get(),
                                                                                self.var_tc.get(),
                                                                                self.var_adres.get()
                                                                                ))
                                                                               
                conn.commit()
                self.veri()
                conn.close()                                                              
                messagebox.showinfo("Başarılı","Müşteri Başarıyla Eklendi",parent=self.root)
                
            except Exception:
                messagebox.showwarning("Uyarı","Bu ID de Zaten Bir Müşteri Var",parent=self.root)
          
        
        
    def veri(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from musteri")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Musteri_Tablosu.delete(*self.Musteri_Tablosu.get_children())
            for i in rows:
                self.Musteri_Tablosu.insert("",END,values=i)
            conn.commit()       
        conn.close()
        
    def veri_goster(self,event=""):
        cursor_row=self.Musteri_Tablosu.focus()
        content=self.Musteri_Tablosu.item(cursor_row)
        row=content["values"]
        
        self.var_id.set(row[0]),
        self.var_ad.set(row[1]),
        self.var_cinsiyet.set(row[2]),
        self.var_tel.set(row[3]),
        self.var_mail.set(row[4]),
        self.var_uyruk.set(row[5]),
        self.var_tc.set(row[6]),
        self.var_adres.set(row[7])
        
        
    def guncelle(self):
        if self.var_tel.get()=="":
           messagebox.showerror("Hata","Telefon Numarasını Giriniz",parent=self.root)
        else:          
           conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
           my_cursor=conn.cursor()
           my_cursor.execute("update musteri set ad=%s,cinsiyet=%s,tel=%s,mail=%s,uyruk=%s,tc=%s,adres=%s where id=%s",(
                                                       
                                                       self.var_ad.get(),
                                                       self.var_cinsiyet.get(),
                                                       self.var_tel.get(),
                                                       self.var_mail.get(),
                                                       self.var_uyruk.get(),
                                                       self.var_tc.get(),
                                                       self.var_adres.get(),
                                                       self.var_id.get()



                                                         
                                                                               ))
           
           conn.commit()
           self.veri()
           conn.close()
           messagebox.showinfo("Güncelleme","Müşteri Bilgileri Başarıyla Güncellendi",parent=self.root)
    
   
    def sil(self):
        sil=messagebox.askyesno("Otel Yönetim Sistemi","Bu Müşteriyi Silmek İstiyor musunuz?",parent=self.root)
        if sil>0:
            conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
            my_cursor=conn.cursor()
            query="delete from musteri where id=%s"
            value=(self.var_id.get(),)
            my_cursor.execute(query,value)
        
        else:
            if not sil:
                return
        conn.commit()
        self.veri()
        conn.close()
        
    def sifirla(self):
        self.var_id.set(""),
        self.var_ad.set(""),
        self.var_tel.set(""),
        self.var_mail.set(""),
        self.var_uyruk.set(""),
        self.var_tc.set(""),
        self.var_adres.set("")

        
    def ara(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
        my_cursor=conn.cursor()        
        my_cursor.execute("select * from musteri where "+str(self.ara_var.get())+" LIKE '%"+str(self.txtAra.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows) != 0:
            self.Musteri_Tablosu.delete(*self.Musteri_Tablosu.get_children())  
            for i in rows:
                self.Musteri_Tablosu.insert("",END,values=i)
            conn.commit()
        conn.close()
        
if __name__ == "__main__":
    root=Tk()
    obj=Mus_Pen(root)
    root.mainloop()