from core import  PictureCutting,Translate

if __name__=="__main__":
    p=PictureCutting("asserts/image.png")
    pic_path=p.recognize_cutting()
    t = Translate(pic_path,id="AKIDru3GUiyIe0OhuxpcGqEVbjegYO9lmaBY",key="JQM5ez73wc6MOp36ygDfw54rTxGPPFuO")
    re = t.Translate_string()
    print(re[0], re[1])
