#Düğum sınıfı
class Node():

    def __init__(self,data): # Her düğüm iki bölümden oluşur 1.veri 2.işaretçi
        self.data = data     # Düğüme veri atadık
        self.next = None     # Şuan duğum nesnesi tek elemanlı olduğu için işaretçi boş


#Bağlı liste sınıfı
class LinkedList():

    def __init__(self):
        self.head = None   # Her bağlı listenin bir başı vardır

        # Listenin en başına ekleme
    def push(self, new_data):
        new_node = Node(new_data)  # yeni düğüm oluştur

        new_node.next = self.head  # yeni düğüm işaretçisi bağlı listenin başını göster
        self.head = new_node  # listenin başını yeni düğümü ata

    def print(self):
        temp = self.head

        while temp:
            print(temp.data, end=" =>")
            temp = temp.next

if __name__=='__main__':

    lliste = LinkedList()
    
    lliste.head = Node(5)
    second = Node(8)
    lliste.head.next= second
    lliste.push(3) #listenin başına 3 ekle
    lliste.print() #listeyi oku