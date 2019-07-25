from orbitModeling import *
from load_star_database import load_star_database
from load_planet_database import load_planet_database
from load_satellite_database import load_satellite_database
from hohmann_transfer import *
import vpython as vp
import time
import datetime
from eclipse_predictor import *

from setup_master_database import setup_master_database
setup_master_database()
list_of_planets = load_planet_database()
list_of_satellites = load_satellite_database()
list_of_planet_models = []
list_of_satellite_models = []
list_of_planet_names = []
list_of_planet_angles = []
list_of_satellite_names = []

def simulate_next_planet_iteration(t): #simulates all the planets for an increment t
    for planet in list_of_planets:
        planet.simulate_orbit(t)
        list_of_planet_models[list_of_planets.index(planet)].pos = vp.vector(planet.xPos / 10000000, planet.yPos / 10000000, planet.zPos / 10000000)
        list_of_planet_names[list_of_planets.index(planet)].pos = list_of_planet_models[list_of_planets.index(planet)].pos

        

def prediction():
    global ecl
    print(ecl)
    predict = eclipse_predictor(ecl)
    for result in predict:
        vp.wtext(text=result)
        print(result)
        vp.scene.append_to_caption('\n')


eclipses ='eclipses'
        
        
def simulate_next_satellite_iteration(t): #simulate all the satellites for an increment t
    for satellite in list_of_satellites:
        for planet in list_of_planets:
            if satellite.host == planet.name:
                satellite.simulate_orbit(t, planet)
                list_of_satellite_models[list_of_satellites.index(satellite)].pos = vp.vector(satellite.xPos / 10000000, satellite.yPos / 10000000, satellite.zPos / 10000000)
                list_of_satellite_names[list_of_satellites.index(satellite)].pos = list_of_satellite_models[list_of_satellites.index(satellite)].pos
                break

def display_at(year, month, day):

    for planet in list_of_planets:
        planet.simulate_orbit_date(month, day, year, True)
        list_of_planet_models[list_of_planets.index(planet)].make_trail = False #disable trail
        list_of_planet_models[list_of_planets.index(planet)].pos = vp.vector(planet.xPos / 10000000, planet.yPos / 10000000, planet.zPos / 10000000)
        list_of_planet_names[list_of_planets.index(planet)].pos = list_of_planet_models[list_of_planets.index(planet)].pos
        list_of_planet_models[list_of_planets.index(planet)].make_trail = True #enable trail
    for satellite in list_of_satellites:
        for planet in list_of_planets:
            if satellite.host == planet.name:
                satellite.simulate_orbit_date(month, day, year, True, planet)
                list_of_satellite_models[list_of_satellites.index(satellite)].pos = vp.vector(satellite.xPos / 10000000, satellite.yPos / 10000000, satellite.zPos / 10000000)
                list_of_satellite_names[list_of_satellites.index(satellite)].pos = list_of_satellite_models[list_of_satellites.index(satellite)].pos
                break
    global current_date
    current_date = datetime.datetime(year = year, month = month, day = day)
    global pause #pause the simulation after redisplaying the bodies
    pause = True



def display():
    """
    # creates the visual representation of the planets
    earth = vp.sphere(texture=vp.textures.earth,
                      pos=vp.vector(celestpos[0] / 10000000, celestpos[1] / 10000000, celestpos[2] / 10000000),
                      make_trail=True, trail_type="points", interval=10, retain=25)
    mars = vp.sphere(color=vp.vector(1, 0, 0),
                     pos=vp.vector(celestpos[3] / 10000000, celestpos[4] / 10000000, celestpos[5] / 10000000),
                     make_trail=True, trail_type="points", interval=10, retain=25)
    #    venus = vp.sphere(color = vp.vector(1,1,.8), pos = vp.vector(celestpos[0] / 10000000,celestpos[0] / 10000000,celestpos[0] / 10000000), make_trail=True, trail_type="points", interval=10, retain=10)
    #    mercury = vp.sphere(color = vp.vector(.3,.3,.3), pos = vp.vector(celestpos[0] / 10000000,celestpos[0] / 10000000,celestpos[0] / 10000000), make_trail=True, trail_type="points", interval=10, retain=5)
    #    moon = vp.sphere(color = vp.vector(.3,.3,.3), pos = vp.vector(Moon.xPos / 10000000, Moon.yPos / 10000000,0))
    """
    global guidate
    global current_date
    while True:
        while pause == False:
            guiday = str(current_date.day)
            guimonth = str(current_date.month)
            guiyear = str(current_date.year)
            guidate.text = guiday + "/" + guimonth + "/" + guiyear

            simulate_next_planet_iteration(sl.value)
            simulate_next_satellite_iteration(sl.value)

            date_increment = datetime.timedelta(days = math.floor(sl.value), hours = (sl.value - math.floor(sl.value)) * 24)

            # simulates motion
            #            Moon.simulate_orbit(i, 0)
            #            Earth.simulate_orbit(t, 0)
            #            Venus.simulate_orbit(t, 0)
            #            Mercury.simulate_orbit(t, 0)
            #earth.pos = vp.vector(celestpos[0] / 10000000, celestpos[1] / 10000000, celestpos[2] / 10000000)
            #mars.pos = vp.vector(celestpos[3] / 10000000, celestpos[4] / 10000000, celestpos[5] / 10000000)
            #            venus.pos = vp.vector(Venus.xPos / 10000000,Venus.yPos / 10000000,0)
            #            mercury.pos = vp.vector(Mercury.xPos / 10000000, Mercury.yPos / 10000000,0)
            #       moon.pos = vp.vector(Moon.xPos / 10000000, Moon.yPos / 10000000,0)
            if (sl.value > 0):
                time.sleep(.01/sl.value)
            elif(sl.value < 0):
                time.sleep(.01/(-sl.value))
            else:
                time.sleep(.01)

            current_date = current_date + date_increment


