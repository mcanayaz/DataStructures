#Düğum sınıfı
class Node():

    def __init__(self,data): # Her düğüm iki bölümden oluşur 1.veri 2.işaretçi
        self.data = data     # Düğüme veri atadık
        self.next = None     # Şuan duğum nesnesi tek elemanlı olduğu için işaretçi boş


#Bağlı liste sınıfı
class LinkedList():

    def __init__(self):
        self.head = None   # Her bağlı listenin bir başı vardır

    # Herhangi bir düğümden sonra düğüm ekleme
    def insert(self, prev_node, new_data):
        if prev_node is None:  # Düğümü sonrasına ekleyeceğimiz düğüm mecut değil ise?
            print("Sonrasına eklemek istediğiniz eleman bulunamadı")
            return

        new_node = Node(new_data)  # yeni düğüm oluştur
        new_node.next = prev_node.next  # yeni düğümün işaretçisini sonrasına eklemek istediğimiz düğümün işaretçisine ata
        prev_node.next = new_node  # sonrasına eklemek istediğimiz düğümün işarettçisi yeni düğümü göster

    def print(self):
        temp = self.head

        while temp:
            print(temp.data, end=" =>")
            temp = temp.next

if __name__=='__main__':

    lliste = LinkedList()

    lliste.head = Node(5)
    second = Node(8)
    third =  Node(10)

    lliste.head.next= second
    second.next=third


    lliste.insert(lliste.head.next,13) #listenin başından sonraki elemamın arkasına 13 ekle
    lliste.print() #listeyi oku