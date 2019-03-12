import webbrowser
class movie:
    def __init__(self,a,i,s,h):
        self.a=a
        self.i=i
        self.s_url=s
        self.h_url=h
    def show_trailer(self):
        webbrowser.open(self.h_url)
        
