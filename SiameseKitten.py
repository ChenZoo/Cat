

class Cat(object):
    
    def __init__(self):
        print "I am Cat!"
        


class SiameseKitten(Cat):
    
    def __init__(self):
        super(SiameseKitten, self).__init__()
        print "I am SiameseKitten!"
        
        
SiameseKitten()
