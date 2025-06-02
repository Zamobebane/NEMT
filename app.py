# app.py

import streamlit as st
from datetime import datetime

# ——————————————————————————————————————————————————————————————
# Streamlit page configuration
# ——————————————————————————————————————————————————————————————
st.set_page_config(
    page_title="My Oregon Ride | NEMT",
    page_icon="🚐",
    layout="wide",
)

# Define the navigation menu items
PAGES = ["Home", "About Us", "Services", "Fleet", "Book a Ride", "Contact", "FAQ"]

# ——————————————————————————————————————————————————————————————
# Sidebar Navigation
# ——————————————————————————————————————————————————————————————
with st.sidebar:
    # Logo (replace with your actual logo URL)
    st.image(
        "https://raw.githubusercontent.com/yourusername/yourrepo/main/assets/logo.png",
        width=150,
    )
    st.markdown("<h2 style='text-align:center; color: #4B4B4B;'>My Oregon Ride</h2>", unsafe_allow_html=True)
    page_selection = st.radio("Navigate", PAGES)

# ——————————————————————————————————————————————————————————————
# Function to display a banner on each page
# ——————————————————————————————————————————————————————————————
def show_banner():
    st.image(
        "https://raw.githubusercontent.com/yourusername/yourrepo/main/assets/banner.jpg",
        use_column_width=True,
    )
    st.markdown("<hr>", unsafe_allow_html=True)

# ——————————————————————————————————————————————————————————————
# Page helper functions
# ——————————————————————————————————————————————————————————————

def show_home():
    show_banner()
    st.title("My Oregon Ride 🚐")
    st.markdown(
        """
        **Your Trusted Non-Emergency Medical Transportation Provider in Oregon.**

        At My Oregon Ride, we specialize in safe, comfortable, and punctual rides to your medical appointments—whether it’s a dialysis session, doctor’s visit, or routine check-up.

        - **24/7 Availability**  
        - **Wheelchair & Stretcher-Accessible Vans**  
        - **Professional, CPR-Certified Drivers**  
        - **Serving Portland, Eugene, Salem, and Surrounding Areas**  
        """
    )
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("🕒 Punctuality Guaranteed")
        st.write("We monitor traffic and schedules to ensure you arrive on time.")
    with col2:
        st.subheader("💺 Comfortable Rides")
        st.write("Our vehicles are clean, sanitized, and fully accessible.")
    with col3:
        st.subheader("💲 Affordable Rates")
        st.write("Competitive pricing, accepted insurance, and transparent billing.")
    st.markdown("---")

    st.subheader("How It Works")
    st.markdown(
        """
        1. **Book Online or Call Us**: Use our booking form below or dial (253) 561-5714.  
        2. **Confirm Appointment**: We’ll confirm your pickup time and any special requirements.  
        3. **Ride Comfortably**: Our trained driver arrives, assists you into the vehicle, and takes you to your destination safely.  
        4. **Return Trip**: If needed, schedule your return in advance or request it on the spot.  
        """
    )


def show_about():
    show_banner()
    st.header("About My Oregon Ride")
    st.markdown(
        """
        Founded in 2024, My Oregon Ride was created to fill a critical need for reliable, dignified, and safe non-emergency medical transportation (NEMT) across Oregon. Our mission is to empower patients and families with a transportation solution that respects their time, comfort, and medical requirements.

        - **Our Vision**: Every patient deserves access to high-quality transportation for healthcare without stress.  
        - **Our Mission**: Provide punctual, safe, and comfortable rides—whether you need a wheelchair-accessible van, stretcher service, or ambulation assistance.  
        - **Service Area**: Portland, Eugene, Salem, Keizer, Beaverton, Hillsboro, and surrounding counties.  
        """
    )
    st.image(
        "https://raw.githubusercontent.com/yourusername/yourrepo/main/assets/about_image.jpg",
        use_column_width=True,
    )
    st.markdown("---")

    st.subheader("Why Choose Us?")
    st.write(
        """
        - **Fully Licensed & Insured**: Meets all state and federal NEMT regulations.  
        - **Certified Drivers**: CPR-certified, trained in patient transfers, and background-checked.  
        - **Modern Fleet**: Each vehicle is sanitized after every trip and equipped to handle wheelchairs, stretchers, and oxygen.  
        - **Insurance Billing**: We work with most major insurance providers—ask us about coverage.  
        """
    )


