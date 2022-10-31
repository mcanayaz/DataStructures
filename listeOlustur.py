#Düğum sınıfı
class Node():

    def __init__(self,data): # Her düğüm iki bölümden oluşur 1.veri 2.işaretçi
        self.data = data     # Düğüme veri atadık
        self.next = None     # Şuan duğum nesnesi tek elemanlı olduğu için işaretçi boş


#Bağlı liste sınıfı
class LinkedList():

    def __init__(self):
        self.head = None   # Her bağlı listenin bir başı vardır


if __name__ =='__main__':
    lliste= LinkedList() # LinkedListt sınıfından nesne oluşturduk
    lliste.head = Node(1) #Linkedlist başına 1 atadık
    second = Node(2)      #ikinci düğüme 2 ekledık
    third = Node(3)       #üçüncü düğüme 3 ekledik

    lliste.head.next = second #Listenin başı ikinci düğümün adresini tutuyor
    second.next =third        #ikinci düğümün üçüncü düğümün adresini tutuyor