#Düğum sınıfı
class Node():

    def __init__(self,data): # Her düğüm iki bölümden oluşur 1.veri 2.işaretçi
        self.data = data     # Düğüme veri atadık
        self.next = None     # Şuan duğum nesnesi tek elemanlı olduğu için işaretçi boş


#Bağlı liste sınıfı
class LinkedList():

    def __init__(self):
        self.head = None   # Her bağlı listenin bir başı vardır

    def countList(self):
        temp = self.head
        count =0

        while temp:
            count +=1
            temp = temp.next
        return count


if __name__=='__main__':

    lliste = LinkedList()

    lliste.head = Node(5)
    second = Node(8)
    third =  Node(10)

    lliste.head.next= second
    second.next=third


    print("Listenin Eleman sayısı:",lliste.countList())