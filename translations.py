def get_translations(lang):
    translations = {
        'en': {
            # General
            'site_name': "Emi's Swim School Academy",
            'site_subtitle': "Swimming Lessons in Warsaw",
            'site_name_subtitle': "Swimming Lessons Warsaw",

            # Navigation
            'nav_home': "Home",
            'nav_about': "About Me",
            'nav_gallery': "Gallery",
            'nav_pricing': "Pricing",
            'nav_contact': "Contact",

            # Hero Section
            'hero_headline': "Private swimming lessons with a multiple-time Polish champion!",
            'hero_cta': "Book a lesson",

            # What We Offer
            'offer_title': "What We Offer",
            'offer_1': "Private swimming lessons in Warsaw",
            'offer_2': "Fun and effective lessons for children and adults",
            'offer_3': "Professional swimming technique training",
            'offer_4': "Learning swimming elements (e.g. diving, turns)",
            'offer_5': "Preparation for swimming and triathlon competitions",
            'offer_6': "Preparation for fitness and swimming exams",
            'offer_cta': "Start training with a multiple-time Polish champion!",

            # Voucher Section
            'voucher_title': "Swimming Lesson Voucher with a Champion",
            'voucher_desc': "Give the gift of swimming – to yourself or someone you care about. Buy a voucher for 8 individual swimming lessons in Warsaw!",
            'voucher_type_1': "8 x 30 minutes",
            'voucher_type_2': "8 x 45 minutes",
            'voucher_type_3': "For one or two people",
            'voucher_button': "View pricing",

            # About School
            'about_school_title': "ESSA Swim School Warsaw – Enroll Today!",
            'about_school_text': "ESSA is the perfect place to start your swimming journey, improve your technique, or prepare for competitions. Our classes are tailored to all age groups and skill levels – from young children to adults.",
            'about_school_guarantee': "We guarantee:",
            'about_school_point_1': "Experienced instructors",
            'about_school_point_2': "Effective teaching methods",
            'about_school_point_3': "Friendly and supportive atmosphere",
            'about_school_cta': "Sign up today",

            # Locations & Schedule
            'locations_title': "Where and When?",
            'locations_title_footer': "Our Locations",
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
            'about_description': "As a multiple-time Polish swimming champion, I've dedicated my life to mastering the art of swimming. Now, I'm passionate about sharing my knowledge and experience with both children and adults who want to learn or improve their swimming techniques.",
            'about_achievements': "Achievements",
            'about_experience': "Teaching Experience",
            'testimonials_title': "Testimonials",

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
            'pricing_info': "All packages must be used within 2 months from the first lesson. Cancellations must be madeat least 24 hours in advance, otherwise the lesson is counted as completed.",

            # Payment details
            'payment_details_title': "Payment details",
            'payment_details_heading': "Payment details for swimming lessons:",
            'bank_account': "Bank account:",


            # FAQ
            'faq-title': "Frequently Asked Questions",
            'faq-question-1': "What should I bring to my swimming lesson?",
            'faq-answer-1': "Please bring your swimming suit, a towel, swimming cap, and goggles. It's also good to have flip-flops for pool area. All other equipment like kickboards or pull buoys will be provided during the lesson.",
            'faq-question-2': "How do I cancel or reschedule a lesson?",
            'faq-answer-2': "You can cancel or reschedule your lesson by contacting us via phone or email at least 24 hours before your scheduled lesson. Cancellations with less than 24 hours notice will be charged as a completed lesson.",
            'faq-question-3': "How long does it take to learn to swim?",
            'faq-answer-3': "Learning to swim is a very individual process. Some students feel comfortable in water after just a few lessons, while others may take more time. Generally, with regular lessons (once per week), most students can learn basic swimming skills within 2-3 months.",
            'faq-question-4': "What length of lesson is recommended to start with? 30 or 45 minutes?",
            'faq-answer-4': "At first, 30-minute lessons are best – they allow you to gradually get used to the water and the new environment. As your comfort and fitness improve, you can easily extend the classes to 45 minutes.",

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
            'privacy_intro': "At ESSA, we are committed to protecting your privacy. This Privacy Policy explains how we collect, use, and safeguard your personal information when you visit our website or use our services.",

            # Information We Collect
            'information_we_collect_title': "Information We Collect",
            'personal_information_title': "Personal Information:",
            'personal_information_text': "When you create an account or make a purchase, we collect personal information such as your name, email address, and shipping address.",
            'usage_data_title': "Usage Data:",
            'usage_data_text': "We may collect information about how you interact with our website, including pages visited, time spent, and other analytics data.",
            'cookies_title': "Cookies:",
            'cookies_text': "We use cookies to enhance your browsing experience and improve our services.",

            # How We Use Your Information
            'how_we_use_information_title': "How We Use Your Information",
            'order_processing_title': "Order Processing:",
            'order_processing_text': "We use your personal information to process orders, deliver products, and provide customer support.",
            'marketing_communications_title': "Marketing Communications:",
            'marketing_communications_text': "With your consent, we may send you promotional emails or newsletters.",
            'analytics_title': "Analytics:",
            'analytics_text': "We analyze usage data to improve our website and services.",

            # Data Security
            'data_security_title': "Data Security",
            'data_security_text': "We take appropriate measures to protect your personal information from unauthorized access, disclosure, alteration, or destruction.",

            # Your Rights
            'your_rights_title': "Your Rights",
            'your_rights_text': "You have the right to access, correct, or delete your personal information. Please contact us if you have any requests or questions.",

            # Changes to this Policy
            'policy_changes_title': "Changes to this Policy",
            'policy_changes_text': "We may update this Privacy Policy from time to time. Please review it periodically for any changes.",
        },
        'pl': {
            # General
            'site_name': "Emi's Swim School Academy",
            'site_subtitle': "Lekcje pływania w Warszawie",
            'site_name_subtitle': "Nauka Pływania Warszawa",

            # Navigation
            'nav_home': "Strona główna",
            'nav_about': "O mnie",
            'nav_gallery': "Galeria",
            'nav_pricing': "Cennik",
            'nav_contact': "Kontakt",

            # Hero Section
            'hero_headline': "Prywatne lekcje pływania z wielokrotną mistrzynią Polski!",
            'hero_cta': "Zarezerwuj lekcję",

            # What We Offer
            'offer_title': "Co oferujemy",
            'offer_1': "Prywatne lekcje pływania w Warszawie",
            'offer_2': "Zabawne i skuteczne zajęcia dla dzieci i dorosłych",
            'offer_3': "Profesjonalne doskonalenie techniki pływania",
            'offer_4': "Nauka elementów pływania (np. nurkowanie, nawroty)",
            'offer_5': "Przygotowanie do zawodów pływackich i triathlonowych",
            'offer_6': "Przygotowanie do egzaminów sprawnościowych i pływackich",
            'offer_cta': "Rozpocznij treningi z wielokrotną mistrzynią Polski!",

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
            'about_school_cta': "Zapisz się dziś",

            # Locations & Schedule
            'locations_title': "Gdzie i kiedy?",
            'schedule_heading': "Godziny zajęć:",
            'schedule_saturday': "Sobota: 11:00 – 20:00",
            'schedule_sunday': "Niedziela: 12:00 – 20:00",
            'locations_heading': "Lokalizacje:",
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
            'about_description': """Cześć, nazywam się Emilka i jestem założycielką szkółki ESSA Warsaw.🐬 Poniżej znajdziesz więcej informacji o mnie, mojej przygodzie z pływaniem i wiele innych ciekawych rzeczy. ☺️

            Od ponad 20 lat jestem związana z pływaniem. Od 4 klasy podstawówki należałam do klubu, jak i również uczęszczałam do szkoły sportowej. Wtedy też poznałam swojego trenera, z którym trenowałam przez kolejne 10 lat. Pamiętam jak na pierwszym treningu powiedział, że mam pływać pierwsza na torze. Od tamtej pory starałam się prowadzić, co nie zawsze było łatwe.
            Pierwszy medal mistrzostw Polski zdobyłam w kategorii 16 latków, i potem co pół roku kilka krążków wpadało do kolekcji. 🥇🥈🥉
            Oprócz tego od ponad 3 lat zajmuję się nauką pływania dzieci i dorosłych. Uwielbiam przekazywać swoją wiedzę i zdobyte doświadczenie moim podopiecznym, dlatego też zdecydowałam o założeniu swojej szkółki. 🥰
            Nazwa „ESSA” jest nie tylko skrótem od „Emi’s Swim School Academy”, ale i również słowem, które oznacza radość, luz i brak przymusu… czyli to co u mnie na zajęciach. 😉
            Jeśli chcesz się przekonać to zapraszam do kontaktu i zapisu na lekcje!

            Pływaj ze mną i ESSA!🤪""",
            'about_achievements': "Osiągnięcia",
            'about_experience': "Doświadczenie w nauczaniu",
            'testimonials_title': "Opinie",


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
            'pricing_info': "Wszystkie pakiety muszą zostać wykorzystane w ciągu 2 miesięcy od pierwszej lekcji. Anulacje muszą zostać dokonane co najmniej 24 godziny wcześniej, w przeciwnym razie lekcja zostanie uznana za zakończoną.",

            # Payment details
            'payment_details_title': "Dane do płatności",
            'payment_details_heading': "Dane do wpłat za naukę pływania:",
            'bank_account': "Rachunek:",

            # FAQ
            'faq-title': "Najczęściej Zadawane Pytania",
            'faq-question-1': "Co powinienem przynieść na lekcję pływania?",
            'faq-answer-1': "Proszę zabrać ze sobą strój kąpielowy, ręcznik, czepek i okularki. Dobrze jest też mieć klapki na basenie. Cały pozostały sprzęt, taki jak deski do pływania lub bojki, będzie zapewniony podczas lekcji.",
            'faq-question-2': "Jak odwołać lub przełożyć lekcję?",
            'faq-answer-2': "Możesz anulować lub przełożyć lekcję, kontaktując się z nami telefonicznie lub e-mailem co najmniej 24 godziny przed zaplanowaną lekcją. Anulacje dokonane z wyprzedzeniem krótszym niż 24 godziny będą rozliczane jako ukończona lekcja.",
            'faq-question-3': "Ile czasu zajmuje nauczenie się pływania?",
            'faq-answer-3': "Nauka pływania to bardzo indywidualny proces. Niektórzy uczniowie czują się komfortowo w wodzie już po kilku lekcjach, podczas gdy inni potrzebują więcej czasu. Zazwyczaj, przy regularnych lekcjach (raz w tygodniu), większość uczniów może nauczyć się podstawowych umiejętności pływania w ciągu 2-3 miesięcy.",
            'faq-question-4': "Jaka długość lekcji jest polecana początek? 30 czy 45 minut?",
            'faq-answer-4': "Na początek najlepiej sprawdzają się lekcje 30-minutowe – pozwalają stopniowo przyzwyczaić się do wody i nowego środowiska. Gdy wzrośnie komfort i kondycja, można śmiało wydłużyć zajęcia do 45 minut.",

            # Contact
            'contact_title': "Kontakt",
            'contact_phone': "Telefon",
            'contact_email': "Email",
            'contact_form_title': "Wyślij nam wiadomość",
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
            'privacy_policy_title': "Polityka prywatności",
            'privacy_intro': "W ESSA dokładamy wszelkich starań, aby chronić Twoją prywatność. Niniejsza Polityka Prywatności wyjaśnia, w jaki sposób gromadzimy, wykorzystujemy i chronimy Twoje dane osobowe, gdy odwiedzasz naszą stronę lub korzystasz z naszych usług.",

            'information_we_collect_title': "Informacje, które zbieramy",
            'personal_information_title': "Dane osobowe:",
            'personal_information_text': "Gdy tworzysz konto lub dokonujesz zakupu, zbieramy dane osobowe takie jak imię i nazwisko, adres e-mail oraz adres dostawy.",
            'usage_data_title': "Dane o użytkowaniu:",
            'usage_data_text': "Możemy zbierać informacje o tym, jak korzystasz z naszej strony, w tym odwiedzane strony, czas spędzony i inne dane analityczne.",
            'cookies_title': "Pliki cookies:",
            'cookies_text': "Używamy plików cookies, aby poprawić Twoje wrażenia z przeglądania oraz ulepszać nasze usługi.",

            'how_we_use_information_title': "Jak wykorzystujemy Twoje dane",
            'order_processing_title': "Przetwarzanie zamówień:",
            'order_processing_text': "Używamy Twoich danych osobowych do realizacji zamówień, dostarczania produktów i obsługi klienta.",
            'marketing_communications_title': "Komunikacja marketingowa:",
            'marketing_communications_text': "Za Twoją zgodą możemy wysyłać Ci e-maile promocyjne lub biuletyny.",
            'analytics_title': "Analityka:",
            'analytics_text': "Analizujemy dane o użytkowaniu, aby ulepszać naszą stronę internetową i usługi.",

            'data_security_title': "Bezpieczeństwo danych",
            'data_security_text': "Podejmujemy odpowiednie środki, aby chronić Twoje dane osobowe przed nieautoryzowanym dostępem, ujawnieniem, zmianą lub zniszczeniem.",

            'your_rights_title': "Twoje prawa",
            'your_rights_text': "Masz prawo do dostępu, poprawiania lub usuwania swoich danych osobowych. Skontaktuj się z nami w razie pytań lub wniosków.",

            'policy_changes_title': "Zmiany w tej polityce",
            'policy_changes_text': "Możemy od czasu do czasu aktualizować niniejszą Politykę Prywatności. Prosimy o okresowe jej przeglądanie w celu zapoznania się z ewentualnymi zmianami.",
        }
    }

    return translations.get(lang, translations['en'])
