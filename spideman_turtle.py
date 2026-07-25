# spiderman_turtle.py
# A stylized Spider-Man mask drawn with turtle graphics
import turtle
turtle.tracer(0)
t = turtle.Turtle()
turtle.update
import math

screen = turtle.Screen()
screen.title("Spider-Man Mask (Turtle)")
screen.setup(width=700, height=700)
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

# helper: move without drawing
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# draw filled circle for head
def draw_head(radius=200):
    t.color("black", "#d81b1b")   # outline black, fill spidey-red
    t.penup()
    t.goto(0, -radius)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# draw stylized eye - uses an arc technique to form a white almond
def draw_eye(cx, cy, scale=1.0, flip=False):
    # Parameters control the almond shape using two arcs
    w = 70 * scale
    h = 120 * scale
    t.penup()
    # start a bit left of center of eye
    start_x = cx - w/2
    start_y = cy
    t.goto(start_x, start_y)
    t.setheading(0)
    t.pendown()
    t.color("black", "white")
    t.begin_fill()
    # top arc (approximate)
    for i in range(60):
        angle = math.radians(i * (180/59))
        x = cx + (w/2) * math.cos(angle)
        y = cy + (h/2) * math.sin(angle)
        if flip:
            x = 2*cx - x
        if i == 0:
            t.goto(x, y)
        else:
            t.goto(x, y)
    # bottom arc (backwards)
    for i in range(60):
        angle = math.radians(180 - i * (180/59))
        x = cx + (w/2) * math.cos(angle)
        y = cy + (h/3) * math.sin(angle) - 18*scale  # lower curvature
        if flip:
            x = 2*cx - x
        t.goto(x, y)
    t.end_fill()
    # outline
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.color("black")
    t.pensize(2)
    for i in range(120):
        angle = math.radians(i * (360/119))
        x = cx + (w/2) * math.cos(angle)
        y = cy + (h/2) * math.sin(angle)
        if flip:
            x = 2*cx - x
        if i == 0:
            t.penup(); t.goto(x,y); t.pendown()
        else:
            t.goto(x,y)
    t.pensize(2)

# draw radial web lines from a point near top-center
def draw_web(center_x=0, center_y=80, radius=180, spokes=14):
    t.color("black")
    t.pensize(2)
    for i in range(spokes):
        ang = 180 - (i * (360 / spokes))
        # convert to radians, compute end
        rad = math.radians(ang)
        ex = center_x + radius * math.cos(rad)
        ey = center_y + radius * math.sin(rad)
        move(center_x, center_y)
        t.setheading(0)
        t.goto(ex, ey)

# draw concentric curved web "rings" using bezier-like points (approx)
def draw_web_rings(center_x=0, center_y=80, rings=6):
    t.color("black")
    t.pensize(2)
    for r in range(1, rings + 1):
        rr = 30 * r + 20
        # draw an oval-ish curve across face
        t.penup()
        t.goto(center_x - rr, center_y - 10*r)
        t.pendown()
        for angle in range(0, 181, 2):
            rad = math.radians(angle)
            # elliptical parametric, squash y to make it mask-fitting
            x = center_x + rr * math.cos(rad)
            y = center_y + (rr * 0.6) * math.sin(rad) - 10*r
            t.goto(x, y)

# small inner web details connecting radial lines to rings
def draw_web_detail(center_x=0, center_y=80, radius=180, spokes=14, rings=6):
    t.color("black")
    t.pensize(1.5)
    # sample points along radial spokes, draw small connecting arcs between spokes
    for ring in range(1, rings + 1):
        rr = 30 * ring + 20
        points = []
        for i in range(spokes):
            ang = math.radians(180 - i * (360 / spokes))
            x = center_x + rr * math.cos(ang)
            y = center_y + (rr * 0.6) * math.sin(ang) - 10*ring
            points.append((x, y))
        # draw small curve connecting every Nth point to make web look organic
        for i in range(len(points)-1):
            move(points[i][0], points[i][1])
            t.goto(points[i+1][0], points[i+1][1])

# Draw everything (order matters)
t.tracer(False)  # speed up drawing
draw_head(radius=200)
draw_web(center_x=0, center_y=80, radius=190, spokes=16)
draw_web_rings(center_x=0, center_y=80, rings=6)
draw_web_detail(center_x=0, center_y=80, radius=190, spokes=16, rings=6)
# Eyes (left and right)
draw_eye(-60, 30, scale=1.2, flip=False)
draw_eye(60, 30, scale=1.2, flip=True)
t.tracer(True)

# finish
move(0, -260)
t.color("black")
t.write("Spider-Man mask (stylized) — turtle graphics", align="center", font=("Arial", 12, "normal"))
t.hideturtle()

# Keep window open until closed
turtle.done()
