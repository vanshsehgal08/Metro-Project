import streamlit as st
from graph import delhi
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title='Metro Planner',
    page_icon='images/icon.png',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': '# Delhi Metro Planner  \n~Vansh Sehgal'
    }
)

st.sidebar.image('images/delhi_metro.png')
stations = delhi.keys()

st.markdown("<h1 style='text-align: center; color: white;'>Delhi Metro Travel Planner</h1>", unsafe_allow_html=True)
metro_map = Image.open('images/delhi_map.jpg')
st.image(metro_map)
st.markdown("<h2 style='text-align: center; color: white;'>Enter Station Names</h2>", unsafe_allow_html=True)

st.markdown(
    '''
    <style>
    [data-baseweb='select'] {
        margin-top: -30px;
    }
    [data-baseweb='textarea'] {
        margin-top: -30px;
    }
    </style>
    ''',
    unsafe_allow_html=True,
)

st.write('### Source')
source = st.selectbox('Source',stations)
st.write('### Destination')
dest = st.selectbox('Destination',stations)
        
def dfs(delhi, s, e, minlength=-1, path=[]):
  path = path + [s]
  if s == e: return path
  if s not in delhi: return None
  shortest = None
  for node in delhi[s]:
    if node not in path:
      if minlength==-1 or len(path)<(minlength-1):
        new = dfs(delhi, node, e, minlength, path)
        if new:
          if not shortest or len(new) < len(shortest):
            shortest = new
            minlength = len(new)  
  return shortest        
        
start=source
end=dest

button1 = st.button('Search Route')

if st.session_state.get('button') != True:
    st.session_state['button'] = button1

if st.session_state['button'] == True:
  path=dfs(delhi,start,end)
  output = pd.DataFrame({'Station Name' : path})
  output.index += 1
  st.write('####',start,' to ', end, 'Route : ')
  st.write(output)      
  if st.button('Return Route'):
    path.reverse()
    output2 = pd.DataFrame({'Station Name' : path})
    output2.index += 1
    st.write('####',end,' to ', start, 'Route : ')
    st.write(output2)
    st.session_state['button'] = False