def show_services():
    show_banner()
    st.header("Our Services")
    st.markdown(
        """
        **My Oregon Ride** offers a wide range of NEMT services to fit your needs:

        1. **Wheelchair Transport**  
           - Fully equipped wheelchair vans.  
           - Secure tie-downs and fold-away ramps.  
           - Door-to-door assistance.  
        
        2. **Ambulatory Transport**  
           - For patients who can walk but need assistance getting to/from the vehicle.  
           - Well-trained staff to provide any needed support.  
        
        3. **Stretcher Transport**  
           - Comfortable stretchers with safety belts.  
           - Oxygen and medical-grade reclining seats available.  
        
        4. **Long-Distance Trips**  
           - We cover appointments up to 100 miles one-way.  
           - Flat rate + per-mile fee (contact us for specifics).  
        
        5. **Scheduled & Same-Day Rides**  
           - Book up to 30 days in advance or request same-day via phone.  
        
        6. **Insurance & Self-Pay Options**  
           - We bill most Medicaid/Medicare plans directly.  
           - Self-pay rates available upon request.  
        """
    )


def show_fleet():
    show_banner()
    st.header("Our Fleet")
    st.markdown(
        """
        We maintain a modern, well-inspected fleet to ensure safe and comfortable transportation:
        """
    )

    st.markdown(
        """
        - **Wheelchair Van**  
          ![Wheelchair Van](https://raw.githubusercontent.com/yourusername/yourrepo/main/assets/wheelchair_van.jpg)  
          *Equipped with hydraulic ramp, safety straps, and extra headroom.*

        - **Stretcher Van**  
          ![Stretcher Van](https://raw.githubusercontent.com/yourusername/yourrepo/main/assets/stretcher_van.jpg)  
          *Reclining stretcher, oxygen mount, and medical storage cabinet.*

        - **Ambulatory Van**  
          ![Ambulatory Van](https://raw.githubusercontent.com/yourusername/yourrepo/main/assets/ambulatory_van.jpg)  
          *Standard van with fold-away seats, handrails, and gentle lift assistance.*
        """
    )
    st.markdown("---")
    st.write(
        """
        All vehicles are:  
        - Cleaned and sanitized after each ride  
        - Maintained to the highest safety standards  
        - Equipped with GPS tracking and two-way communication  
        """
    )


def show_booking_form():
    show_banner()
    st.header("Book a Ride")
    st.markdown(
        """
        Please fill out the form below to schedule your non-emergency medical transportation.  
        One of our coordinators will reach out to confirm details and any special requirements.
        """
    )

    with st.form(key="booking_form"):
        col1, col2 = st.columns(2)

        with col1:
            full_name = st.text_input("Patient Name", max_chars=100)
            phone = st.text_input(
                "Phone Number", placeholder="e.g., (253) 561-5714"
            )
            email = st.text_input(
                "Email Address", placeholder="e.g., name@example.com"
            )
            pickup_address = st.text_input("Pickup Address")
            dropoff_address = st.text_input("Drop-Off Address")
            appointment_date = st.date_input(
                "Appointment Date", datetime.now().date()
            )
            appointment_time = st.time_input(
                "Appointment Time", datetime.now().time()
            )

        with col2:
            assistance_type = st.selectbox(
                "Assistance Type",
                [
                    "Wheelchair Transport",
                    "Stretcher Transport",
                    "Ambulatory Transport",
                    "Other",
                ],
            )
            return_trip = st.checkbox("Need Return Trip?", value=False)
            if return_trip:
                return_date = st.date_input("Return Date", datetime.now().date())
                return_time = st.time_input("Return Time", datetime.now().time())
            else:
                return_date = None
                return_time = None

            insurance_carrier = st.selectbox(
                "Insurance Carrier (if applicable)",
                ["Medicaid", "Medicare", "Private Insurance", "Self-Pay", "Other"],
            )
            notes = st.text_area("Additional Notes / Special Requirements", height=100)

        submit_button = st.form_submit_button("Submit Booking Request")

    if submit_button:
        st.success(f"✅ Thank you, **{full_name}**! Your booking request has been received.")
        st.write("**Summary of your request:**")
        summary_md = f"""
        - **Patient:** {full_name}  
        - **Phone:** {phone}  
        - **Email:** {email}  
        - **Pickup:** {pickup_address} on {appointment_date} at {appointment_time.strftime("%H:%M")}  
        - **Drop-Off:** {dropoff_address}  
        - **Assistance:** {assistance_type}  
        - **Return Trip:** {"Yes" if return_trip else "No"}  
        """
        if return_trip:
            summary_md += f"- **Return On:** {return_date} at {return_time.strftime('%H:%M')}\n"
        summary_md += f"- **Insurance / Pay:** {insurance_carrier}\n"
        if notes:
            summary_md += f"- **Notes:** {notes}\n"

        st.markdown(summary_md)
        st.info(
            "Our dispatch team will call you within 1 business hour to confirm "
            "rates, insurance billing, and finalize your reservation."
        )