def showat():
    global day
    global month
    global year
    #need conditions
    display_at(year, month, day)


def setday(d):
    global day
    day = d.number


def setmonth(m):
    global month
    month = m.number

def setspeed(s):
    speed = s

def setyear(y):
    global year
    year = y.number


pause = False

t = 0

day = 0

ecl = 0
def seteclipse(e):
    global ecl
    ecl = e.number


def Pause():
    global pause
    pause = True

def Play():
    global pause
    pause  = False

def Reset():
    vp.scene.width = 800
    vp.scene.height = 800
    vp.scene.range = 1.3
    vp.scene.title = "ANTIKYTHERA\n"
    vp.button(text="display", bind=display, pos=vp.scene.title_anchor)
    vp.scene.append_to_title('\n')
    vp.button(text="display at", bind=showat, pos=vp.scene.title_anchor)
    vp.scene.append_to_title('\n')
    vp.button(text="credits", bind=credits, pos=vp.scene.title_anchor)
    vp.winput(bind=setday, pos=vp.scene.title_anchor)
    vp.winput(bind=setmonth, pos=vp.scene.title_anchor)
    vp.winput(bind=setyear, pos=vp.scene.title_anchor)
    vp.scene.append_to_title('\n')
    current_date = datetime.datetime.today()
    guidate = vp.wtext(text="date")

def setPlanet1(inputOne):
    global planetOne
    val1 = inputOne.selected
    if val1 == "Mercury":
        planetOne = list_of_planets[0]
    elif val1 == "Venus":
        planetOne = list_of_planets[1]
    elif val1 == "Earth":
        planetOne = list_of_planets[2]
    elif val1 == "Mars":
        planetOne = list_of_planets[3]
    elif val1 == "Jupiter":
        planetOne = list_of_planets[4]
    elif val1 == "Saturn":
        planetOne = list_of_planets[5]
    elif val1 == "Uranus":
        planetOne = list_of_planets[6]
    elif val1 == "Neptune":
        planetOne = list_of_planets[7]
    elif val1 == "Pluto":
        planetOne = list_of_planets[8]

def setPlanet2(inputTwo):
    global planetTwo
    val2 = inputTwo.selected
    if val2 == "Mercury":
        planetTwo = list_of_planets[0]
    elif val2 == "Venus":
        planetTwo = list_of_planets[1]
    elif val2 == "Earth":
        planetTwo = list_of_planets[2]
    elif val2 == "Mars":
        planetTwo = list_of_planets[3]
    elif val2 == "Jupiter":
        planetTwo = list_of_planets[4]
    elif val2 == "Saturn":
        planetTwo = list_of_planets[5]
    elif val2 == "Uranus":
        planetTwo = list_of_planets[6]
    elif val2 == "Neptune":
        planetTwo = list_of_planets[7]
    elif val2 == "Pluto":
        planetTwo = list_of_planets[8]
def projCalc():
    orbital_transfer(planetOne,planetTwo)

