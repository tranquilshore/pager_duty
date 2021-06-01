
class Notification:
    def __init__(self,number,message):
        self.number = str(number)
        self.message = message
        
    def send(self):
        msg = "Message: "+ self.message +" Sent Successfully to: "+self.number
        return msg
