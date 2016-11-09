#coding:utf8  
#环境要求:python2.7x,PIL,pywin32  
#备注:只在win7系统试过正常  
#创建时间:2016.11.09
  
import Image  
import ImageFont,ImageDraw
import win32api,win32con,win32gui  
import re,os
import datetime
ISOTIMEFORMAT='%Y-%m-%d %X'
def set_wallpaper_from_bmp(bmp_path):  
    #打开指定注册表路径  
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)  
    #最后的参数:2拉伸,0居中,6适应,10填充,0平铺  
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")  
    #最后的参数:1表示平铺,拉伸居中等都是0  
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")  
    #刷新桌面  
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,bmp_path, win32con.SPIF_SENDWININICHANGE)  
  
def set_wallpaper(img_path):  
    #把图片格式统一转换成bmp格式,并放在源图片的同一目录  
    img_dir = os.path.dirname(img_path)  
    bmpImage = Image.open(img_path)  
    new_bmp_path = os.path.join(img_dir,'wallpaper.bmp')  
    bmpImage.save(new_bmp_path, "BMP")  
    set_wallpaper_from_bmp(new_bmp_path)  
#根据倒计时创建图片文字
def createTimePic(img_path):
    font = ImageFont.truetype('simsun.ttc',50)
    im = Image.open(img_path)
    draw = ImageDraw.Draw(im)
    text = unicode(getDaoJiShi(datetime.datetime(2016, 12, 30, 19, 55)),'utf-8')
    draw.text((850,570), text, font=font, fill=(0,0,0,0))
    im.save('images\\time.jpg')

def getDaoJiShi(endtime):
    nowtime = datetime.datetime.now()
    # endtime = datetime.datetime(2016, 12, 30, 19, 55)
    days = (endtime - nowtime).days
    hours = (endtime - nowtime).seconds/60/60
    timeStr = ''.join([str(days),'天',str(hours),'小时'])
    return timeStr

if __name__ == '__main__': 
    createTimePic('images\\img0.jpg')
    set_wallpaper('images\\time.jpg')  
