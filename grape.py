
x0_grape = -1.4569724 
dx_grape = 8.5430296 + 1.4569724
y0_grape = -5.3048957
dy_grape = 4.6951043 + 5.3048957

grape_template = """
    <g
       id="grape{serialnum}"
       transform="matrix(0.17486025,0,0,0.17074389,{xpos},{ypos})"
       style="stroke:none;stroke-width:5.78735">
	  <title>{name}</title> 
      <ellipse
         style="fill:#{color};stroke:none;stroke-width:11.5748"
         id="path846-7"
         cx="59.757355"
         cy="90.330879"
         rx="22.830881"
         ry="29.97794" />
      <ellipse
         style="fill:#ffffff;fill-opacity:0.794486;stroke:none;stroke-width:11.5749;stroke-opacity:1"
         id="path870-9"
         cx="76.624405"
         cy="59.023647"
         rx="9.7650099"
         ry="16.275019"
         transform="rotate(19.481064)" />
      <ellipse
         style="fill:#ffffff;fill-opacity:0.794486;stroke:none;stroke-width:11.5749;stroke-opacity:1"
         id="path870-4-5"
         cx="74.7714"
         cy="58.378075"
         rx="5.9555278"
         ry="9.9258804"
         transform="rotate(19.481064)" />
    </g>
"""

svg_header = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>

"""

svg_prefix = """
<svg
   width="48mm"
   height="48mm"
   viewBox="0 0 48 48"
   version="1.1"
   id="svg5"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <defs
     id="defs2" />
  <g
     id="layer1">
"""

svg_suffix = """
  </g>
</svg>
"""

def make_grape(serialnum, name, color, xpos, ypos):
    svg = ( grape_template.replace("{serialnum}",str(serialnum)) 
      .replace("{name}",str(name))
      .replace("{color}","%02x%02x%02x"%color)
      .replace("{xpos}", str(x0_grape+xpos*dx_grape+ypos*dx_grape/2))
      .replace("{ypos}", str(y0_grape+ypos*dy_grape))
      )
    return svg  
    
def make_bunch(color_struct, name_pool=[]):
    svg = ""
    i = 0
    y_pos = 0
    name = "name"
    for k in color_struct:
      x_pos = 0
      for c in k:
        if name_pool: name = name_pool.pop(0)
        svg += make_grape(i,name,c,x_pos,y_pos)
        i +=1
        x_pos +=1
      y_pos +=1
    return svg_prefix + svg + svg_suffix

def lerp(a,b,t):
  return a*(1-t)+b*t
  
def ilerp(a,b,t):
  return int(lerp(a,b,t))
  
def clerp(a,b,t):
  return tuple(ilerp(aa,bb,t) for aa, bb in zip(a,b))

def color_scale(value):
    if value <0.5 :
      color = clerp((255,200,0),(0,255,0),2*value)
    else:
      color = clerp((0,255,0),(156,0,255),2*value-1)
    return color


def grape(df, column_struct):
    color_struct = [[color_scale(df[c].mean()) for c in k] for k in column_struct]
    names = [c for k in column_struct for c in k]
    return make_bunch(color_struct,names)    
