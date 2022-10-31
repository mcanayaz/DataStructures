# Düğüm Oluştur
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
# Çift Yönlü liste için sınıf oluştur
class doublyLinkedList:
    def __init__(self):
        self.start_node = None
    # Boş listeye eleman ekleme
    def BosListeyeEkle(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("Liste bos degil")
    # En sona eleman ekleme
    def SonaEkle(self, data):
        # Listenin boş olup olmadığını kontrol
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # NULL 'a ulaşana kadar ilerle
        while n.next is not None:
            n = n.next
        new_node = Node(data)
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
        self.start_prev = None;
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
        new_node = Node(new_data)
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
                print("Element is: ", n.item)
                n = n.next
        print("\n")
# Yeni çift yönlü liste oluştur
YeniIkiliListe = doublyLinkedList()
# Boş listeye eleman ekle
YeniIkiliListe.BosListeyeEkle(10)

# Sona Eleman Ekle
YeniIkiliListe.SonaEkle(20)
YeniIkiliListe.SonaEkle(30)
YeniIkiliListe.SonaEkle(40)
YeniIkiliListe.SonaEkle(50)
YeniIkiliListe.SonaEkle(60)
print("****Liste Oluşturuldu****")
# Listeyi Göster
YeniIkiliListe.Goster()
YeniIkiliListe.IstenilenYereEkle(30,35)
YeniIkiliListe.Goster()
YeniIkiliListe.IstenilenYereEkle(40,45)
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
