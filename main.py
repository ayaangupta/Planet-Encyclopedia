from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Planet App")
root.geometry("600x700")
root.config(bg="midnightblue")

ceres = ImageTk.PhotoImage(Image.open("ceres.jpeg"))
h1 = Image.open("haumea.jpg")
h2 = h1.resize((225, 225))
haumea = ImageTk.PhotoImage(h2)
j1 = Image.open("jupiter.jpg")
j2 = j1.resize((225, 225))
jupiter = ImageTk.PhotoImage(j2)
makemake = ImageTk.PhotoImage(Image.open("makemake.jpg"))
mars = ImageTk.PhotoImage(Image.open("mars.jpeg"))
mercury = ImageTk.PhotoImage(Image.open("mercury.jpg"))
n1 = Image.open("neptune.jpg")
n2 = n1.resize((375, 225))
neptune = ImageTk.PhotoImage(n2)
pluto = ImageTk.PhotoImage(Image.open("pluto.jpeg"))
saturn = ImageTk.PhotoImage(Image.open("saturn.jpeg"))
sun = ImageTk.PhotoImage(Image.open("Sun.jpeg"))
u1 = Image.open("uranus.jpg")
u2 = u1.resize((225, 225))
uranus = ImageTk.PhotoImage(u2)
v1 = Image.open("venus.jpg")
v2 = v1.resize((225, 225))
venus = ImageTk.PhotoImage(v2)
earth = ImageTk.PhotoImage(Image.open("earth.jpeg"))
eris = ImageTk.PhotoImage(Image.open("eris.jpeg"))

planets = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Ceres", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Makemake", "Haumea", "Eris"]

selectedval = StringVar()

dropdown = ttk.Combobox(root, values=planets, textvariable=selectedval)
dropdown.place(relx=0.5, rely=0.1, anchor=CENTER)

