from PIL import Image
import webcolors

'''
taking input along lines
'''

# striping surrounding white pixels

'''
im=Image.open('output.png')

pixels=im.load()

im1=Image.new('RGB',(100,30))
pixy=im1.load()

for i in range(2,32):
	for j in range(2,102):
		pixy[j-2,i-2]=pixels[j,i]

im1.save('better.png')
'''

colour={"B":(0,0,0),
"W":(255,255,255),
"G":(128,128,128),
"r":(255,0,0),
"g":(0,255,0),
"b":(0,0,255),
"y":(255,255,0),
"c":(0,255,255),
"m":(255,0,255)
}

a=[colour["m"],colour["r"],colour["g"],colour["y"],colour["b"],colour["c"]]
b=[colour["r"],colour["m"],colour["g"],colour["y"],colour["b"],colour["c"]]
c=[colour["r"],colour["g"],colour["m"],colour["y"],colour["b"],colour["c"]]
d=[colour["r"],colour["g"],colour["y"],colour["m"],colour["b"],colour["c"]]
e=[colour["r"],colour["g"],colour["y"],colour["b"],colour["m"],colour["c"]]
f=[colour["r"],colour["g"],colour["y"],colour["b"],colour["c"],colour["m"]]
g=[colour["g"],colour["r"],colour["y"],colour["b"],colour["c"],colour["m"]]
h=[colour["g"],colour["y"],colour["r"],colour["b"],colour["c"],colour["m"]]
i=[colour["g"],colour["y"],colour["b"],colour["r"],colour["c"],colour["m"]]
j=[colour["g"],colour["y"],colour["b"],colour["c"],colour["r"],colour["m"]]
k=[colour["g"],colour["y"],colour["b"],colour["c"],colour["m"],colour["r"]]
l=[colour["y"],colour["g"],colour["b"],colour["c"],colour["m"],colour["r"]]
m=[colour["y"],colour["b"],colour["g"],colour["c"],colour["m"],colour["r"]]
n=[colour["y"],colour["b"],colour["c"],colour["g"],colour["m"],colour["r"]]
o=[colour["y"],colour["b"],colour["c"],colour["m"],colour["g"],colour["r"]]
p=[colour["y"],colour["b"],colour["c"],colour["m"],colour["r"],colour["g"]]
q=[colour["b"],colour["y"],colour["c"],colour["m"],colour["r"],colour["g"]]
r=[colour["b"],colour["c"],colour["y"],colour["m"],colour["r"],colour["g"]]
s=[colour["b"],colour["c"],colour["m"],colour["y"],colour["r"],colour["g"]]
t=[colour["b"],colour["c"],colour["m"],colour["r"],colour["y"],colour["g"]]
u=[colour["b"],colour["c"],colour["m"],colour["r"],colour["g"],colour["y"]]
v=[colour["c"],colour["b"],colour["m"],colour["r"],colour["g"],colour["y"]]
w=[colour["c"],colour["m"],colour["b"],colour["r"],colour["g"],colour["y"]]
x=[colour["c"],colour["m"],colour["r"],colour["b"],colour["g"],colour["y"]]
y=[colour["c"],colour["m"],colour["r"],colour["g"],colour["b"],colour["y"]]
z=[colour["c"],colour["m"],colour["r"],colour["g"],colour["y"],colour["b"]]

A0=[colour["B"],colour["G"],colour["W"],colour["B"],colour["G"],colour["W"]]
A1=[colour["G"],colour["B"],colour["W"],colour["B"],colour["G"],colour["W"]]
A2=[colour["G"],colour["W"],colour["B"],colour["B"],colour["G"],colour["W"]]
A3=[colour["G"],colour["W"],colour["B"],colour["G"],colour["B"],colour["W"]]
A4=[colour["G"],colour["W"],colour["B"],colour["G"],colour["W"],colour["B"]]
A5=[colour["W"],colour["G"],colour["B"],colour["G"],colour["W"],colour["B"]]
A6=[colour["W"],colour["B"],colour["G"],colour["G"],colour["W"],colour["B"]]
A7=[colour["W"],colour["B"],colour["G"],colour["W"],colour["G"],colour["B"]]
A8=[colour["W"],colour["B"],colour["G"],colour["W"],colour["B"],colour["G"]]
A9=[colour["B"],colour["W"],colour["G"],colour["W"],colour["B"],colour["G"]]
space=[colour["W"],colour["W"],colour["W"],colour["W"],colour["W"],colour["W"]]
space2=[colour["B"],colour["B"],colour["B"],colour["B"],colour["B"],colour["B"]]
comma=[colour["W"],colour["B"],colour["B"],colour["W"],colour["W"],colour["B"]]
period=[colour["B"],colour["W"],colour["W"],colour["B"],colour["B"],colour["W"]]

letters={'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,'y':y,'z':z,'0':A0,'1':A1,'2':A2,'3':A3,'4':A4,'5':A5,'6':A6,'7':A7,'8':A8,'9':A9,' ':space,',':comma,'.':period}


im=Image.open("frame002.png")
pixels=im.load()

#print(im.size,im.height)

#main code... 
hexhue=[]

print(im.height)
print(im.width)
# print(webcolors.rgb_to_name(pixels[0,0]))
# print(pixels[140,0])
# print(pixels[0,100])
# print(pixels[140,100])
# print(pixels[0,200])
# print(pixels[140,200])

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css21_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

requested_colour = (247, 247, 76)
actual_name, closest_name = get_colour_name(requested_colour)
print(closest_name)