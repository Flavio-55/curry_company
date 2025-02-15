import streamlit as st
from PIL import Image

st.set_page_config( page_title="Home",layout='wide')

#image_path = 'logo_alvo_1.jpg'
image = Image.open( 'logo_alvo_1.jpg' )
st.sidebar.image( image, width=300 )

st.sidebar.markdown( '# Cury Company' )
st.sidebar.markdown( '## Fastest Delivery in Town' )
st.sidebar.markdown( """---""" )

st.write( "# Curry Company Growth Dashboard")

st.markdown(

"""Growth Dashboard foi construído para acompanhar as métricas de crescimento dos Entregadores e Restaurantes.
### Como utilizar esse Growth Dashboard?
- Visão Empresa:
    - Visão Gerencial: Métricas gerais de comportamento.
    - Visão Tática: Indicadores semanais de crescimento.
    - Visão Geográfica: Insights de geolocalização.
- Visão Entregador:
    - Acompanhamentodos indicadores semanais de crescimento.
- Visão Restaurante:
    - Indicadores semanais de crescimento dos restaurantes
### Ask for Help
- Time de Data Science no Discord
        - @ ...

""")
