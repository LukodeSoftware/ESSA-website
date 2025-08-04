def get_translations(lang):
    translations = {
        'en': {
            # General
            'site_name': "Emi's Swim School Academy",
            'site_subtitle': "Private Swimming Lessons in Warsaw",
            'site_name_subtitle': "Swimming Lessons Warsaw",

            # Navigation
            'nav_home': "Home",
            'nav_about': "About Me",
            'nav_gallery': "Gallery",
            'nav_pricing': "Pricing",
            'nav_contact': "Contact",

            # Hero Section
            'hero_headline': "Learn how to swim with a multiple-time Polish champion!",
            'hero_cta': "Book a lesson",

            # What We Offer
            'offer_title': "What We Offer",
            'offer_1': "Private swimming lessons in Warsaw",
            'offer_2': "Effective and fun lessons for children and adults",
            'offer_3': "Professional swimming technique training",
            'offer_4': "Learning swimming elements (e.g. jumps, diving, turns)",
            'offer_5': "Preparation for swimming and triathlon competitions",
            'offer_6': "Preparation for fitness and swimming exams",
            'offer_7': "Fun water activities for children",
            'offer_8': "Swimming lessons in English",
            'offer_cta': "Start training with a multiple-time Polish champion!",

            # Voucher Section
            'voucher_title': "Swimming Lesson Voucher with a Champion",
            'voucher_desc': "Give the gift of swimming – to yourself or someone you care about. Buy a voucher for 8 individual swimming lessons in Warsaw!",
            'voucher_type_1': "8 x 30 minutes",
            'voucher_type_2': "8 x 45 minutes",
            'voucher_type_3': "For one or two people",
            'voucher_button': "View pricing",

            # About School
            'about_school_title': "ESSA Swim School Warsaw – Sign Up Today!",
            'about_school_text': "ESSA is the perfect place to start your swimming journey, improve your technique, or prepare for competitions. Our classes are tailored to all age groups and skill levels – from young children to adults.",
            'about_school_guarantee': "We guarantee:",
            'about_school_point_1': "Experienced instructors",
            'about_school_point_2': "Effective teaching methods",
            'about_school_point_3': "Friendly and supportive atmosphere",
            'about_school_cta': "Sign up today",

            # Locations & Schedule
            'locations_title': "Our locations",
            'links_header': "Links",
            'schedule_heading': "Lesson hours:",
            'schedule_saturday': "Saturday: 11:00 AM – 8:00 PM",
            'schedule_sunday': "Sunday: 12:00 PM – 8:00 PM",
            'locations_heading': "Locations:",
            'location_1': "Inflancka Swimming Center",
            'location_1_address': "ul. Inflancka 8, Warsaw",
            'location_1_more': "More about this location",
            'location_2': "Medical University of Warsaw Pool (WUM)",
            'location_2_address': "ul. Księcia Trojdena 2C, Warsaw",
            'location_2_more': "More about this location",

            # Booking Section
            'booking_title': "Book Your Lesson Today!",
            'booking_desc': "Improve your swimming technique with tailored private lessons for both kids and adults.",
            'booking_cta': "Book a lesson",

            # Gallery
            'gallery_title': "Gallery",
            'gallery_subtitle': "Images from our lessons, competitions, and trainings",

            # About Me
            'about_title': "About Me",
            'about_intro': "Meet Emilia - Multiple-time Polish Swimming Champion",
            'about_greeting': "Hi!",
            'about_description1': """My name is Emilka and I’m the founder of the ESSA Warsaw swim school.
            I’ve been involved in swimming for over 20 years — first as a competitor, and later as an instructor.""",
            'about_description2': """For years, I trained in sports clubs, competing at the highest national level.
            I’m a multiple medalist of the Polish Championships in both short and long course pools, specializing in backstroke and individual medley in 50, 100, and 200-meter distances. I also took part in international competitions.""",
            'about_description3': """Currently, I combine my passion for sports with law studies and take part in the Polish Academic Championships, where I also win medals.""",
            'about_description4': """For several years, I’ve been teaching children, teenagers, and adults how to swim — from beginners to those who want to improve their technique, prepare for competitions, or pass physical fitness tests.""",
            'about_description5': "In my classes, I focus on an individual approach, safety, and a positive atmosphere.",
            'about_description6': "Why ESSA?",
            'about_description7': """It’s short for Emi’s Swim School Academy, but it also means chill and joy — the vibe I bring to my lessons.""",
            'about_description8': """If you want to learn to swim in a professional yet relaxed way, I warmly invite you to ESSA Warsaw!""",
            'about_achievements': "Achievements",
            'about_experience': "Teaching Experience",
            'testimonials_title': "Testimonials",

            # Achievements
            'achievement1': "Multiple-time medalist at the Polish Championships",
            'achievement2': "Winner of Championnats - Paris",
            'achievement3': "National Team Member",
            'achievement4': "University Sports Medalist",
            'achievement1_description': "Won national championships in backstroke and medley.",
            'achievement2_description': "Won international championships in 200m backstroke.",
            'achievement3_description': "Represented Poland as a member of the national swimming team.",
            'achievement4_description': "Multiple medals representing Univeristy SWPS Warsaw.",

            # Teaching experience
            'teaching_experience_intro': "After my competitive swimming career, I have focused on teaching swimming to people of all ages. I have over 5 years of experience teaching children and adults:",
            'teaching_experience1': "Certified swimming instructor with specialized training in teaching children",
            'teaching_experience2': "Experience with students of all levels from beginners to competitive swimmers",
            'teaching_experience3': "Modern teaching methods focusing on proper technique and enjoyment",
            'teaching_experience4': "Personalized approach adapted to each student's abilities and goals",
            'teaching_experience5': "Specialized in helping students overcome fear of water",
            'teaching_experience6': "Preparation for competitions and exams",
            'teaching_experience_outro': "My teaching philosophy is based on creating a supportive, encouraging environment where students can develop their swimming skills at their own pace. I believe that everyone can learn to swim with the right guidance and patience",

            # Pricing
            'pricing_title': "Pricing",
            'basic_prices': "Basic prices",
            'pricing_packages_5': "Packages of 5 classes paid in advance",
            'pricing_packages_10': "Packages of 10 classes paid in advance",

            'pricing_30min': "30 minutes",
            'pricing_45min': "45 minutes",
            'pricing_60min': "60 minutes",
            'pricing_vouchers': "Vouchers",
            'pricing_1person': "For 1 person",
            'pricing_2people': "For 2 people",
            'pricing_time': "Time",
            'pricing_1_person': "1 person",
            'pricing_2_persons': "2 people",
            'pricing_5_lessons_1_person': "5 lessons (1 person)",
            'pricing_5_lessons_2_persons': "5 lessons (2 people)",
            'pricing_10_lessons_1_person': "10 lessons (1 person)",
            'pricing_10_lessons_2_persons': "10 lessons (2 people)",
            'person': "person",
            'pricing_info': "Lessons can be canceled no later than 24 hours before their start. After this time, the lesson will be considered as conducted and the payment will not be refunded.",

            # Payment details
            'payment_details_title': "Payment details",
            'payment_details_heading': "Payment details for swimming lessons:",
            'bank_account': "Bank account:",
            'payment_info': "Cash payment before the lesson is also available.",


            # FAQ
            'faq-title': "Frequently Asked Questions",
            'faq-question-1': "What should I bring to my swimming lesson?",
            'faq-answer-1': "Please bring your swimming suit, a towel, swimming cap, goggles and flip-flops. All other equipment like kickboards or pull buoys will be provided during the lesson.",
            'faq-question-2': "How do I cancel or reschedule a lesson?",
            'faq-answer-2': "You can cancel or reschedule your lesson by contacting us via phone or email no later than 24 hours before your scheduled lesson. Cancellations with less than 24 hours notice will be charged as a completed lesson.",
            'faq-question-3': "How long does it take to learn to swim?",
            'faq-answer-3': "Learning to swim is a very individual process. Some students feel comfortable in water after just a few lessons, while others may take more time. Generally, with regular lessons (1-2 per week), most students can learn basic swimming skills within 2-3 months.",
            'faq-question-4': "What length of lesson is recommended to start with? 30, 45 or 60 minutes?",
            'faq-answer-4': "For the first lesson, we recommend 30-minute sessions for children and 45-minute sessions for adults. As the course progresses, the lesson duration is adjusted individually based on the student’s needs, abilities, and preferences.",

            # Contact
            'contact_title': "Contact Us",
            'contact_phone': "Phone",
            'contact_email': "Email",
            'contact_form_title': "Send us a message",
            'contact_name': "Name",
            'contact_email_field': "Email",
            'contact_phone_field': "Phone",
            'contact_message': "Message",
            'contact_submit': "Send Message",
            'contact_success': "Thank you! Your message has been sent.",
            'contact_error': "Sorry, there was an error sending your message. Please try again.",
            'schedule_day_title': "Day",
            'schedule_hours_title': "Hours",
            'schedule_availability_title': "Availability",
            'schedule_weekdays': "Monday - Friday",
            'schedule_saturday': "Saturday",
            'schedule_sunday': "Sunday",
            'schedule_weekdays_hours': "6:00 PM - 8:00 PM",
            'schedule_saturday_hours': "11:00 AM - 8:00 PM",
            'schedule_sunday_hours': "12:00 PM - 8:00 PM",
            'schedule_available': "Available",
            'schedule_info': "To book a specific time slot, please contact us by phone or email, or fill out the contact form.",

            # Footer
            'footer_privacy': "Privacy Policy",
            'footer_copyright': "© 2025 ESSA Emi's Swim School Academy",

            # Error Pages
            '404_title': "Page Not Found",
            '404_message': "The page you are looking for does not exist.",
            '500_title': "Server Error",
            '500_message': "Something went wrong on our server. Please try again later.",

            # Privacy Policy
            'privacy_policy_title': "Privacy Policy",

            'section1_title': "1. General Information",
            'section1_text': "This Privacy Policy outlines the rules for processing personal data through the website operated by ESSA Warsaw swimming school, managed by Bizera sp. z o.o., located at Rusiecka 8a, 03-698 Warsaw, Poland, NIP: 5242765832. For matters related to personal data, please contact us via email: info@essawaw.pl.",

            'section2_title': "2. Scope of Data Collected",
            'section2_intro': "As part of our business activities, we process the following data:",
            'section2_point1': "Identification data (name and surname of the participant and/or legal guardian)",
            'section2_point2': "Contact data (email address, phone number)",
            'section2_point3': "Organizational data (age, swimming level)",
            'section2_point4': "Technical data (IP address, browser type, operating system, connection time)",
            'section2_point5': "Information from contact forms and class registration",

            'section3_title': "3. Purposes and Legal Bases for Data Processing",
            'section3_intro': "We process data for the following purposes:",
            'section3_point1': "Class registration",
            'section3_point2': "Inquiry handling",
            'section3_point3': "Promotional information",
            'section3_point4': "Accounting documentation – based on legal obligations",
            'section3_point5': "Website improvement and statistics – based on legitimate interests",

            'section4_title': "4. Data Recipients",
            'section4_intro': "Data may be shared with:",
            'section4_point1': "hosting company",
            'section4_point2': "cooperating instructors and employees",
            'section4_point3': "accounting, legal, and IT service providers",
            'section4_point4': "providers of marketing and analytics tools (e.g., Google, Meta)",
            'section4_point5': "public authorities when required by law",

            'section5_title': "5. Data Retention Period",
            'section5_point1': "Service-related data – up to 5 years after the end of cooperation",
            'section5_point2': "Marketing data – up to 3 years after the last contact or until consent is withdrawn",
            'section5_point3': "Technical data – until deleted or according to browser settings",

            'section6_title': "6. Your Rights",
            'section6_intro': "You have the right to:",
            'section6_point1': "access your data",
            'section6_point2': "rectify your data",
            'section6_point3': "delete your data",
            'section6_point4': "restrict processing",
            'section6_point5': "data portability",
            'section6_point6': "object to processing",
            'section6_point7': "withdraw consent at any time",
            'section6_point8': "file a complaint with the President of the Personal Data Protection Office (ul. Stawki 2, 00-193 Warsaw)",

            'section7_title': "7. Cookies and Tracking Technologies",
            'section7_intro': "The website uses cookies for the following purposes:",
            'section7_point1': "maintaining sessions after visiting the site",
            'section7_point2': "statistical analysis (e.g., Google Analytics)",
            'section7_point3': "personalized advertising content",
            'section7_text': "Users can manage cookies through browser settings. Limiting cookies may affect the functionality of some parts of the site.",

            'section8_title': "8. Security Measures",
            'section8_point1': "SSL encrypted connection",
            'section8_point2': "regular system updates",
            'section8_point3': "data backups",
            'section8_point4': "data access restricted to authorized personnel",

            'section9_title': "9. Changes to the Privacy Policy",
            'section9_text': "This Privacy Policy may be updated periodically. The current version will always be available on our website. We recommend reviewing it regularly. Last updated: July 29, 2025."
        },
        'pl': {
            # General
            'site_name': "Emi's Swim School Academy",
            'site_subtitle': "Prywatne lekcje pływania w Warszawie",
            'site_name_subtitle': "Nauka Pływania Warszawa",

            # Navigation
            'nav_home': "Strona główna",
            'nav_about': "O mnie",
            'nav_gallery': "Galeria",
            'nav_pricing': "Cennik",
            'nav_contact': "Kontakt",

            # Hero Section
            'hero_headline': "Naucz się pływać z wielokrotną mistrzynią Polski!",
            'hero_cta': "Zarezerwuj lekcję",

            # What We Offer
            'offer_title': "Co oferujemy",
            'offer_1': "Prywatne lekcje pływania w Warszawie",
            'offer_2': "Efektywne i przyjemne zajęcia dla dzieci i dorosłych",
            'offer_3': "Profesjonalne doskonalenie techniki pływania",
            'offer_4': "Nauka elementów pływania (np. skoki, nurkowanie, nawroty)",
            'offer_5': "Przygotowanie do zawodów pływackich i triathlonowych",
            'offer_6': "Przygotowanie do egzaminów sprawnościowych i pływackich",
            'offer_7': "Zabawy w wodzie dla najmłodszych",
            'offer_8': "Zajęcia pływania po angielsku",
            'offer_cta': "Zacznij już dziś!",

            # Voucher Section
            'voucher_title': "Voucher na lekcje pływania z Mistrzynią",
            'voucher_desc': "Podaruj swimming – sobie lub komuś, na kim Ci zależy. Kup voucher na 8 indywidualnych lekcji pływania w Warszawie!",
            'voucher_type_1': "8 x 30 minut",
            'voucher_type_2': "8 x 45 minut",
            'voucher_type_3': "Dla jednej lub dwóch osób",
            'voucher_button': "Zobacz cennik",

            # About School
            'about_school_title': "ESSA Nauka Pływania Warszawa – Zapisz się już dziś!",
            'about_school_text': "ESSA to idealne miejsce, aby rozpocząć swoją przygodę z pływaniem, poprawić technikę lub przygotować się do zawodów. Nasze zajęcia są dostosowane do wszystkich grup wiekowych i poziomów umiejętności – od małych dzieci po dorosłych.",
            'about_school_guarantee': "Gwarantujemy:",
            'about_school_point_1': "Doświadczonych instruktorów",
            'about_school_point_2': "Skuteczne metody nauczania",
            'about_school_point_3': "Przyjazną i wspierającą atmosferę",
            'about_school_cta': "Zapisz się!",

            # Locations & Schedule
            'locations_title': "Nasze lokalizacje",
            'schedule_heading': "Godziny zajęć:",
            'schedule_saturday': "Sobota: 11:00 – 20:00",
            'schedule_sunday': "Niedziela: 12:00 – 20:00",
            'location_1': "Pływalnia Inflancka",
            'location_1_address': "ul. Inflancka 8, Warszawa",
            'location_1_more': "Więcej o tej lokalizacji",
            'location_2': "Basen WUM",
            'location_2_address': "ul. Księcia Trojdena 2C, Warszawa",
            'location_2_more': "Więcej o tej lokalizacji",

            # Booking Section
            'booking_title': "Zarezerwuj lekcję już dziś!",
            'booking_desc': "Popraw swoją technikę pływania dzięki indywidualnym lekcjom dostosowanym zarówno dla dzieci, jak i dorosłych.",
            'booking_cta': "Zarezerwuj lekcję",

            # Gallery
            'gallery_title': "Galeria",
            'gallery_subtitle': "Zdjęcia z naszych lekcji, zawodów i treningów",

            # About Me
            'about_title': "O mnie",
            'about_intro': "Poznaj Emilię - Wielokrotną Mistrzynię Polski w Pływaniu",
            'about_greeting': "Cześć!",
            'about_description1': """Nazywam się Emilka i jestem założycielką szkółki pływackiej ESSA Warsaw.
            Z pływaniem jestem związana od ponad 20 lat, najpierw jako zawodniczka, później instruktorka.""",
            'about_description2': """Przez lata trenowałam w klubach sportowych, startując na najwyższym krajowym poziomie.
            Jestem wielokrotną medalistką Mistrzostw Polski na krótkim i długim basenie, specjalizując się w stylu grzbietowym i zmiennym na dystansach 50, 100 i 200 metrów. Brałam także udział w zawodach międzynarodowych.""",
            'about_description3': """Obecnie łączę pasję do sportu ze studiami prawniczymi i startami w Akademickich Mistrzostwach Polski, gdzie również zdobywam medale.""",
            'about_description4': """Od kilku lat uczę pływać dzieci, młodzież i dorosłych, od osób zaczynających przygodę z wodą po tych, którzy chcą poprawić technikę, przygotować się do zawodów lub testów sprawnościowych.""",
            'about_description5': "Na zajęciach stawiam na indywidualne podejście, bezpieczeństwo i dobrą atmosferę.",
            'about_description6': "Dlaczego ESSA?",
            'about_description7': """To skrót od Emi’s Swim School Academy, ale też słowo oznaczające luz i radość, które towarzyszą moim zajęciom.""",
            'about_description8': """Jeśli chcesz uczyć się pływać w profesjonalny, ale swobodny sposób to zapraszam do ESSA Warsaw!""",
            'about_achievements': "Osiągnięcia",
            'about_experience': "Doświadczenie w nauczaniu",
            'testimonials_title': "Opinie",

            # Achievements
            'achievement1': "Wielokrotna medalistka Mistrzostw Polski",
            'achievement2': "Zwyciężczyni zawodów Championnats - Paris",
            'achievement3': "Reprezentantka Kadry Narodowej",
            'achievement4': "Medalistka Akademickich Mistrzostw Polski",
            'achievement1_description': "Zwycięstwa w mistrzostwach Polski w stylu grzbietowym i zmiennym.",
            'achievement2_description': "Zwycięstwo w międzynarodowych zawodach na 200 m stylem grzbietowym.",
            'achievement3_description': "Reprezentowała Polskę jako członkini narodowej kadry pływackiej.",
            'achievement4_description': "Wielokrotne medale w barwach Uniwersytetu SWPS w Warszawie.",


            # Teaching experience
            'teaching_experience_intro': "Po zakończeniu kariery zawodowej skupiłam się na nauczaniu pływania osób w każdym wieku. Mam ponad 5 lat doświadczenia w pracy z dziećmi i dorosłymi:",
            'teaching_experience1': "Certyfikowany instruktor pływania ze specjalistycznym szkoleniem w pracy z dziećmi",
            'teaching_experience2': "Doświadczenie w pracy z osobami na każdym poziomie – od początkujących po pływaków wyczynowych",
            'teaching_experience3': "Nowoczesne metody nauczania skupiające się na poprawnej technice i przyjemności z pływania",
            'teaching_experience4': "Indywidualne podejście dopasowane do możliwości i celów każdego ucznia",
            'teaching_experience5': "Specjalizacja w pracy z osobami z lękiem przed wodą",
            'teaching_experience6': "Przygotowanie do zawodów i egzaminów",
            'teaching_experience_outro': "Moja filozofia nauczania opiera się na tworzeniu wspierającej, motywującej atmosfery, w której uczniowie mogą rozwijać swoje umiejętności pływackie we własnym tempie. Wierzę, że każdy może nauczyć się pływać przy odpowiednim wsparciu i cierpliwości.",



            # Pricing
            'pricing_title': "Cennik",
            'basic_prices': "Ceny podstawowe",
            'pricing_packages_5': "Pakiety 5 zajęć do opłaty z góry",
            'pricing_packages_10': "Pakiety 10 zajęć do opłaty z góry",
            'pricing_30min': "30 minut",
            'pricing_45min': "45 minut",
            'pricing_60min': "60 minut",
            'pricing_time': "Czas",
            'pricing_1_person': "1 osoba",
            'pricing_2_persons': "2 osoby",
            'pricing_5_lessons_1_person': "5 zajęć (1 os.)",
            'pricing_5_lessons_2_persons': "5 zajęć (2 os.)",
            'pricing_10_lessons_1_person': "10 zajęć (1 os.)",
            'pricing_10_lessons_2_persons': "10 zajęć (2 os.)",
            'person': "os.",
            'pricing_info': "Zajęcia można anulować najpóźniej 24 godziny przed ich rozpoczęciem. Po tym czasie lekcja zostanie uznana za odbytą, a opłata nie zostanie zwrócona.",

            # Payment details
            'payment_details_title': "Dane do płatności",
            'payment_details_heading': "Dane do wpłat za naukę pływania:",
            'bank_account': "Rachunek:",
            'payment_info': "Możliwa jest również płatność gotówką przed zajęciami.",


            # FAQ
            'faq-title': "Najczęściej Zadawane Pytania",
            'faq-question-1': "Co przynieść na lekcję pływania?",
            'faq-answer-1': " Proszę zabrać ze sobą strój kąpielowy, ręcznik, czepek, okularki i klapki. Cały pozostały sprzęt, taki jak deski do pływania lub bojki, będzie zapewniony podczas lekcji.",
            'faq-question-2': "Jak odwołać lub przełożyć lekcję?",
            'faq-answer-2': "Możesz anulować lub przełożyć lekcję, kontaktując się z nami telefonicznie lub e-mailem najpóźniej 24 godziny przed zaplanowaną lekcją. Za lekcje odwołane w czasie krótszym niż 24 godziny przed zajęciami nie przysługuje zwrot.",
            'faq-question-3': "Ile czasu zajmuje nauczenie się pływania?",
            'faq-answer-3': "Nauka pływania to bardzo indywidualny proces. Niektórzy uczniowie czują się komfortowo w wodzie już po kilku lekcjach, podczas gdy inni potrzebują więcej czasu. Zazwyczaj, przy regularnych lekcjach (1-2 razy w tygodniu), większość uczniów może nauczyć się podstawowych umiejętności pływania w ciągu 2-3 miesięcy.",
            'faq-question-4': "Jaka długość lekcji jest polecana początek? 30, 45 czy 60 minut?",
            'faq-answer-4': "Na pierwsze zajęcia zalecamy lekcje 30-minutowe dla dzieci oraz 45-minutowe dla dorosłych. W kolejnych etapach długość zajęć jest dostosowywana indywidualnie – w zależności od potrzeb, możliwości oraz preferencji ucznia.",

            # Contact
            'contact_title': "Kontakt",
            'contact_phone': "Telefon",
            'contact_email': "Email",
            'contact_form_title': "Napisz do nas",
            'contact_name': "Imię i nazwisko",
            'contact_email_field': "Email",
            'contact_phone_field': "Telefon",
            'contact_message': "Wiadomość",
            'contact_submit': "Wyślij wiadomość",
            'contact_success': "Dziękujemy! Twoja wiadomość została wysłana.",
            'contact_error': "Przepraszamy, wystąpił błąd podczas wysyłania wiadomości. Spróbuj ponownie.",
            'schedule_day_title': "Dzień",
            'schedule_hours_title': "Godziny",
            'schedule_availability_title': "Dostępność",
            'schedule_weekdays': "Poniedziałek - Piątek",
            'schedule_saturday': "Sobota",
            'schedule_sunday': "Niedziela",
            'schedule_weekdays_hours': "18:00 - 20:00",
            'schedule_saturday_hours': "11:00 - 20:00",
            'schedule_sunday_hours': "12:00 - 20:00",
            'schedule_available': "Dostępne",
            'schedule_info': "Aby zarezerwować konkretny termin, prosimy o kontakt telefoniczny, mailowy lub wypełnienie formularza kontaktowego.",

            # Footer
            'footer_privacy': "Polityka prywatności",
            'footer_copyright': "© 2025 ESSA Emi's Swim School Academy",
            'locations_title_footer': "Lokalizacje",
            'links_header': "Linki",

            # Error Pages
            '404_title': "Strona nie znaleziona",
            '404_message': "Strona, której szukasz, nie istnieje.",
            '500_title': "Błąd serwera",
            '500_message': "Coś poszło nie tak na naszym serwerze. Spróbuj ponownie później.",

            # Privacy policy
            'privacy_policy_title': "Polityka Prywatności",

            'section1_title': "1. Informacje ogólne",
            'section1_text': "Niniejsza Polityka Prywatności określa zasady przetwarzania danych osobowych za pośrednictwem strony internetowej prowadzonej przez szkółkę pływacką ESSA Warsaw, prowadzoną przez Bizera sp. z o.o., z siedzibą przy ul. Rusieckiej 8a, 03-698 Warszawa, NIP: 5242765832. W sprawach związanych z danymi osobowymi można się skontaktować mailowo: info@essawaw.pl.",

            'section2_title': "2. Zakres zbieranych danych",
            'section2_intro': "W ramach prowadzonej działalności przetwarzamy następujące dane:",
            'section2_point1': "Dane identyfikacyjne (imię i nazwisko kursanta i/lub opiekuna prawnego)",
            'section2_point2': "Dane kontaktowe (adres e-mail, numer telefonu)",
            'section2_point3': "Dane organizacyjne (wiek, poziom pływacki)",
            'section2_point4': "Dane techniczne (adres IP, rodzaj przeglądarki, system operacyjny, czas połączenia)",
            'section2_point5': "Informacje z formularzy kontaktowych i zapisów na zajęcia",

            'section3_title': "3. Cele i podstawy przetwarzania danych",
            'section3_intro': "Dane przetwarzamy w następujących celach:",
            'section3_point1': "Zapisy na zajęcia",
            'section3_point2': "Obsługa zapytań",
            'section3_point3': "Informacje promocyjne",
            'section3_point4': "Prowadzenie dokumentacji księgowej – na podstawie obowiązku prawnego",
            'section3_point5': "Usprawnianie działania strony i statystyki – na podstawie prawnie uzasadnionego interesu",

            'section4_title': "4. Odbiorcy danych",
            'section4_intro': "Dane mogą być przekazywane:",
            'section4_point1': "firmie hostingowej",
            'section4_point2': "współpracującym instruktorom i pracownikom",
            'section4_point3': "firmom księgowym, prawnym i IT",
            'section4_point4': "dostawcom narzędzi marketingowych i analitycznych (np. Google, Meta)",
            'section4_point5': "organom publicznym, jeśli wymagają tego przepisy prawa",

            'section5_title': "5. Okres przechowywania danych",
            'section5_point1': "Dane potrzebne do realizacji usług – do 5 lat od zakończenia współpracy",
            'section5_point2': "Dane marketingowe – do 3 lat od ostatniego kontaktu lub do momentu wycofania zgody",
            'section5_point3': "Dane techniczne – do momentu usunięcia lub zgodnie z ustawieniami przeglądarki",

            'section6_title': "6. Twoje prawa",
            'section6_intro': "Masz prawo do:",
            'section6_point1': "dostępu do swoich danych",
            'section6_point2': "sprostowania danych",
            'section6_point3': "usunięcia danych",
            'section6_point4': "ograniczenia przetwarzania",
            'section6_point5': "przeniesienia danych",
            'section6_point6': "wniesienia sprzeciwu wobec przetwarzania",
            'section6_point7': "wycofania zgody w dowolnym momencie",
            'section6_point8': "złożenia skargi do Prezesa UODO (ul. Stawki 2, 00-193 Warszawa)",

            'section7_title': "7. Pliki cookies i technologie śledzące",
            'section7_intro': "Strona korzysta z plików cookies w celu:",
            'section7_point1': "utrzymania sesji po wejściu na stronę",
            'section7_point2': "analizy statystycznej (np. Google Analytics)",
            'section7_point3': "personalizacji treści reklamowych",
            'section7_text': "Użytkownik może samodzielnie zarządzać plikami cookies poprzez ustawienia przeglądarki. Ograniczenie stosowania cookies może wpłynąć na działanie niektórych funkcji strony.",

            'section8_title': "8. Środki bezpieczeństwa",
            'section8_point1': "szyfrowanie połączenia (SSL)",
            'section8_point2': "regularne aktualizacje systemu",
            'section8_point3': "kopie zapasowe danych",
            'section8_point4': "dostęp do danych tylko przez uprawnione osoby",

            'section9_title': "9. Zmiany w Polityce Prywatności",
            'section9_text': "Polityka prywatności może być okresowo aktualizowana. Aktualna wersja zawsze będzie dostępna na naszej stronie. Zalecamy jej regularne przeglądanie. Data ostatniej aktualizacji: 29 lipca 2025."
        }
    }

    return translations.get(lang, translations['en'])
