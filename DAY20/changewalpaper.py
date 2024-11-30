import win32api
import win32com.client
import win32gui


def setWallpaper(imagePath):
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, imagePath, win32con.SPIF_UPDATEINFILE | win32con.SPIF_SENDCHANGE)

setWallpaper(r'C:\Users\Administrator\Desktop\UST_Training\DAY21\Image\sample16.jpg')