def planet_info():
    planet=selectedval.get()
    if planet=="Sun":
        label_planet_name['text'] = "Sun"
        label_planet_image['image'] = sun
        label_planet_gravity['text'] = "274 m/s²"
        label_planet_info['text'] = "The Sun has been called by many names. The Latin word for Sun is sol, which is the main adjective for all things Sun-related: solar. Helios, the Sun god in ancient Greek mythology, lends his name to many Sun-related terms as well, such as heliosphere and helioseismology. Our Sun is a medium-sized star with a radius of about 435,000 miles (700,000 kilometers). Many stars are much larger but the Sun is far more massive than our home planet: it would take more than 330,000 Earths to match the mass of the Sun, and it would take 1.3 million Earths to fill the Sun's volume."
        label_planet_away_sun['text'] = "0km Away from the Sun (In Million km)"
        label_planet_type['text'] = "Type: Star"

    if planet=="Mercury":
        label_planet_name['text'] = "Mercury"
        label_planet_image['image'] = mercury
        label_planet_gravity["text"] = "3.7 m/s²"
        label_planet_info['text'] = "Mercury is the smallest planet in our solar system and the nearest to the Sun.Mercury is only slightly larger than Earth's Moon. Its surface is covered in tens of thousands of impact craters. Despite its proximity to the Sun, Mercury is not the hottest planet in our solar system that title belongs to nearby Venus, thanks to its dense atmosphere. But Mercury is the fastest planet, zipping around the Sun every 88 Earth days. Mercury is appropriately named for the swiftest of the ancient Roman gods."
        label_planet_away_sun['text'] = "59.276km Away from the Sun (In Million km)"
        label_planet_type['text'] = "Type: Planet"

    if planet=="Venus":
        label_planet_name['text'] = "Venus"
        label_planet_image['image'] = venus
        label_planet_gravity["text"] = "8.87 m/s²"
        label_planet_info['text'] = "Venus is the second planet from the Sun, and the sixth largest planet. Its the hottest planet in our solar system.Venus is a cloud-swaddled planet named for a love goddess, and often called Earths twin. But pull up a bit closer, and Venus turns hellish. Our nearest planetary neighbor, the second planet from the Sun, has a surface hot enough to melt lead. The atmosphere is so thick that, from the surface, the Sun is just a smear of light."
        label_planet_away_sun['text'] = "108.7km Away from the Sun (In Million km)"
        label_planet_type['text'] = "Type: Planet"

    if planet=="Earth":
        label_planet_name['text'] = "Earth"
        label_planet_image['image'] = earth
        label_planet_gravity["text"] = "9.807 m/s²"
        label_planet_info['text'] = "While Earth is only the fifth largest planet in the solar system, it is the only world in our solar system with liquid water on the surface. Just slightly larger than nearby Venus, Earth is the biggest of the four planets closest to the Sun, all of which are made of rock and metal. Earth is the only planet in the solar system whose English name does not come from Greek or Roman mythology. The name was taken from Old English and Germanic. It simply means 'the ground.' There are, of course, many names for our planet in the thousands of languages spoken by the people of the third planet from the Sun."
        label_planet_away_sun['text'] = "149.8km Away from the Sun (In Million km)"
        label_planet_type['text'] = "Type: Planet"

    if planet=="Mars":
        label_planet_name['text'] = "Mars"
        label_planet_image['image'] = mars
        label_planet_gravity["text"] = "3.71 m/s²"
        label_planet_info['text'] = "Mars is the fourth planet from the Sun, and the seventh largest. Its the only planet we know of inhabited entirely by robots. Mars is no place for the faint-hearted. Its dry, rocky, and bitter cold. The fourth planet from the Sun, Mars, is one of Earth's two closest planetary neighbors (Venus is the other). Mars is one of the easiest planets to spot in the night sky — it looks like a bright red point of light."   
        label_planet_away_sun['text'] = "226.03km Away from the Sun (In Million km)" 
        label_planet_type['text'] = "Type: Planet"

    if planet=="Jupiter":
        label_planet_name['text'] = "Jupiter"
        label_planet_image['image'] = jupiter
        label_planet_gravity["text"] = "24.79 m/s²"
        label_planet_info['text'] = "Jupiter is the largest planet in our solar system. If Jupiter was a hollow shell, 1,000 Earths could fit inside. Jupiter also is the oldest planet, forming from the dust and gases left over from the Sun's formation 4.5 billion years ago. But it has the shortest day in the solar system, taking only 10.5 hours to spin around once on its axis."
        label_planet_away_sun['text'] = "755.6km Away from the Sun (In Million km)"
        label_planet_type['text'] = "Type: Planet"

    if planet=="Saturn":
        label_planet_name['text'] = "Saturn"
        label_planet_image['image'] = saturn
        label_planet_gravity["text"] = "10.44 m/s²"
        label_planet_info['text'] = "Saturn is the sixth planet from the Sun and the second largest planet in our solar system. Adorned with a dazzling system of icy rings, Saturn is unique among the planets. Saturn is a massive ball made mostly of hydrogen and helium. The farthest planet from Earth discovered by the unaided human eye, Saturn has been known since ancient times. The planet is named for the Roman god of agriculture and wealth, who was also the father of Jupiter."   
        label_planet_away_sun['text'] = "1.4439km Away from the Sun (In Billion km)"
        label_planet_type['text'] = "Type: Planet"

    if planet=="Uranus":
        label_planet_name['text'] = "Uranus"
        label_planet_image['image'] = uranus
        label_planet_gravity["text"] = "8.87 m/s²"
        label_planet_info['text'] = "Uranus is the seventh planet from the Sun, and it's the third largest planet in our solar system about four times wider than Earth. Uranus is a very cold and windy planet. It is surrounded by faint rings, and more than two dozen small moons as it rotates at a nearly 90-degree angle from the plane of its orbit. This unique tilt makes Uranus appear to spin on its side. Uranus is blue-green in color due to large amounts of methane, which absorbs red light but allows blues to be reflected back into space."
        label_planet_away_sun['text'] = "2.9263km Away from the Sun (In Billion km)"
        label_planet_type['text'] = "Type: Planet"

    if planet=="Neptune":
        label_planet_name['text'] = "Neptune"
        label_planet_image['image'] = neptune
        label_planet_gravity["text"] = "11.15 m/s²"
        label_planet_info['text'] = "Dark, cold and whipped by supersonic winds, giant Neptune is the eighth and most distant major planet orbiting our Sun. More than 30 times as far from the Sun as Earth, Neptune is not visible to the naked eye. The planets blue color comes from methane in its atmosphere, which absorbs red wavelengths of light, but allows blue ones to be reflected back into space very much like its neighbor, Uranus. Neptune was the first planet located using math. German astronomer Johann Galle was the first to observe the planet in 1846. The planet is named after the Roman god of the sea."  
        label_planet_away_sun['text'] = "4.4717km Away from the Sun (In Billion km)"  
        label_planet_type['text'] = "Type: Planet" 

    if planet=="Ceres":
        label_planet_name['text'] = "Ceres"
        label_planet_image['image'] = ceres
        label_planet_gravity["text"] = "0.72 m/s²"
        label_planet_info['text'] = "Dwarf planet Ceres is the largest object in the asteroid belt between Mars and Jupiter, and it's the only dwarf planet located in the inner solar system. It was the first member of the asteroid belt to be discovered when Giuseppe Piazzi spotted it in 1801. When NASA's Dawn arrived in 2015, Ceres became the first dwarf planet to be explored by a spacecraft. Called an asteroid for many years, Ceres is so much bigger and so different from its rocky neighbors that scientists classified it as a dwarf planet in 2006. Even though Ceres comprises 25% of the asteroid belt's total mass, Pluto is still 14 times more massive. Ceres is named for the Roman goddess of corn and harvests. The word cereal comes from the same name." 
        label_planet_away_sun['text'] = "413km Away from the Sun (In Million km)"  
        label_planet_type['text'] = "Type: Dwarf Planet"     

    if planet=="Pluto":
        label_planet_name['text'] = "Pluto"
        label_planet_image['image'] = pluto
        label_planet_gravity["text"] = "0.62 m/s²"
        label_planet_info['text'] = "Pluto is a dwarf planet located in a distant region of our solar system beyond Neptune known as the Kuiper Belt. Pluto was long considered our ninth planet, but the International Astronomical Union reclassified Pluto as a dwarf planet in 2006. NASA's New Horizons was the first spacecraft to explore Pluto up close, flying by in 2015. Pluto was discovered in 1930 by astronomer Clyde Tombaugh. It was named by 11-year-old Venetia Burney of Oxford, England."
        label_planet_away_sun['text'] = "5.9km Away from the Sun (In Billion km)"
        label_planet_type['text'] = "Type: Dwarf Planet" 

    if planet=="Haumea":
        label_planet_name['text'] = "Haumea"
        label_planet_image['image'] = haumea
        label_planet_gravity["text"] = "0.401 m/s²"
        label_planet_info['text'] = "Dwarf planet Haumea was originally designated 2003 EL61 (and nicknamed Santa by one discovery team). Haumea is located in the Kuiper Belt, a doughnut-shaped region of icy bodies beyond the orbit of Neptune. Haumea is an oval-shaped dwarf planet that is one of the fastest rotating large objects in our solar system. The fast spin distorts Haumea's shape, making this dwarf planet look like a football."  
        label_planet_away_sun['text'] = "6.5km Away from the Sun (In Billion km)"   
        label_planet_type['text'] = "Type: Dwarf Planet"   

    if planet=="Makemake":
        label_planet_name['text'] = "Makemake"
        label_planet_image['image'] = makemake
        label_planet_gravity["text"] = "0.5 m/s²"
        label_planet_info['text'] = "Dwarf planet Makemake along with Pluto, Haumea, and Eris is located in the Kuiper Belt, a donut-shaped region of icy bodies beyond the orbit of Neptune. Makemake is slightly smaller than Pluto, and is the second-brightest object in the Kuiper Belt as seen from Earth while Pluto is the brightest. It takes about 305 Earth years for this dwarf planet to make one trip around the Sun. Makemake holds an important place in the history of solar system studies because it was one of the objects along with Eris whose discovery prompted the International Astronomical Union to reconsider the definition of a planet, and to create the new group of dwarf planets."  
        label_planet_away_sun['text'] = "6.847km Away from the Sun (In Billion km)" 
        label_planet_type['text'] = "Type: Dwarf Planet" 

    if planet=="Eris":
        label_planet_name['text'] = "Eris"
        label_planet_image['image'] = eris
        label_planet_gravity["text"] = "0.82 m/s²"
        label_planet_info['text'] = "Eris is one of largest the dwarf planets in our solar system. It's about the same size as Pluto, but it's three times farther from the Sun. The discovery of Eris help trigger a debate in the scientific community that led to the International Astronomical Union's decision in 2006 to clarify the definition of a planet. Pluto, Eris, and other similar objects are now classified as dwarf planets. Eris was discovered on Jan. 5, 2005, from data obtained on Oct. 21, 2003, during a Palomar Observatory survey of the outer solar system by Mike Brown, a professor of planetary astronomy at the California Institute of Technology; Chad Trujillo of the Gemini Observatory; and David Rabinowitz of Yale University." 
        label_planet_away_sun['text'] = "10km Away from the Sun (In Billion km)"  
        label_planet_type['text'] = "Type: Dwarf Planet"  

