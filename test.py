import vpython as vp
day = 0
month = 0
year = 0
vp.winput(bind=setday, pos=vp.scene.title_anchor)
vp.winput(bind=setmonth, pos=vp.scene.title_anchor)
vp.winput(bind=setyear, pos=vp.scene.title_anchor)
vp.button(text="display at", bind=showat, pos=vp.scene.title_anchor)

def showat():
    global day
    global month
    global year
    #need conditions
    display_at(year, month, day)
