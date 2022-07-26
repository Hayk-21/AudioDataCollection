#https://stackoverflow.com/questions/21549847/send-key-combination-with-python
#https://msdn.microsoft.com/en-us/library/8c6yea83(v=vs.84).aspx

import win32com.client as comclt
def change_status():
    wsh= comclt.Dispatch("WScript.Shell")
    # wsh.SendKeys("ON!") #types out abc directly into wherever you have your cursor (ex: right into this editor itself!)
    wsh.SendKeys("{CAPSLOCK}") #toggles the state of NumLock, CapsLock, and ScrollLock; remove whichever one you don't want to toggle