def credits():
    t0 = vp.text(text='Jacob Jones', pos=vp.vec(5,5,0),color=vp.color.cyan, billboard=True, emissive=True)
    t1 = vp.text(text='Ralph Ghannam', pos=vp.vec(3,3,0),color=vp.color.cyan, billboard=True, emissive=True)
    t2 = vp.text(text='Matthew Cosman', pos=vp.vec(1,1,0),color=vp.color.cyan, billboard=True, emissive=True)
    t3 = vp.text(text='Ameer Noufal', pos=vp.vec(-1,-1,0),color=vp.color.cyan, billboard=True, emissive=True)
    t4 = vp.text(text='Akshar Patel', pos=vp.vec(-3,-3,0),color=vp.color.cyan, billboard=True, emissive=True)
    t5 = vp.text(text='Daniel Smith De-Paz', pos=vp.vec(-5,-5,0),color=vp.color.cyan, billboard=True, emissive=True)
    t6 = vp.text(text='Shail Patel ', pos=vp.vec(-7,-7,0),color=vp.color.cyan, billboard=True, emissive=True)

#variables used by the showat function
year = 0
day = 0
month = 0
#setting the scene
vp.scene.width = 800
vp.scene.height = 800
vp.scene.range = 1.3
vp.scene.title = "ANTIKYTHERA\n"
vp.button(text="display", bind=display, pos=vp.scene.title_anchor)
vp.scene.append_to_title('\n')
vp.button(text="display at", bind=showat, pos=vp.scene.title_anchor)
vp.scene.append_to_title('\n')
vp.button(text="Efficient Projectile estimated date", bind = projCalc, pos = vp.scene.title_anchor)
planetOne = vp.menu(pos = vp.scene.title_anchor,bind = setPlanet1,choices = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto'])
planetTwo = vp.menu(pos = vp.scene.title_anchor, bind = setPlanet2,choices =['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto'] )
vp.scene.append_to_title('\n')
vp.button(text="credits", bind=credits, pos=vp.scene.title_anchor)
vp.scene.append_to_title('\n')
eclipse = vp.winput(bind=seteclipse, pos=vp.scene.title_anchor)
vp.button(text="eclipes predictor", bind=prediction, pos=vp.scene.title_anchor)
vp.scene.append_to_title('\n')
day = vp.winput(bind=setday, pos=vp.scene.title_anchor)
month = vp.winput(bind=setmonth, pos=vp.scene.title_anchor)
year = vp.winput(bind=setyear, pos=vp.scene.title_anchor)
vp.scene.append_to_title('\n')
vp.scene.append_to_caption('\n')
vp.scene.append_to_caption('\n')
vp.scene.append_to_caption('\n')
guidate = vp.wtext(text="date")
vp.scene.append_to_caption('\n')


################################################################################
vp.scene.append_to_title('\n')
vp.scene.append_to_caption('\n')
vp.button(text="Pause", bind=Pause)
vp.button(text="Play", bind=Play)
vp.button(text="Reset", bind=Reset)
vp.scene.append_to_caption('\n')
vp.scene.append_to_caption('\n')
# makes the sun shine
vp.sphere(color=vp.color.yellow, emissive=True, radius = 1)
vp.local_light(pos=vp.vector(0, 0, 0), color=vp.color.yellow)
############## Setting body models initial values ##########################
current_date = datetime.datetime.today() # current date of the simulation
for planet in list_of_planets:
    planet.simulate_orbit(0)
    list_of_planet_models.append(vp.sphere(textures=vp.textures.earth,
                     pos=vp.vector(planet.xPos / 10000000, planet.yPos / 10000000, planet.zPos / 10000000),
                     make_trail=True, trail_type="curve", interval=10, retain=50, radius = 0.1))
    list_of_planet_names.append(vp.label(text = planet.name, pos = list_of_planet_models[list_of_planets.index(planet)].pos, height = 15, yoffset = 50, space = 30, border = 4, font = 'sans'))
for satellite in list_of_satellites:
    for planet in list_of_planets:
        if satellite.host == planet.name:
            satellite.simulate_orbit(0, planet)
            list_of_satellite_models.append(vp.sphere(textures=vp.textures.earth,
                            pos=vp.vector(satellite.xPos / 10000000, satellite.yPos / 10000000, satellite.zPos / 10000000),
                            make_trail=False, radius = 0.03))
            list_of_satellite_names.append(vp.label(text = satellite.name, pos = list_of_satellite_models[list_of_satellites.index(satellite)].pos, height = 15, yoffset = 50, space = 30, border = 4, font = 'sans'))
            break
############################################################################
vp.scene.append_to_caption('\n')
sl = vp.slider(min=-3, max=3, value=0.5, length=675, bind=setspeed)

guiday = str(current_date.day)
guimonth = str(current_date.month)
guiyear = str(current_date.year)

################################################################################

guidate = vp.wtext(text="date")
guidate.text = guiday + "/" + guimonth + "/" + guiyear

vp.scene.camera.pos = vp.vector(0, 0, 20)
