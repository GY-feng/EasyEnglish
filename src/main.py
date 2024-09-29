from core import  PictureCutting,Translate

if __name__=="__main__":
    p=PictureCutting("asserts/image.png")
    pic_path=p.recognize_cutting()
    #t = Translate(pic_path)
    re = t.Translate_string()
    print(re[0], re[1])
