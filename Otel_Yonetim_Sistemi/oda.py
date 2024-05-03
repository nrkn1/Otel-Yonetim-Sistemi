from tkinter import*
from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class odabilgileri:
    def __init__(self,root):
        self.root=root
        self.root.title("Otel Yönetim Sistemi")
        self.root.geometry("1297x552+232+222")

        lbl_baslik = Label(self.root,text="ODA BİLGİLERİ")
        lbl_baslik.place(x=0,y=0,width=1295,height=50)
        
        self.var_odano=StringVar()
        self.var_kat=StringVar()
        self.var_odaturu=StringVar()
        
        labelframeleft=LabelFrame(self.root,bd=2,text="Yeni Oda Ekle")
        labelframeleft.place(x=5,y=50,width=540,height=350)

        # oda no
        lbl_odano=Label(labelframeleft,text="Oda Numarası:")
        lbl_odano.grid(row=0,column=0,sticky=W)
        
        enty_odano=ttk.Entry(labelframeleft,textvariable=self.var_odano)
        enty_odano.grid(row=0,column=1,sticky=W)   

        # kat
        lbl_kat=Label(labelframeleft,text="Kat Numarası:") 
        lbl_kat.grid(row=1,column=0,sticky=W)
    
        enty_kat=ttk.Entry(labelframeleft,textvariable=self.var_kat)
        enty_kat.grid(row=1,column=1,sticky=W)

        #oda türü
        lbl_odaturu=Label(labelframeleft,text="Oda Türü:")
        lbl_odaturu.grid(row=2,column=0,sticky=W)
        
        enty_odaturu=ttk.Entry(labelframeleft,textvariable=self.var_odaturu)
        enty_odaturu.grid(row=2,column=1,sticky=W)

        btn_frame=Frame(labelframeleft,bd=2)
        btn_frame.place(x=157,y=201,width=413,height=37)
         
        btnEkle=Button(btn_frame,text="Ekle",command=self.ekle)
        btnEkle.grid(row=0,column=0,padx=1)
         
        btnGuncelle=Button(btn_frame,text="Güncelle",command=self.guncelle)
        btnGuncelle.grid(row=0,column=1,padx=1)
         
        btnSil=Button(btn_frame,text="Sil",command=self.sil)
        btnSil.grid(row=0,column=2,padx=1)
        
        btnSifirla=Button(btn_frame,text="Sıfırla",command=self.sifirla)
        btnSifirla.grid(row=0,column=3,padx=1)


        
        cerceve=LabelFrame(self.root,text="Bilgileri Görüntüle")
        cerceve.place(x=601,y=57,width=602,height=352)

        scroll_x=ttk.Scrollbar(cerceve,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(cerceve,orient=VERTICAL)
        
        self.Oda_Tablosu=ttk.Treeview(cerceve,column=("odano","kat","odaturu"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Oda_Tablosu.xview)
        scroll_y.config(command=self.Oda_Tablosu.yview)        
    
        self.Oda_Tablosu.heading("odano",text="Oda Numarası")        
        self.Oda_Tablosu.heading("kat",text="Kat Numarası")
        self.Oda_Tablosu.heading("odaturu",text="Oda Türü")
    
          
        self.Oda_Tablosu["show"]="headings"
        
        self.Oda_Tablosu.column("odano",width=100)
        self.Oda_Tablosu.column("kat",width=100)
        self.Oda_Tablosu.column("odaturu",width=100)
        
        self.Oda_Tablosu.pack(fill=BOTH,expand=1)
        self.Oda_Tablosu.bind("<ButtonRelease-1>",self.veri_goster)
        self.veri()
        
        
        

    def ekle(self):
        if  self.var_odano.get()=="" or self.var_kat.get()=="":
            messagebox.showerror("Hata","Lütfen Gerekli Bilgileri Giriniz",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into oda values(%s,%s,%s)",(
                                                                                self.var_odano.get(),
                                                                                self.var_kat.get(),            
                                                                                self.var_odaturu.get()      
                                                                               
                                                                                
                                                                                
                                                                   
                                                                                ))
                                                                               
                conn.commit()
                self.veri()
                conn.close()                                                              
                messagebox.showinfo("Başarılı","Yeni Oda Başarıyla Eklendi",parent=self.root)
            except Exception:
                messagebox.showwarning("Hata","Lütfen Başka Bir Oda Numarası Giriniz",parent=self.root)


    def veri(self):
         conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
         my_cursor=conn.cursor()
         my_cursor.execute("select * from oda")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.Oda_Tablosu.delete(*self.Oda_Tablosu.get_children())
             for i in rows:
                 self.Oda_Tablosu.insert("",END,values=i)
             conn.commit()       
         conn.close()    

    def veri_goster(self,event=""):
         cursor_row=self.Oda_Tablosu.focus()
         content=self.Oda_Tablosu.item(cursor_row)
         row=content["values"]
        
         self.var_odano.set(row[0]),
         self.var_kat.set(row[1]),            
         self.var_odaturu.set(row[2])
         
    def guncelle(self):
        if self.var_kat.get()=="":
           messagebox.showerror("Hata","Lütfen Kat Numarasını Giriniz",parent=self.root)
        else:          
           conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
           my_cursor=conn.cursor()
           my_cursor.execute("update oda set kat=%s,odaturu=%s where odano=%s",(
                                                       
                                                       self.var_kat.get(),
                                                       self.var_odaturu.get(),
                                                       self.var_odano.get()
                                                         
                                                                               ))
           
           conn.commit()
           self.veri()
           conn.close()
           messagebox.showinfo("Update","Oda Bilgileri Başarıyla Güncellendi",parent=self.root) 

    def sil(self):
        sil=messagebox.askyesno("Otel Yönetim Sistemi","Bu Oda Bilgilerini Silmek İstiyor musunuz?",parent=self.root)
        if sil>0:
            conn=mysql.connector.connect(host='localhost',user='root',password='Nurkan.2001',database='yonetim',charset='utf8mb4')
            my_cursor=conn.cursor()
            query="delete from oda where odano=%s"
            value=(self.var_odano.get(),)
            my_cursor.execute(query,value)
         
        else:
            if not sil:
                return
        conn.commit()
        self.veri()
        conn.close()    

    def sifirla(self):
        self.var_kat.set("")
        self.var_odano.set("")
        self.var_odaturu.set("")



if __name__ == "__main__":
    root=Tk()
    obj=odabilgileri(root)
    root.mainloop()
    