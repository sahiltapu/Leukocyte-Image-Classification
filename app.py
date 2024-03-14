import streamlit as st





st.set_page_config(layout="wide")
css = """
<style>
    .container {
        display: flex;
        flex-direction: row;
        align-items: center;
        margin: 10px;  /* Adjust margins as needed */
        gap:20px;
    }
    .image {
        flex: 0 0 200px;  /* Set fixed width for image */
        margin-right: 10px;  /* Adjust spacing between image and text */
    }
    @media (width <= 1024px){
        .image{
            display:none;
        }
      
    }
    .scale-in-top {
	-webkit-animation: scale-in-top 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
	        animation: scale-in-top 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
}
@-webkit-keyframes scale-in-top {
  0% {
    -webkit-transform: scale(0);
            transform: scale(0);
    -webkit-transform-origin: 50% 0%;
            transform-origin: 50% 0%;
    opacity: 1;
  }
  100% {
    -webkit-transform: scale(1);
            transform: scale(1);
    -webkit-transform-origin: 50% 0%;
            transform-origin: 50% 0%;
    opacity: 1;
  }
}
@keyframes scale-in-top {
  0% {
    -webkit-transform: scale(0);
            transform: scale(0);
    -webkit-transform-origin: 50% 0%;
            transform-origin: 50% 0%;
    opacity: 1;
  }
  100% {
    -webkit-transform: scale(1);
            transform: scale(1);
    -webkit-transform-origin: 50% 0%;
            transform-origin: 50% 0%;
    opacity: 1;
  }
}
.scale-in-left {
	-webkit-animation: scale-in-left 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
	        animation: scale-in-left 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
}
@-webkit-keyframes scale-in-left {
  0% {
    -webkit-transform: scale(0);
            transform: scale(0);
    -webkit-transform-origin: 0% 50%;
            transform-origin: 0% 50%;
    opacity: 1;
  }
  100% {
    -webkit-transform: scale(1);
            transform: scale(1);
    -webkit-transform-origin: 0% 50%;
            transform-origin: 0% 50%;
    opacity: 1;
  }
}
@keyframes scale-in-left {
  0% {
    -webkit-transform: scale(0);
            transform: scale(0);
    -webkit-transform-origin: 0% 50%;
            transform-origin: 0% 50%;
    opacity: 1;
  }
  100% {
    -webkit-transform: scale(1);
            transform: scale(1);
    -webkit-transform-origin: 0% 50%;
            transform-origin: 0% 50%;
    opacity: 1;
  }
}
.scale-in-right {
	-webkit-animation: scale-in-right 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
	        animation: scale-in-right 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
}

@-webkit-keyframes scale-in-right {
  0% {
    -webkit-transform: scale(0);
            transform: scale(0);
    -webkit-transform-origin: 100% 50%;
            transform-origin: 100% 50%;
    opacity: 1;
  }
  100% {
    -webkit-transform: scale(1);
            transform: scale(1);
    -webkit-transform-origin: 100% 50%;
            transform-origin: 100% 50%;
    opacity: 1;
  }
}
@keyframes scale-in-right {
  0% {
    -webkit-transform: scale(0);
            transform: scale(0);
    -webkit-transform-origin: 100% 50%;
            transform-origin: 100% 50%;
    opacity: 1;
  }
  100% {
    -webkit-transform: scale(1);
            transform: scale(1);
    -webkit-transform-origin: 100% 50%;
            transform-origin: 100% 50%;
    opacity: 1;
  }
}

}

</style>
"""
st.markdown("""<h1 class="scale-in-top " style='text-align: start; color: #67C6E3;'>What are Leukocytes !!</h1>""",unsafe_allow_html = True)

st.markdown(css, unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div class="container">
        <img class="image scale-in-left" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQY3-8Sam0tIPX6uCKnDj0ZceULu_Cec07CfYhOqODa1r93UoMF1XAnxqCEwlxKrMFtFYw&usqp=CAU" alt="Image description">  
    <p class="scale-in-right">Leukocytes, commonly known as white blood cells, are a crucial
        component of the human immune system, playing a vital role in defending the body against infections, 
        pathogens, and foreign substances. These specialized cells are produced in the bone marrow and circulate throughout 
        the bloodstream, patrolling the body to identify and neutralize potential threats.</p>
    
    
    </div>
    """, unsafe_allow_html=True)


st.markdown("""<h1 class="scale-in-left " style='text-align: start; color: #67C6E3;'>Types - </h1>""",unsafe_allow_html = True)
st.markdown("""
            <p class="scale-in-left"> <strong>Neutrophils:</strong>
Neutrophils are the most abundant type of white blood cells and are often the first responders to infection.
They are highly effective at engulfing and digesting bacteria and other microbes.
Neutrophils have a short lifespan and are typically the first cells to arrive at the site of infection.
<br />
<br />
<strong>Lymphocytes:</strong>
Lymphocytes are responsible for the body's adaptive immune response.
There are two main types of lymphocytes: B cells and T cells.
B cells produce antibodies, proteins that recognize and neutralize specific pathogens.
T cells have various functions, including the destruction of infected cells and the coordination of the immune response.
<br />
<br />
<strong>Monocytes:</strong>
Monocytes are larger white blood cells that circulate in the bloodstream before entering tissues and differentiating into macrophages or dendritic cells.
Macrophages are phagocytic cells that engulf and digest pathogens and cellular debris.
Dendritic cells play a crucial role in presenting antigens to T cells, initiating an immune response.
<br />
<br />
<strong>Eosinophils:</strong>
Eosinophils are involved in the immune response against parasites and are also implicated in allergic reactions.
They release substances that help combat parasites and modulate the inflammatory response.
<br />
<br />
<strong>Basophils:</strong>
Basophils are involved in allergic reactions and the inflammatory response.
They release histamine, a chemical that contributes to the dilation of blood vessels and increased permeability, promoting the influx of other immune cells to the site of infection.</p>""",unsafe_allow_html= True )
