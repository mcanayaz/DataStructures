# Düğüm Oluştur



class Node:
    def __init__(self, data,ad,soyad):
        self.item = data
        self.ad=ad
        self.soyad=soyad
        self.next = None
        self.prev = None
# Çift Yönlü liste için sınıf oluştur
class doublyLinkedList:
    def __init__(self):
        self.start_node = None
    # Boş listeye eleman ekleme
    def BosListeyeEkle(self, data, ad, soyad):
        if self.start_node is None:
            new_node = Node(data,ad,soyad)            
            self.start_node = new_node
        else:
            print("Liste bos degil")
    # En sona eleman ekleme
    def SonaEkle(self, data, ad, soyad):
        # Listenin boş olup olmadığını kontrol
        if self.start_node is None:
            new_node = Node(data,ad,soyad)
            self.start_node = new_node
            return
        n = self.start_node
        # NULL 'a ulaşana kadar ilerle
        while n.next is not None:
            n = n.next
        new_node = Node(data, ad, soyad)
        n.next = new_node
        new_node.prev = n
    # Baştan eleman silme
    def BastanSil(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None
    # Sondan Eleman Silme
    def SondanSil(self):
        # Listenin boş olup olmadığını kontrol
        if self.start_node is None:
            print("Liste bos eleman silinemez")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None
    def IstenilenYereEkle(self, prev_node, new_data):
        
        if prev_node is None:  # Düğümü sonrasına ekleyeceğimiz düğüm mecut değil ise?
            print("Sonrasına eklemek istediğiniz eleman bulunamadı")
            return
        n = self.start_node        
        
        while n.next is not None:
            if n.item==prev_node:                               
                break
            else:
                n = n.next 
        
        #print(n.item)
        n_sonra=n.next  #40 oldu      
        #print(n_sonra.item) 
        ID,ad,soyad=new_data       
                  
        new_node = Node(ID,ad,soyad)
        n.next = new_node
        new_node.prev = n
        new_node.next=n_sonra
       
       
        
    # Liste Elemanlarını göster
    def Goster(self):
        if self.start_node is None:
            print("Liste Bos")
            return
        else:
            n = self.start_node
            while n is not None:
                print("ID: ", n.item)
                print("Ad: ", n.ad)
                print("Soyad",n.soyad)
                n = n.next
        print("\n")
# Yeni çift yönlü liste oluştur
YeniIkiliListe = doublyLinkedList()
# Boş listeye eleman ekle
YeniIkiliListe.BosListeyeEkle(10,"Murat","Canayaz")
YeniIkiliListe.Goster()

# Sona Eleman Ekle
YeniIkiliListe.SonaEkle(20,"Ali","Akar")
YeniIkiliListe.SonaEkle(30,"Cezmi","Koç")
YeniIkiliListe.SonaEkle(40,"Hakan","Demir")
YeniIkiliListe.SonaEkle(50,"Sait","Deniz")
YeniIkiliListe.SonaEkle(60,"Hakim","Kerim")
print("****Liste Oluşturuldu****")
# Listeyi Göster
YeniIkiliListe.Goster()
new_data1=["35","Ahmet","Can"]
YeniIkiliListe.IstenilenYereEkle(30,new_data1)
YeniIkiliListe.Goster()
new_data2=["45","Umut","Can"]
YeniIkiliListe.IstenilenYereEkle(40,new_data2)
YeniIkiliListe.Goster()
print("****İstenilen Yere Elemanlar Eklendi****")
# Baştan Eleman Sil
YeniIkiliListe.BastanSil()
YeniIkiliListe.Goster()
print("****Baş Eleman Silindi****")
#Sondan Eleman Sil
YeniIkiliListe.SondanSil()
YeniIkiliListe.Goster()
print("****Son Eleman Silindi****")
