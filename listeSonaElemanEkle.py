#Düğum sınıfı
class Node():

    def __init__(self,data): # Her düğüm iki bölümden oluşur 1.veri 2.işaretçi
        self.data = data     # Düğüme veri atadık
        self.next = None     # Şuan duğum nesnesi tek elemanlı olduğu için işaretçi boş


#Bağlı liste sınıfı
class LinkedList():

    def __init__(self):
        self.head = None   # Her bağlı listenin bir başı vardır

    # En sona düğüm eklemek
    def append(self, new_data):

        new_node = Node(new_data)  # yeni düğüm oluştur

        if self.head is None:  # Eğer bağlı liste boş ise yeni düğümü ekle ve yeni düğüm listenin başı olur
            self.head = new_node
            return

        temp = self.head  # Dolaştırıcı oluştur ve listenin başını başlangıç olarak ata

        while temp.next:  # listenin sonuna kadar git
            temp = temp.next  # teker teker arttır

        # while düngüsü bittiğinde dolaştırıcı listenin en sonunu yani boş olan işaretçiyi gösterir
        temp.next = new_node  # Düğümü ekle



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


    lliste.append(25) #listenin en sonuna 25 ekle
    lliste.print() #listeyi oku