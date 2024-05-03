from tkinter import*
from customer import Mus_Pen
from oda import odabilgileri
from rezervasyyon import Rezervasyon





class OtelYonetim:
    def __init__(self,root):
        self.root=root
        self.root.title("Otel Yönetim Sistemi")
        self.root.geometry("1554x801+0+0")
    
        
     
        lbl_title = Label(self.root,text="OTEL YÖNETİM SİSTEMİ",font=("arial",14,"bold"),bd=4)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        
        main_frame=Frame(self.root,bd=4)
        main_frame.place(x=0,y=190,width=1550,height=620)
      
        lbl_menu=Label(main_frame,text="MENU",bd=4)
        lbl_menu.place(x=630,y=0,width=231)
        
        btn_frame=Frame(main_frame,bd=4)
        btn_frame.place(x=702,y=35,width=231,height=190)
        
        otel_btn=Button(btn_frame,text="MÜŞTERİ",command=self.Musteri_Tablo)
        otel_btn.grid(row=0,column=0,pady=1)
        
        otel_btn=Button(btn_frame,text="ODA BİLGİLERİ",command=self.Oda_Tablo)
        otel_btn.grid(row=1,column=0,pady=8)
        
        otel_btn=Button(btn_frame,text="REZERVASYON",command=self.Rezervasyon_Tablo)
        otel_btn.grid(row=2,column=0,pady=8)
        
        

    


        
        
    def Musteri_Tablo(self):
        self.new_window=Toplevel(self.root)
        self.app=Mus_Pen(self.new_window)
        
    def Oda_Tablo(self):
        self.new_window=Toplevel(self.root)
        self.app=odabilgileri(self.new_window)
        
    def Rezervasyon_Tablo(self):
        self.new_window=Toplevel(self.root)
        self.app=Rezervasyon(self.new_window)
        

if __name__ == "__main__":
    root=Tk()
    obj=OtelYonetim(root)
    root.mainloop()