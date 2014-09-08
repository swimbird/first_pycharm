class Island:
    def __init__(self, name, opens, closes, next=None):
        self.name = name
        self.opens = opens
        self.closes = closes
        self.next = next

    def display(self):
        print('name:{0} working time:{1}-{2}'
              .format(self.name, self.opens, self.closes))
        if self.next:
            self.next.display()

amity = Island('amity', '9:00', '17:00')
craggy = Island('craggy', '9:00', '17:00')
isla_nublar = Island('isla_nublar', '9:00', '17:00')
shutter = Island('shutter', '9:00', '17:00')
skull = Island('skull', '9:00', '17:00')

amity.next = craggy
craggy.next = isla_nublar
isla_nublar.next = shutter
shutter.next = skull

amity.display()