def show_contact():
    show_banner()
    st.header("Contact Us")
    st.markdown(
        """
        **My Oregon Ride**  
        12070 SW Fischer Rd Apt A108  
        Tigard, OR 97224  

        📞 **Phone:** (253) 561-5714  
        📧 **Email:** myoregonride@gmail.com  
        
        **Office Hours:**  
        Monday – Friday: 7:00 AM – 7:00 PM  
        Saturday – Sunday: 8:00 AM – 5:00 PM  
        """
    )
    st.markdown("**Follow us on social media:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("[Facebook](https://www.facebook.com/MyOregonRide)")
    with col2:
        st.markdown("[Instagram](https://www.instagram.com/MyOregonRide)")
    with col3:
        st.markdown("[LinkedIn](https://www.linkedin.com/company/my-oregon-ride)")

    st.markdown("---")
    st.subheader("Send Us a Message")
    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email_contact = st.text_input("Your Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message", height=150)
        contact_submit = st.form_submit_button("Send Message")
    if contact_submit:
        st.success(f"✅ Thank you, {name}! Your message has been sent.")
        st.write("We will respond as soon as possible.")


def show_faq():
    show_banner()
    st.header("Frequently Asked Questions (FAQ)")
    faqs = {
        "Do you accept insurance?": (
            "Yes. We bill most Medicaid and Medicare plans directly. "
            "We also accept major private insurers. Please have your insurance information handy when booking."
        ),
        "How far in advance should I schedule my ride?": (
            "We recommend booking at least 24 hours in advance. "
            "Same-day requests may be accommodated based on availability."
        ),
        "Are your vehicles wheelchair accessible?": (
            "Absolutely. All our vans are fully equipped with hydraulic wheelchair ramps, "
            "secure tie-downs, and seating to ensure safety and comfort."
        ),
        "What if my appointment runs late?": (
            "Please notify us as soon as possible. We’ll do our best to accommodate any changes, "
            "but additional fees may apply for extended wait times."
        ),
        "Do you provide oxygen or medical monitoring?": (
            "Yes. Our stretcher vans can be equipped with oxygen mounts. "
            "For extended medical monitoring, please inform us ahead of time so we can assign a certified EMT driver."
        ),
        "What is your cancellation policy?": (
            "Cancellations made 2 hours before the scheduled pickup time are free of charge. "
            "Late cancellations or no-shows may incur a fee."
        ),
    }
    for question, answer in faqs.items():
        with st.expander(question):
            st.write(answer)


# ——————————————————————————————————————————————————————————————
# Main logic: render the selected page
# ——————————————————————————————————————————————————————————————
if page_selection == "Home":
    show_home()
elif page_selection == "About Us":
    show_about()
elif page_selection == "Services":
    show_services()
elif page_selection == "Fleet":
    show_fleet()
elif page_selection == "Book a Ride":
    show_booking_form()
elif page_selection == "Contact":
    show_contact()
elif page_selection == "FAQ":
    show_faq()
