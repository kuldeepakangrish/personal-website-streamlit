import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Kuldeepak Resume", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")
img_kuldeepak_portrait = Image.open("images/KuldeepakAngrish.jpeg")

# ---- HEADER SECTION ----
with st.container():
    text_column, image_column = st.columns((3, 1))
    with image_column:
        st.image(img_kuldeepak_portrait)
    with text_column:
        st.title("Kuldeepak Angrish")
        st.subheader("Sales Engineering Leader")
        st.write(
            """
            - Seasoned Solution Engineering leader helping enterprises with API adoption, automation, Big Data, IoT, and Cloud Technologies.
            - Built-Managed-Mentored NAM West pre-sales team.
            - Guided deals from the technical front while collaborating with sales leadership to formally define sales process & qualify opportunities.
            - Trailblazer for SwAG’s cloud transformation & adoption journey Won many firsts -iPaas Deal, IoT deal NAM West, Cloud deal.
            - Well-versed in positioning, presenting and articulating solutions from technical & business perspectives to a variety of audiences from developers to C level.
        """
        )
        st.write("[LinkedIn >](https://www.linkedin.com/in/kuldeepakangrish/)")

# ---- ACHIEVEMENTS ----
with st.container():
    st.write("---")
    st.header("ACHIEVEMENTS & THOUGHT LEADERSHIP")
    left_column, right_column = st.columns(2)
    with left_column:
        #st.header("ACHIEVEMENTS & THOUGHT LEADERSHIP")
        
        st.markdown("[Infosys Blog Practitioner’s View: What Does it Mean to Integrate a Multinational Corporation, Technically](https://app.box.com/s/xgoiub4nj9vsrpojyl2vgbeb00hys9oq)")    
        st.markdown("[LinkedIn Live: Building Modern Foundations for Cloud Innovation](https://www.linkedin.com/video/live/urn:li:ugcPost:6877321443001065473/)")    
        st.markdown("[YouTube: Driving Innovation and Disruption in a Time of Accelerated Change](https://www.youtube.com/watch?t=1212&v=Qz6qC6i2MJc&feature=youtu.be)")    
        st.markdown("[LinkedIn: RFP or Not to RFP](https://www.linkedin.com/pulse/rfp-kuldeepak-angrish/)")    
        st.markdown("[SoftwareAG.com: Improving customer satisfaction using webMethods.io](https://www.softwareag.com/en_corporate/customers/customer-stories/webmethods-customer-satisfaction-story.html)")    
        st.markdown("[iDevnews.com: Integration Developer News - Cloud Architecture Summit](https://www.idevnews.com/registration?event_id=521&code=ws_calendar)")        
        st.markdown('<iframe width="200" height="100" src="https://www.youtube.com/embed/HNk293pQTHo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',unsafe_allow_html=True)

        
    with right_column:
        #st_lottie(lottie_coding, height=300, key="coding_achievements")
        st.write("##")
        st.write(
            """
            - Led Team with > 150% Quota for 2019 & 2020
            - #1 Pre-Sales with 435% Quota in 2016
            - Consistently achieved >100%
            """
        )

# ---- WORK EXPERIENCE ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("WORK EXPERIENCE")
        st.subheader("[RapidAPI](https://rapidapi.com)")
        st.write("##")
        st.write(
            """
            - Established hiring strategy.
            - Led various field Marketing events from a tech/messaging perspective.
            - Created a brand new inbound lead channel with an RFP thought leadership.
            """
        )
        st.subheader("[SoftwareAG](https://softwareag.com)")
        st.write("##")
        st.write(
            """
            - Led and Coached field sales [AE/SE] for campaigns and led the team in the right direction for a win.
            - Defined strategies with Sales Leadership to come up with value prop.
            - Collaborated with cross-functional teams (Prod Marketing, Prod Management, RnD, CSM etc.) to best serve the customer.
            - Led Inseego IoT opportunity from C level relation to evaluation to eventual win(1st IoT win NAM West for SwAG)
            - Instrumental in getting key net new logos like Google, Chevron, Adobe.
            """
        )
        st.write(
            """
            Key Accomplishments:
            - Proposed Google’s supply chain group how to handle 10x of their traffic to address seasonality and growing hardware business.
            - Implemented modular solutions that reduced 3M's SAP rollout time and saved them millions of dollars, reduced time to plant-level inventory visibility by 50%.
            - Revolutionized Chevron's downstream operations by streamlining lead synchronization and reducing wait times from days to minutes.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=Qz6qC6i2MJc&t=1212s)")
        st.subheader("[Flex](https://flex.com)")
        st.write("##")
        st.write(
            """
            Built a global team of solution managers to ensure customers are seamlessly on-boarded. We added 60+(and 200+ suppliers) partners resulting in 25% revenue growth.
            """
        )
        st.write(
            """
            Key Accomplishments:
            - Designed and implemented a self-service partner onboarding framework. Reduced ~28 days onboarding process to 5 days.
            - Led one of the manufacturing sites to go live on a robust modern platform for Cisco. Won Cisco’s Supplier Appreciation Award.
            - Helped Flex achieve stringent peak time SLA for supply chain communication with Apple.
            """
        )

        st.subheader("[Infosys](https://infosys.com)")
        st.write("##")
        st.write(
            """
            Led many customer engagements for smooth delivery of transformational projects @fortune 500 companies.
            """
        )
        st.write(
            """
            Key Accomplishments:
            - Re Architected aps.com to bring down the response time within 2ms SLA, improving customer experience and drop in support engagement.
            - Helped Toshiba Europe to tightly integrate siloed applications with a 66% reduction in maintenance costs
            """
        )


# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/kuldeepak@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
