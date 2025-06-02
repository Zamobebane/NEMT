# app.py

import streamlit as st
from PIL import Image
import base64

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="My Oregon Ride - NEMT Services",
    page_icon="🚐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------
# CSS and Background Setup
# ------------------------------
def set_background_image(image_file):
    """
    Injects CSS to set a full-screen background image for the Streamlit app.
    Expects image_file to be the path to an image in the repo.
    """
    with open(image_file, "rb") as img:
        encoded_string = base64.b64encode(img.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background: url("data:image/jpeg;base64,{encoded_string}") no-repeat center center fixed;
        background-size: cover;
    }}
    /* Make content containers slightly translucent to stand out */
    .reportview-container .main .block-container {{
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 12px;
        padding: 2rem 2rem 2rem 2rem;
    }}
    /* Customize header font and color */
    .header-title {{
        font-family: 'Helvetica', sans-serif;
        color: #2c3e50;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }}
    .subheader {{
        font-family: 'Helvetica', sans-serif;
        color: #34495e;
        font-size: 1.25rem;
        margin-bottom: 1.5rem;
    }}
    /* Style buttons */
    .stButton>button {{
        background-color: #2980b9;
        color: white;
        border-radius: 8px;
        height: 3rem;
        width: 100%;
        font-size: 1.1rem;
        font-weight: 600;
    }}
    .stButton>button:hover {{
        background-color: #1f618d;
        color: #ecf0f1;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set your background image (place 'background.jpg' in the same folder as app.py)
set_background_image("background.jpg")

# ------------------------------
# Sidebar Navigation / Booking Form
# ------------------------------
st.sidebar.image("logo.png", use_column_width=True)  # Place a 'logo.png' in the repo for branding (optional)

st.sidebar.markdown("<h2 class='header-title'>Book Your Ride</h2>", unsafe_allow_html=True)
st.sidebar.write("Complete the form below, and we'll get back to you within minutes. We serve 24/7!")

with st.sidebar.form(key="booking_form"):
    st.write("### Ride Details")
    name = st.text_input("Full Name", max_chars=50)
    phone = st.text_input("Phone Number", max_chars=15, help="e.g., 555-123-4567")
    email = st.text_input("Email Address", max_chars=100)
    pickup_address = st.text_input("Pickup Address", max_chars=200)
    dropoff_address = st.text_input("Drop-off Address", max_chars=200)
    date = st.date_input("Date of Service")
    time = st.time_input("Time of Service")
    wheelchair = st.selectbox(
        "Do you require wheelchair assistance?",
        ("No", "Yes")
    )
    notes = st.text_area(
        "Additional Notes / Special Requirements",
        placeholder="e.g., traveling with oxygen, service animal, etc."
    )
    submit_button = st.form_submit_button(label="Request a Quote")

if submit_button:
    # In a real app, you would handle form submission (e.g., send an email or store in a database)
    st.sidebar.success("Thank you! We received your request and will be in touch shortly.")
    # Example: st.write("Booking details:", name, phone, email, pickup_address, dropoff_address, date, time, wheelchair, notes)

# ------------------------------
# Main Content
# ------------------------------

# Header Section
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.markdown("<h1 class='header-title'>My Oregon Ride</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'><i>Your Trusted 24/7 Non-Emergency Medical Transportation Service</i></p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Brief Introduction
st.markdown(
    """
    **My Oregon Ride** is dedicated to providing safe, reliable, and comfortable non-emergency medical transportation
    across the Portland area and beyond. With our 24/7 service, professional drivers, and ADA-compliant vehicles,
    you can rest assured that your medical appointments are just a ride away.
    """
)

# Two-column layout: About Us and Why Choose Us
col1, col2 = st.columns(2)

with col1:
    st.markdown("### About Us")
    st.write(
        """
        - **Established Expertise**: Our team has over 10 years of combined experience in medical transport and patient care coordination.
        - **Safety First**: All vehicles are thoroughly sanitized before and after each trip. Drivers undergo specialized training and background checks.
        - **ADA-Compliant Fleet**: We offer wheelchair lifts, securement systems, and spacious interiors to accommodate various mobility needs.
        - **Insurance & Licensing**: Fully licensed, bonded, and insured to operate in Oregon; we adhere to all state and federal regulations.
        """
    )

with col2:
    st.markdown("### Why Choose My Oregon Ride?")
    st.write(
        """
        - **24/7 Availability**: Late-night or early-morning appointments? We’re on-call around the clock.
        - **Flat & Transparent Rates**: No hidden fees. You’ll know your fare upfront.
        - **Real-Time Tracking**: Receive live updates on your driver’s location and estimated arrival time.
        - **Multilingual Drivers**: English, Kurdish, and Arabic-speaking staff to assist diverse communities.
        - **Easy Scheduling**: Book online, via phone, or through our mobile-friendly website.
        - **Insurance Billing**: We handle most major insurances and Medicaid/Medicare for seamless billing.
        """
    )

st.markdown("---")

# Services Section
st.markdown("## Our Services")
st.write(
    """
    1. **Medical Appointments**  
       Transportation to hospitals, clinics, dialysis centers, physical therapy sessions, and other medical facilities.  
    2. **Routine Check-ups**  
       Safe rides for routine doctor visits, dental check-ups, and specialist appointments.  
    3. **Therapy & Rehab**  
       Secure transport for physical therapy, occupational therapy, and rehabilitation centers.  
    4. **Dialysis Transport**  
       Dedicated, comfortable vans for patients attending dialysis sessions multiple times a week.  
    5. **Pharmacy Runs**  
       Convenient medication pick-up and delivery services if you cannot leave home.  
    6. **Discharge Transport**  
       Calm and supportive ride home from hospital discharge—no rush, no stress.
    """
)

# Areas Served
st.markdown("### Areas We Serve")
areas = [
    "Portland Metro (PDX, Gresham, Beaverton, Hillsboro)",
    "Tigard & Lake Oswego",
    "Beaverton & Tigard",
    "Clackamas County (Oregon City, Gladstone)",
    "Washington County (Hillsboro, Forest Grove, Cornelius)",
    "Multnomah County (Portland, Troutdale, Fairview)",
    "Clark County WA (Vancouver, Camas, Battle Ground)"
]
for area in areas:
    st.write(f"- {area}")

st.markdown("---")

# Fleet & Safety
st.markdown("## Our Fleet & Safety Protocols")
fleet_img_col, fleet_text_col = st.columns([1, 2])

with fleet_img_col:
    st.image("fleet_sample.jpg", caption="Our ADA-Compliant Vehicle", use_column_width=True)

with fleet_text_col:
    st.write(
        """
        - **ADA-Accessible Vans**: Wheelchair ramps, lift systems, and securement points.  
        - **Comfortable Seating**: Extra legroom, climate-controlled interiors, and cushioned seats.  
        - **Sanitization**: Vehicles are deep-cleaned daily; high-touch areas disinfected between trips.  
        - **GPS-Enabled**: Real-time navigation and route optimization to reduce travel time.  
        - **Emergency Preparedness**: First-aid kits on board. Drivers trained in basic first aid and CPR.
        """
    )

st.markdown("---")

# Testimonials Section
st.markdown("## What Our Clients Say")
testimonials = [
    {
        "quote": "My Oregon Ride made getting to my dialysis appointments so much easier! Always on time, polite drivers, and spotless vans.",
        "client": "Emily R."
    },
    {
        "quote": "I rely on their late-night service when I have urgent medical tests. Dependable 24/7 availability is a lifesaver!",
        "client": "Michael S."
    },
    {
        "quote": "Booking is super easy via their website. Insurance billing was seamless, and they took care of everything.",
        "client": "Sarah L."
    }
]

for t in testimonials:
    st.markdown(f"> *\"{t['quote']}\"*  ")
    st.markdown(f"> — **{t['client']}**")
    st.write("")

st.markdown("---")

# Contact Section
st.markdown("## Contact Us")
contact_col1, contact_col2 = st.columns(2)

with contact_col1:
    st.markdown("**Phone**")
    st.write("📞 253-561-5714")
    st.markdown("**Email**")
    st.write("✉️ myoregonride@gmail.com")
    st.markdown("**Address**")
    st.write("🏢 12070 SW Fischer Rd, Apt A108, Tigard, OR 97224")
    st.markdown("**24/7 Dispatch Line**")
    st.write("🚐 Available Anytime—Call or Text")

with contact_col2:
    map_image = Image.open("map_placeholder.png")  # Place a map placeholder or actual map image in the repo
    st.image(map_image, caption="Tigard, OR Office Location", use_column_width=True)

st.markdown("---")

# Footer
st.markdown(
    """
    <div style='text-align: center; color: #7f8c8d; font-size: 0.9rem; margin-top: 2rem;'>
    © 2025 My Oregon Ride LLC | All Rights Reserved &nbsp;|&nbsp; Designed with care for our community
    </div>
    """,
    unsafe_allow_html=True
)
