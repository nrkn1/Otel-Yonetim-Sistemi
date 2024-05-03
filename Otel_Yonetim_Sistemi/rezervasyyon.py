from tkinter import*
from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Rezervasyon:
    def __init__(self,root):
        self.root=root
        self.root.title("Otel Yönetim Sistemi")
        self.root.geometry("1298x552+231+223")
        


        self.var_iletisim=StringVar()
        self.var_giris=StringVar()
        self.var_cikis=StringVar()
        self.var_odaturu=StringVar()
        self.var_bosoda=StringVar()
        self.var_gun=StringVar()    
        


        lbl_baslik = Label(self.root,text="REZERVASYON BİLGİLERİ")
        lbl_baslik.place(x=0,y=0,width=1297,height=53)

        
        labelframeleft=LabelFrame(self.root,text="Oda Bilgileri")
        labelframeleft.place(x=7,y=52,width=427,height=309)
        
        # iletisim
        lbl_iletisim=Label(labelframeleft,text="Telefon Numarası:") 
        lbl_iletisim.grid(row=0,column=0,sticky=W)
     
        enty_iletisim=ttk.Entry(labelframeleft,textvariable=self.var_iletisim)
        enty_iletisim.grid(row=0,column=1,sticky=W)
                                                    
        #giriş tarihi
        giris=Label(labelframeleft,text="Giriş Tarihi:")
        giris.grid(row=1,column=0,sticky=W)
        txtgiris=ttk.Entry(labelframeleft,textvariable=self.var_giris)
        txtgiris.grid(row=1,column=1)
        
        #çıkış tarihi
        lblcikis=Label(labelframeleft,text="Çıkış Tarihi:")
        lblcikis.grid(row=2,column=0,sticky=W)
        txtcikis=ttk.Entry(labelframeleft,textvariable=self.var_cikis)
        txtcikis.grid(row=2,column=1)
        
        #oda türü
        label_odaturu=Label(labelframeleft,text="Oda Türü:")
        label_odaturu.grid(row=3,column=0,sticky=W)
        
        
        conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
        my_cursor=conn.cursor()
        my_cursor.execute("select distinct odaturu from oda")
        ide=my_cursor.fetchall()
        
        combo_odaturu=ttk.Combobox(labelframeleft,textvariable=self.var_odaturu)
        combo_odaturu["value"]=ide
        combo_odaturu.grid(row=3,column=1)
        
        # uygun oda
        lbloda=Label(labelframeleft,text="Boş Odalar:")        
        lbloda.grid(row=4,column=0,sticky=W)

       
        conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
        my_cursor=conn.cursor()
        my_cursor.execute("select odano from oda")
        rows=my_cursor.fetchall()
           
        combo_odano=ttk.Combobox(labelframeleft,textvariable=self.var_bosoda)
        combo_odano["value"]=rows
        combo_odano.grid(row=4,column=1)   
        
        # Gün Sayısı
        lblgun=Label(labelframeleft,text="Gün Sayısı:")        
        lblgun.grid(row=5,column=0,sticky=W)
        txtgun =ttk.Entry(labelframeleft,textvariable=self.var_gun)
        txtgun.grid(row=5,column=1) 
     
        btn_frame=Frame(labelframeleft)
        btn_frame.place(x=60,y=137,width=413,height=37)
        
        btnEkle=Button(btn_frame,text="Ekle",command=self.ekle)
        btnEkle.grid(row=0,column=0)
        
        btnGuncelle=Button(btn_frame,text="Güncelle",command=self.guncelle)
        btnGuncelle.grid(row=0,column=1)
        
        btnSil=Button(btn_frame,text="Sil",command=self.sil)
        btnSil.grid(row=0,column=2)
        
        btnSifirla=Button(btn_frame,text="Sıfırla",command=self.sifirla)
        btnSifirla.grid(row=0,column=3)
        
        
       
        cerceve=LabelFrame(self.root,text="Bilgileri Görüntüle")
        cerceve.place(x=401,y=57,width=865,height=303)        
        
        cerceve=Frame(cerceve)  
        cerceve.place(x=0,y=50,width=860,height=180)
        
        scroll_x=ttk.Scrollbar(cerceve,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(cerceve,orient=VERTICAL)
        
        self.rez_tablo=ttk.Treeview(cerceve,column=("iletisim","giris","cikis","odaturu","bosoda",
                                                                   
       "gun",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.rez_tablo.xview)
        scroll_y.config(command=self.rez_tablo.yview)
      
        self.rez_tablo.heading("iletisim",text="İletişim")
        self.rez_tablo.heading("giris",text="Giriş")
        self.rez_tablo.heading("cikis",text="Çıkış")
        self.rez_tablo.heading("odaturu",text="Oda Türü")
        self.rez_tablo.heading("bosoda",text="Oda Numarası")
        self.rez_tablo.heading("gun",text="Gün Sayısı")

        self.rez_tablo["show"]="headings"
        
        self.rez_tablo.column("iletisim",width=100)
        self.rez_tablo.column("giris",width=100)
        self.rez_tablo.column("cikis",width=100)
        self.rez_tablo.column("odaturu",width=100)
        self.rez_tablo.column("bosoda",width=100)
        self.rez_tablo.column("gun",width=100)
        self.rez_tablo.pack(fill=BOTH,expand=1)
        self.rez_tablo.bind("<ButtonRelease-1>",self.veri_goster)
        self.veri()
        
        
    def ekle(self):
        if self.var_iletisim.get()=="" or self.var_giris.get()=="":
            messagebox.showerror("Hata","Lütfen Zorunlu Bilgileri Giriniz")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into rezervasyyon values(%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_iletisim.get(),            
                                                                                self.var_giris.get(),
                                                                                self.var_cikis.get(),
                                                                                self.var_odaturu.get(),
                                                                                self.var_bosoda.get(),
                                                                                self.var_gun.get()
                                                                                
                                                                                ))
                                                                               
                conn.commit()
                self.veri()
                conn.close()                                                              
                messagebox.showinfo("Başarılı","Oda Rezervasyonu Yapıldı",parent=self.root)
            except Exception:
                messagebox.showwarning("Uyarı","Lütfen Başka Bir Numara Giriniz",parent=self.root)
                
    def veri(self):
         conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
         my_cursor=conn.cursor()
         my_cursor.execute("select * from rezervasyyon")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.rez_tablo.delete(*self.rez_tablo.get_children())
             for i in rows:
                 self.rez_tablo.insert("",END,values=i)
             conn.commit()       
         conn.close()    
    
         
    
    def veri_goster(self,event=""):
         cursor_row=self.rez_tablo.focus()
         content=self.rez_tablo.item(cursor_row)
         row=content["values"]
         
         self.var_iletisim.set(row[0])         
         self.var_giris.set(row[1])
         self.var_cikis.set(row[2])
         self.var_odaturu.set(row[3])
         self.var_bosoda.set(row[4])
         self.var_gun.set(row[5])
    
    
    def guncelle(self):
        if self.var_iletisim.get()=="":
           messagebox.showerror("Hata","Lütfen Telefon Numarasını Giriniz",parent=self.root)
        else:          
           conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
           my_cursor=conn.cursor()
           my_cursor.execute("update rezervasyyon set giris=%s,cikis=%s,odaturu=%s,bosoda=%s,gun=%s where iletisim=%s",(
                                                       
                                                       self.var_giris.get(),
                                                       self.var_cikis.get(),
                                                       self.var_odaturu.get(),
                                                       self.var_bosoda.get(),
                                                       self.var_gun.get(),
                                                       self.var_iletisim.get()
                                                       



                                                         
                                                                               ))
           
           conn.commit()
           self.veri()
           conn.close()
           messagebox.showinfo("Guncelle","Oda Bilgileri Başarıyla Güncellendi",parent=self.root)


    def sil(self):
        sil=messagebox.askyesno("Otel Yönetim Sistemi","Bu Müşteriyi Silmek İstiyor musunuz",parent=self.root)
        if sil>0:
            conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
            my_cursor=conn.cursor()
            query="delete from rezervasyyon where iletisim=%s"
            value=(self.var_iletisim.get(),)
            my_cursor.execute(query,value)
        
        else:
            if not sil:
                return
        conn.commit()
        self.veri()
        conn.close()    
    


    def sifirla(self):
        self.var_iletisim.set("")         
        self.var_giris.set("")
        self.var_cikis.set("")
        self.var_odaturu.set("")
        self.var_odaa.set("")
        self.var_gun.set("")

 
    
 

if __name__ == "__main__":
    root=Tk()
    obj=Rezervasyon(root)
    root.mainloop()
    
    
    