button = Button(root, text="Press this button to show planet info", bg="paleturquoise", command=planet_info)
button.place(relx=0.5, rely=0.15, anchor=CENTER)

label_title = Label(root,text="Solar System Encyclopedia", bg="paleturquoise")
label_title.place(relx=0.2, rely=0.1, anchor=CENTER)

label_info = Label(root, text="m/s² is the same as metres divided by seconds squared", bg="paleturquoise")
label_info.place(relx=0.85, rely=0.1, anchor=CENTER)

label_planet_name = Label(root,text="", bg="paleturquoise")
label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)

label_planet_image = Label(root,bg="paleturquoise")
label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)

label_planet_gravity = Label(root, bg="paleturquoise")
label_planet_gravity.place(relx=0.5, rely=0.8, anchor=CENTER)

label_planet_info = Label(root, bg="paleturquoise", wrap=700)
label_planet_info.place(relx= 0.5, rely=0.9, anchor=CENTER)

label_planet_away_sun = Label(root, bg="paleturquoise")
label_planet_away_sun.place(relx=0.5, rely=0.7, anchor=CENTER)

label_dropdown_info = Label(root, bg="paleturquoise")
label_dropdown_info.place(relx=0.5, rely=0.05, anchor=CENTER)
label_dropdown_info['text'] = "The Dropdown Is In Order Of Which Planets Are Closest To The Sun"

label_planet_type = Label(root, bg="paleturquoise")
label_planet_type.place(relx=0.5, rely=0.2, anchor=CENTER)

root.mainloop()