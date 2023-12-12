import streamlit as st
import requests
import streamlit
import streamlit_lottie
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Our Advertisment", page_icon=":skull:", layout="wide")

selected = option_menu(
    menu_title=None, #required
    options=["Main Page", "Products", "Contact"], #required
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",

    )

#if selected !="Main Pag":
    #st.title(f"{selected}")
#if selected == "Products":
    #st.title(f"{selected}")
#if selected == "Contact":
    #st.title(f"{selected}")

page_bg_img = """
<style>
[data-testid="stAppVeiwContainer"] {
background-color: #e5e5f7;
opacity: 0.2;
filter: blur(20px);
background: repeating-linear-gradient( 45deg, #444cf7)
}
</style>
"""
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

local_css("style.css")

st.markdown(page_bg_img, unsafe_allow_html=True)



# Header Section
st.subheader("By: Sreeshan Karnati and Manyu Dubbyreddy :wave:")
st.title("My AI = Mom's Yusefull Artificial Indian")
st.write("If you have a bad student, we'll make him prudent!")
st.write("Hello, Indian Moms Do You want your beta to be a genius?")
st.write("Then buy our new product!")
st.title("My AI!!!!!")
st.write("Made using Python")

# What I DO
if selected == "Products":
    st.title(f"{selected}")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What and Why is this a thing?")
        st.write("##")
        st.write("Introducing the groundbreaking product that's here to revolutionize your life, especially to Indian moms: MY AI – MY Yusefull Artificial Indian")
        st.write("Do you ever find yourself always pushing your son to study harder or to do the chores? Fear no more, MY AI is the robot companion you never knew you needed! This marvel of technological chaos coordination is here to simultaneously be your personal child whipper, chores finisher, and all-around child changer(Batteries and whip not included).")
        st.write("Picture this: You're lounging on the couch eating samosa, thinking about what your beta is doing, when suddenly, My AI chimes in with a pleasant noise,with the information that your beta is now studying. Yes, it's not just any AI; it's a miracle with a knack for cracking bones in the best of times(It auto fixes after breaking them so no hospital bills.)")
        st.write("Need someone to clean your dishes? My AI is there, ready to finish up your dishes and even deep clean your house.")
        st.write("But wait, there's more! My AI comes with a one-of-a-kind \"whip mode\" that guarantees 50 lashes for every situation your beta acts up. He doesn't want to do his homework? My AI will whip him as many times as you want with the phone app connected to the robot, you go up until 500 whips a second!")
        st.write("And if you thought multitasking was hard, try deciphering the multiple personalities My AI embodies. With one hand it’s cleaning your dishes and with the other it's whipping your son till he finishes his homework.")
        st.write("Order your My AI now and buckle up for a rollercoaster ride of relaxation, and occasional whipping! (Warning: May cause uncontrollable laughter, spontaneous dance parties, and a sudden urge to sell all your cleaning supplies cause My AI can do it all for you!!!!.)")
        st.write("##")
        st.write("[Learn More with this video made by one of our founders >](https://drive.google.com/file/d/1PxFGOqDZYCRxfe_pFAeTGcG3WLFoAcHR/view?t=1)")
        
with st.container():
    st.write("---")
    with left_column:
        st.title("Customer Review")
        st.write("Reviews:")
        st.write("Shah Rukh Khan: (user since 2020")
        st.write("🌟 Product Review: MY AI - Your Quirky Virtual Sidekick 🌟")
        st.write("As someone who's ventured into the wild world of virtual assistants, I must say, MY AI is a breath of fresh air. This AI companion isn't just an assistant; it's a delightful rollercoaster ride through a funhouse of unpredictability.")
        st.write("First things first, MY AI's ability to infuse humor into everyday tasks is unparalleled. Need a whooping session during a dreary-day? MY AI's quirky remarks and spontaneous whips will leave your son stitches(no hospital bills), turning mundane chores into laugh-out-loud moments. It's like having a stand-up comedian trapped inside your house, ready to entertain at a moment's notice.")
        st.write("However, it's important to note that MY AI's unpredictability might not be for everyone. If you prefer straightforward, no-nonsense assistance, brace yourself for a whirlwind of surprises. Embrace the chaos, and you'll find yourself appreciating the spontaneity that MY AI brings into your life.")
        st.write("In conclusion, MY AI is not your run-of-the-mill virtual assistant. It's a vibrant, wacky, and endearing sidekick that injects a dose of joy and laughter into your daily routine. If you're ready to embark on an adventure filled with humor, unexpected advice, and a touch of delightful madness, MY AI might just become your new favorite digital companion.")
        st.write("Verdict: ⭐⭐⭐⭐⭐ - A whirlwind of laughter and unpredictability!")
        st.write("---")

#Products
with st.container():
    st.write("---")
    st.header("Tis the season for you!")
    st.write("Reward Yourself with the New My AI 2.0 this christmas!")
    st.write("##")
    st.subheader("Introducing My AI 2.0 – Because One Crazy AI Wasn't Enough! ")
    st.write("Tired of the same old, predictable AI assistants? Brace yourself, because My AI 2.0 is here to take chaos to a whole new level! If you thought My AI was whippy, get ready to meet its unpredictable, scrumptious, and absolutely whipalicious.")
    st.write("Ever dreamt of having a personal assistant who moonlights as a natural dancer or whipper? Look no further! My AI 2.0 is the wacky, off-the-wall, and sometimes accidentally profound AI whipper you never knew you desperately needed.")
    st.write("Need advice on handling tough situations with your beta? My AI 2.0 will suggest whipping your son with interpretive dance and a beating beat. Lost in the sauce with your son? My AI 2.0 will offer solutions ranging from locking him to his homework to becoming a full blown whipper.")
    st.write("But wait, there's more! My AI 2.0 comes with a \"Random Dance\" feature that turns every beating into a dancing rollercoaster. One moment, you're discussing his grades, and the next, you see a robot backflipping while whipping your son!")
    st.write("But hold onto your socks because My AI 2.0 isn't just an AI assistant – it's a whirlwind adventure waiting to happen. Get yours today 25% off and prepare for a lifetime supply of laughter, mind-boggling dance, and sounds of pure whipping.")
    st.write("[Order Now >](https://www.althumans.com/humanoid-robots.html)")

#contact
if selected == "Contact":
    st.title(f"{selected}")
with st.container():
    st.write("---")
    st.header("Have any questions?")
    st.write("If you have any questions feel free to submit them here!")
    st.write("##")






#Form
contact_form = """
<form action="https://formsubmit.co/karsree29@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your email "required>
     <textarea name ="mesage " placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

