# Residenza 126

Residenza126 is a real estate showcase platform designed for buyers seeking modern, luxurious living spaces in Oristano, Italy. The website provides an elegant and user-friendly experience for exploring available properties within the Residenza 126 project, an exclusive residential complex.

The platform functions as a virtual showroom, allowing users to explore, filter, search and view available apartments securely. Each apartment listing provides detailed information, including floor plans, features, description and images/ videos.

 Registered users can save their favorite apartments for quick access and benefit from personalized recommendations.

Admin users oversee and maintain the property catalog and apartment details, ensuring all listings and specifications are up-to-date. They also have the authority to manage registered users.

Web marketing strategies for Residenza126 focus on organic social media marketing, primarily through Instagram, to engage potential buyers and showcase the project's offerings. 

The platform is built with Django, Python, HTML, Bootstrap, and CSS, ensuring a modern, responsive user experience. It is deployed via Heroku, with PostgreSQL used for database management. Cloudinary is utilized for media storage, and Whitenoise is integrated for efficient static file management.

![Application](staticfiles/README_docs/images/responsive.png "Application")

[Link to the live project](https://www.argicostruzioni.com/)

# Contents

- [User Experience (UX)](https://github.com/Lilla-Kavecsanszki/residenza127#user-experience-ux)
  - [Ideal Client](https://github.com/Lilla-Kavecsanszki/residenza127#ideal-client)
  - [User Stories & Epics](https://github.com/Lilla-Kavecsanszki/residenza127#user-stories-and-epics)
- [Planning](https://github.com/Lilla-Kavecsanszki/residenza127#planning)
- [Design](https://github.com/Lilla-Kavecsanszki/residenza127#design)
  - [Wireframes](https://github.com/Lilla-Kavecsanszki/residenza127#wireframes)
  - [Entity Relationship Diagrams](https://github.com/Lilla-Kavecsanszki/residenza127#entity-relationship-diagrams)
  - [Theme](https://github.com/Lilla-Kavecsanszki/residenza127#theme)
  - [Typography](https://github.com/Lilla-Kavecsanszki/residenza127#typography)
- [Languages Used](https://github.com/Lilla-Kavecsanszki/residenza127#languages-used)
- [Frameworks, Libraries, Programs & Technologies Used](https://github.com/Lilla-Kavecsanszki/residenza127#frameworks-libraries-programs--technologies-used)
- [Features](https://github.com/Lilla-Kavecsanszki/residenza127#features)
- [User Story - Features Cross-Reference Table](https://github.com/Lilla-Kavecsanszki/residenza127#user-story---features-cross-reference-table)
- [Deployment](https://github.com/Lilla-Kavecsanszki/residenza127#deployment)
- [Testing](https://github.com/Lilla-Kavecsanszki/residenza127#testing)
  - [Code Validation](https://github.com/Lilla-Kavecsanszki/residenza127#code-validation)
  - [Manual Testing](https://github.com/Lilla-Kavecsanszki/residenza127#manual-testing)
  - [Further Testing](https://github.com/Lilla-Kavecsanszki/residenza127#further-testing)
  - [Bugs](https://github.com/Lilla-Kavecsanszki/residenza127#bugs)
- [Credits](https://github.com/Lilla-Kavecsanszki/residenza127#credits)
  - [Media and Content](https://github.com/Lilla-Kavecsanszki/residenza127#media-and-content)
  - [Acknowledgments and Code](https://github.com/Lilla-Kavecsanszki/residenza127#acknowledgments-and-code)
  - [Disclaimer](https://github.com/Lilla-Kavecsanszki/residenza127#disclaimer)
  - 

# User Experience (UX)

### Ideal client

The ideal client for this business is:

-	English-speaking and Italian-speaking individuals
- Individuals seeking modern, high-quality living spaces in a peaceful, private environment
- Those looking for a blend of contemporary architecture and cutting-edge technology in a residential setting
- Investors and homebuyers who value premium finishes and customization options
- People seeking privacy, comfort, and style within a prestigious residential area
- Prospective tenants or buyers looking for a unique living experience in Oristano

Visitors to the **Residenza126** website are seeking:

- A **user-friendly platform** to explore available apartments, with detailed information about their features, floor plans, and customization options.
- A comprehensive overview of the **exclusive amenities** and benefits of living in a modern residential complex like Residenza126, highlighting the combination of contemporary design, peace, and privacy.
- **Personalized services** that cater to individual preferences, including the option to schedule private tours and receive tailored advice for apartment selection.
- A **high-quality, modern living experience** in the heart of Oristano, where luxury meets functionality.
- The ability to access **multilingual content** with both **English** and **Italian** language options, thanks to the **language selector**, ensuring a wider reach for prospective buyers or investors.

This website is the best way to help them achieve these goals because:

- The **intuitive navigation** makes it easy for visitors to explore apartment layouts, amenities, and other details, allowing them to make informed decisions about their new home.
- Detailed **apartment descriptions** include information on **floor plans, finishes, and customization** options, giving users insight into how they can personalize their living spaces to fit their unique needs and style.
- The site highlights **exclusive features** of Residenza126, such as **cutting-edge technological solutions** and premium, sustainable materials that align with the needs of modern, eco-conscious residents.
- The site provides **rich visuals** including **images and floor plans** of the apartments, helping visitors get a clear picture of what life in Residenza126 could be like.
- The **language selector** ensures that the website serves both **English and Italian-speaking** users, catering to an international clientele interested in investing or moving to Oristano.

In summary, **Residenza126** provides a high-end, user-focused experience for those looking for a modern, luxurious, and private living environment in Oristano. With a focus on premium quality, cutting-edge design, and a seamless browsing experience, the website effectively guides users through the process of discovering and learning about the exclusive **Residenza126** project.

[Back to top](https://github.com/Lilla-Kavecsanszki/residenza127#contents)

### User stories and Epics

#### Epic 1: User Management

- **US101: User Registration:** As a new user, I can register for an account with my email and password so that I can save my preferences and access property details.
- **US102: User Authentication:** As a returning user, I can log in using my existing credentials or log out so that I can access my personal details in a secure way.
- **US103: Receive Verification Email After Registration:** As a new user, I can receive an email confirmation after submitting the registration form so that I can verify my email address and complete the registration process.
- **US104: Personal User Profile:** As a site user, I can access my personalized user profile so that I can view my saved properties and preferences.

#### Epic 2: Property Management

- **US201: Purpose of Website and Navigation:** As a site user, I can quickly understand that the website showcases available apartments for sale, and I can navigate to various sections such as property listings, details, and contact information.
- **US202: Add New Property Listing:** As an admin, I can add new apartment listings to the website so that I can showcase the latest available apartments to prospective buyers.
- **US203: Update Property Information:** As an admin, I can edit property information such as pricing, floor plans, and availability to ensure the website reflects accurate and up-to-date listings.
- **US204: Delete Property Listing:** As an admin, I can remove properties that are no longer available or sold, so that users are not confused by outdated listings.
- **US205: View Apartment Listings:** As a user, I can view a list of available apartments, so that I can browse and compare different properties.
- **US206: View Detailed Property Information:** As a user, I can view detailed information about each property, including floor plans, features, and location, so that I can make an informed decision.
- **US207: Search for Properties:** As a user, I can search for apartments using keywords or filters (e.g., price, size, location) so that I can quickly find properties that match my criteria.
- **US208: Filter Properties:** As a user, I can filter apartments based on different criteria such as price range, number of bedrooms, and location, so that I can narrow down my search to the most relevant properties.
- **US209: Sort Properties:** As a user, I can sort the list of available apartments based on price, size, or other criteria to help me find the best match faster.
- **US210: View Multimedia for Each Property (Property Carousel):** As a user, I can view a carousel of images and videos for a property on the property details page, so that I can visually assess the property.
- **US211: Handle 404 Error:** As a user, if I encounter a broken link or missing property page, I can be redirected back to the homepage or property listings, ensuring a seamless browsing experience.

#### Epic 3: Contact and Inquiry Management

- **US301: Request Property Information:** As a user, I can request additional information about a property via a contact form or inquiry button, so that I can get more details before deciding to schedule a viewing.
- **US302: Schedule a Property Visit:** As a user, I can submit a request to schedule a visit for a specific apartment, and a representative can follow up with available times for a viewing.
- **US303: View Contact Details:** As a user, I can view contact details for the real estate agents or property managers so that I can easily reach out with questions or inquiries.
- **US304: Send Inquiry:** As a user, I can send an inquiry about a specific apartment to the admin or agent via email or contact form so that I can get more information or arrange a visit.
- **US305: Download Brochure:** As a user, I can download the latest brochure for Residenza 126, so that I can review all details, floor plans, and pricing offline or share it with others.

#### Epic 4: Language and Accessibility

- **US401: Language Switch**: As a user, I can switch between English and Italian so that I can view the website in my preferred language, improving accessibility and user experience.
- **US402: Display Content in Preferred Language**: As a user, I want the website content (such as property listings, navigation, etc.) to display in my selected language, ensuring consistent translation across the site.

#### Epic 5: User Profile Management

- **US601: View Profile Details**: As a registered user, I can view my personal details such as name, email, and phone number, to stay informed about my profile.
- **US602: Update Profile Information**: As a registered user, I can update my personal information like name and phone number to keep my profile current.
- **US603: Change Password**: As a user, I can change my password securely to maintain the privacy and security of my account.
- **US604: View Favourites**: As a user, I can view a list of properties I have marked as favourites, so that I can easily revisit them later.

#### Epic 6: Admin Panel and Management

- **US601: Admin Dashboard:** As an admin, I can access a dashboard to manage properties, users, and inquiries so that I can stay organized and ensure the site operates smoothly.
- **US602: Manage Property Listings:** As an admin, I can edit, update, or remove listings through the admin panel to keep the site accurate and up-to-date with available properties.
- **US603: Manage User Inquiries:** As an admin, I can review and respond to inquiries sent by site users about properties so that I can provide the necessary information to prospective buyers.

#### Epic 7: SEO and Web Marketing

- **US701: SEO Optimization:** As a site user, I can easily find the site through web searches, ensuring that prospective buyers can discover the website easily when searching for properties in Oristano.
- **US702: View Privacy Policy:** As a site user, I can access and view the company’s privacy policy so that I can understand how my data is handled in compliance with GDPR and other regulations.
- **US703: Contact Support:** As a user, I can easily access clear contact information or support options to get help with any issues related to the website or property inquiries.
- **US704: Leave Reviews and Feedback:** As a user, I can leave reviews or feedback about properties I have visited so that I can share my experiences and help others in their decision-making process.

#### Epic 8: Construction Projects

- **US801: View Construction Projects (Construction Page):** 
  - As a user, I can view upcoming construction projects, including their descriptions, images, and expected completion dates, so that I can stay informed about future developments.
  
- **US802: Browse Construction Project Details:** 
  - As a user, I can browse detailed information about each upcoming project, including its location, type of development, and any associated multimedia (images, videos), so that I can better understand future real estate opportunities.

[Back to top](https://github.com/Lilla-Kavecsanszki/residenza127#contents)


# Planning

The planning process for **Residenza 126** began with identifying the ideal clientele for the properties, which involved creating a Persona Profile using Code Institute's template and applying design thinking principles. This Persona Profile helped us better understand the needs, expectations, and preferences of the potential buyers or investors, allowing us to tailor the website experience specifically to them. The website was designed with these user personas in mind, ensuring the presentation and functionality catered to the right audience.

You can view the detailed persona profile [HERE](README_docs/design_thinking_persona_template.pdf).

Given the increasing reliance on mobile devices for browsing and searching for properties, designing a responsive and accessible website was a priority. We utilized Bootstrap’s grid system, along with responsive utilities and custom CSS, to ensure that the website provides a seamless experience across various devices, from desktop to mobile, allowing users to explore the Residenza 126 property easily from anywhere.

### Agile Methodology

In this project, we applied an **Agile** approach using **GitHub issues** to create **User Stories**, which were then grouped into **Epics** and **Milestones** in a GitHub Project. This served as the Agile project management tool to track progress and ensure the team remained on course. The development of issues was managed through a **Kanban board**, which helped us track tasks in stages from **To Do** to **Done**.

Currently, all major issues are marked as **"Done"**, except for a minor task (#42) which is labeled as **"Could have"** and **"Won't be included this time - next sprint"**, according to the **MoSCoW prioritization**. This means the task is desirable but not critical for the current sprint and will be addressed in a future sprint.

For easy access, you can view the **Epics**, **Issues/User Stories** with their **Acceptance Criteria**, and the **Kanban board** [HERE](https://github.com/users/Lilla-Kavecsanszki/projects/6).

[Back to top](https://github.com/Lilla-Kavecsanszki/residenza127#contents)

# Design

### Wireframes

Wireframes were utilized during the design process, generated with Balsamiq to plan and design the interface layout for different screen sizes.

[Wireframe - Home page](README_docs/home.pdf)

[Wireframe - Authentication pages](README_docs/authentication.pdf)

[Wireframe - Property pages](README_docs/product_related.pdf)

[Wireframe - My Profile page](README_docs/my_profile.pdf)

[Wireframe - Property Management page](README_docs/product_management.pdf)

[Wireframe - 404 page](README_docs/404.pdf)

### Entity Relationship Diagrams

To support the functionality of the **Residenza 126** website, the following models have been designed and implemented to store essential property, user, and contact-related information in the database.

The **User** table in the ER diagram serves as a conceptual representation only. It does not directly correspond to the models in `models.py` or the actual physical database tables, but it offers a logical view of how data entities relate to each other. The **User** model handles the management of registered users, including their personal information, preferences, and interactions with the properties.

The **Property** and **Profile** models are designed to handle the details of the properties available for viewing or purchase and the user profiles, respectively. These models store critical details such as property name, price, location, and user preferences for favorite properties.

Additionally, the **ContactForm** model captures the information submitted by users via the contact form on the website. This model allows users to reach out with inquiries about the properties or any other questions they may have regarding **Residenza 126**. The form data is stored securely, including fields such as name, email address, message, and the date/time of submission.

The **Entity Relationship Diagrams (ERD)** below illustrate how the models are interconnected, showcasing the relationships between users, properties, profiles, and contact forms. This ensures that all relevant data is properly organized and accessible for the various website functionalities, such as property browsing, saving favorites, managing user profiles, and handling contact inquiries.

The following models have been designed and implemented to support the functionality of the EarthAlchemy Naturals app. Each model is described with its purpose and relationships with other models.

- UserProfile Model:
    - It is related to the built-in Django **User** model using a `OneToOneField`. This establishes a one-to-one relationship between user profiles and users, ensuring that each user has one user profile and vice versa.
    - It also has a `ManyToManyField` to the **Property** model, allowing users to like properties, keeping track of their interests.

- Property Model:
    - It includes a `ManyToManyField` to the **User** model, which tracks which users have liked each property.
    - The **Property** model also has fields for details like **price**, **bedrooms**, **bathrooms**, **location**, and **property_type**, along with media fields for **main_image** and **main_video** (stored via **Cloudinary**).

- PropertyImage Model:
    - This model is related to the **Property** model via a `ForeignKey`, allowing multiple images to be associated with each property.

- PropertyVideo Model:
    - Like **PropertyImage**, it is related to the **Property** model via a `ForeignKey`, enabling multiple videos to be associated with each property.

- Contact Model:
    - It is a standalone model used for storing contact form submissions.
    - It includes fields like **name**, **email**, **phone_number**, **subject**, **message**, and a **created_at** timestamp for when the contact was submitted.

The following ER diagrams detail these relationships:

<p>
<details><summary>ER Diagram</summary><br/>
<img src="README_docs/images/er_diagram.png" alt="ER Diagram">
</details>


[Back to top](https://github.com/Lilla-Kavecsanszki/residenza127#contents)

### Theme

- White - #ffffff
- Dark Gray - #a9a9a9
- Goldenrod - #daa520
- Atlantic Navy - #16357
- Fibonacci Blue - #182d5f

![colour_palette](staticfiles/README_docs/images/colorkit.png "colour_palette")

The color palette for the Residenza126 website has been carefully selected to reflect the brand's core values of purity, elegance, and natural well-being. It harmoniously blends neutral tones with vibrant accents, conveying a sense of freshness and tranquility that aligns with the nature of the products. The color scheme is designed to highlight key elements for better user engagement and readability while staying true to the aesthetic of the company’s logo.

### Typography

- Cormorant Garamond (Secondary Font for Body and Subheadings):
  - Cormorant Garamond is a serif font that blends modern and classical design elements. Its elegant and readable design makes it perfect for body text and subheadings. This font ensures readability while maintaining a refined and luxurious aesthetic.

![Cormorant_Garamond](staticfiles/README_docs/images/Cormorant_Garamond.png "cormorant_garamond")

- Italiana (Accent Font):
  - Italiana adds a touch of refined elegance with its flowing, cursive style. Used sparingly for emphasis or in specific design elements, it adds a distinctive charm to the overall design while maintaining a sophisticated tone.

![Italiana](staticfiles/README_docs/images/Italiana.png "italiana")

- Playfair Display (Navbar Font):
  - Playfair Display is used in the navbar to give the site an elegant, upscale look. Its high contrast and bold characteristics make it stand out in the navigation, enhancing visibility and ensuring a refined aesthetic. The serif details add a touch of sophistication while maintaining clarity, guiding users smoothly through the website's sections.

![Playfair_Display](staticfiles/README_docs/images/Playfair_Display.png "playfair_display")

- Cinzel (Primary Font for Headings):
  - Cinzel is a classic serif font inspired by Roman inscriptions, offering an elegant and timeless look. It adds a touch of sophistication and grandeur to headings and titles, aligning with the brand's focus on natural, luxurious products.

![Cinzel](staticfiles/README_docs/images/Cinzel.png "cinzel")

Overall, this combination of fonts creates a harmonious balance between elegance and readability, ensuring that both the body text and headers stand out clearly while maintaining the sophisticated and clean aesthetic of the site. The fonts work together to enhance the user experience and support the brand's identity, providing a visually pleasing and engaging environment.

[Back to top](https://github.com/Lilla-Kavecsanszki/residenza127#contents)

# Languages Used

- HTML5
- Python
- CSS3
- Javascript

[Back to top](https://github.com/Lilla-Kavecsanszki/residenza127#contents)

## Frameworks, Libraries, Programs & Technologies Used

- [**Balsamiq**](https://balsamiq.com/) was used to create the wireframes.
- [**Free Privacy Policy Generator**](https://www.freeprivacypolicy.com/free-privacy-policy-generator/) was used to generate the privacy policy for the website.
- [**Lucid**](https://lucid.app/documents#/documents?folder_id=recent) was used to create the ER diagrams.
- [**Canva**](https://www.canva.com/) was used to create the brochure and contact buttons/links on the homepage.
- [**ColorKit**](https://colorkit.co/palette/ffffff-a9a9a9-daa520-163573-182d5f/) was used to create the website's color palette.
- **GitHub** was used as the repository for the project code after being pushed from Git.
- **Visual Studio Code** was used for version control, allowing me to commit changes and push them to GitHub directly from the VS Code terminal. It was the primary tool used for creating and editing all the code.
- [**Google Fonts**](https://fonts.google.com/) was used to source the fonts for the project.
- [**Font Awesome**](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
- [**Favicon**](https://favicon.io/) was used to create the favicon.
- [**Bootstrap**](https://getbootstrap.com/) was used to build a responsive website quickly.
- **Microsoft Word** was used during the design process to sketch out wireframes.
- [**Django**](https://www.djangoproject.com/) was used as the web framework for building the application.
- [**Gunicorn**](https://gunicorn.org/) was used as the web server to run Django on Heroku.
- [**Pillow**](https://pillow.readthedocs.io/en/stable/index.html) - Python Imaging Library, used for image handling.
- [**Django Allauth**](https://django-allauth.readthedocs.io/en/latest/) was used for account registration and authentication.
- [**Django Crispy Forms**](https://django-crispy-forms.readthedocs.io/en/latest/) was used for advanced form rendering.
- [**Cloudinary**](https://cloudinary.com/) was used for storing static files and images, ensuring easy access and management.
- [**Heroku**](https://heroku.com/) was used to deploy the application and provide an environment in which the code can execute.
- [**dj-database-url**](https://pypi.org/project/dj-database-url/) - Used for simplifying database URL configuration.
- [**dj3-cloudinary-storage**](https://pypi.org/project/dj3-cloudinary-storage/) - This is the specific Django package used to connect Django with Cloudinary for static and media storage.
- [**django-cloudinary-storage**](https://pypi.org/project/django-cloudinary-storage/) - Another Cloudinary integration for Django, used for handling media file uploads.
- [**django-phonenumber-field**](https://github.com/stefanfoulis/django-phonenumber-field) - Added to handle phone number fields with international support.
- [**Django Extensions**](https://django-extensions.readthedocs.io/en/latest/) - Provides additional management commands for Django.
- [**SendGrid**](https://sendgrid.com/) - Integrated to send transactional emails via API.
- [**Whitenoise**](https://whitenoise.readthedocs.io/en/latest/) - For serving static files efficiently in production, particularly on Heroku.
- [**ASGI**](https://asgi.readthedocs.io/en/latest/) (asgiref) was used for asynchronous server gateway interface support in Django.
- [**Babel**](https://babel.pocoo.org/en/latest/) - Used to manage internationalization and localization.
- [**Black**](https://black.readthedocs.io/en/stable/) - Python code formatter used to maintain code consistency and style.
- [**Certifi**](https://pypi.org/project/certifi/) - Provides Mozilla’s root certificates for secure HTTPS requests.
- [**CFFI**](https://cffi.readthedocs.io/en/latest/) - Provides a foreign function interface for Python to call C code.
- [**Click**](https://click.palletsprojects.com/en/8.1.x/) - Used for command-line interface creation.
- [**Cryptography**](https://cryptography.io/en/latest/) - A Python library used for secure encryption and cryptographic operations.
- [**Flake8**](https://flake8.pycqa.org/en/latest/) - A Python tool for enforcing coding standards.
- [**IDNA**](https://pypi.org/project/idna/) - For handling internationalized domain names.
- [**Isort**](https://pycqa.github.io/isort/) - A Python tool used to sort imports.
- [**MCCabe**](https://github.com/PyCQA/mccabe) - A complexity checker for Python code.
- [**Mypy Extensions**](https://mypy.readthedocs.io/en/stable/extensions.html) - A library to support optional typing in Python.
- [**Packaging**](https://packaging.pypa.io/en/latest/) - For managing Python package building and distribution.
- [**Pathspec**](https://github.com/cachapa/pathspec) - Used for path matching functionality in Python.
- [**Phonenumbers**](https://github.com/daviddrysdale/python-phonenumbers) - Library for parsing, formatting, and validating phone numbers.
- [**Psycopg2**](https://www.psycopg.org/) - PostgreSQL database adapter for Python.
- [**Pycodestyle**](https://pycodestyle.readthedocs.io/en/latest/) - Python style guide checker.
- [**Pycparser**](https://pypi.org/project/pycparser/) - A library for parsing C code.
- [**Pyflakes**](https://pypi.org/project/pyflakes/) - A fast static code analysis tool for Python.
- [**Python Magic**](https://github.com/ahupp/python-magic) - A library used to determine file types based on content.
- [**Requests**](https://docs.python-requests.org/en/latest/) - A simple library for making HTTP requests.
- [**SQLParse**](https://buildmedia.readthedocs.org/media/pdf/sqlparse/latest/sqlparse.pdf) - A library used to parse SQL statements.
- [**StarkBank ECDSA**](https://github.com/starkbank/ecdsa) - Used for elliptic curve cryptography and secure authentication.
- [**Typing Extensions**](https://pypi.org/project/typing-extensions/) - For providing support for type hints in Python.
- [**Urllib3**](https://urllib3.readthedocs.io/en/latest/) - A powerful HTTP library for Python.

[Back to top](https://github.com/Lilla-Kavecsanszki/residenza127#contents)

# Features

## Home Page

### F01 Navigation Bar

The navigation bar provides easy access to all active pages for the user.

## Future ambitions

- Construction page

[Back to top](https://github.com/Lilla-Kavecsanszki/residenza127#contents)

# User Story - Features Cross-Reference table

How the Features align with and fulfill the User Stories by providing the necessary functionality and interactions that meet the users' needs and requirements.

[Cross-reference Table](README_docs/us_f_crossreference.pdf "crossreference_table")

[Back to top](https://github.com/Lilla-Kavecsanszki/residenza127#contents)

# Deployment

#### The live link to the application can be found here - [www.argicostruzioni.com](https://www.argicostruzioni.com/)

[Back to top](https://github.com/Lilla-Kavecsanszki/residenza127#contents)

# Testing

## Code Validation

## Manual Testing

The table provided below presents the test cases that were utilized, with the corresponding results, and references to the corresponding Feature IDs that each test case addressed. These test cases were primarily designed based on the Acceptance Criteria specified for each User Story.

Details here:
[Manual Testing Document](README_docs/manual_testing_cases.pdf)

All tests passed successfully, indicating that the specified features and functionalities are working as intended.

### Further testing

<p>
<details><summary>Details</summary><br/>
I asked friends and family to look at the application on their devices, browsers and report any issues they find. A few responsiveness and semantical issues were resolved as a result of this.
</details>

[Back to top](https://github.com/Lilla-Kavecsanszki/residenza127#contents)


## Bugs




# Credits

## Media and Content

All images and videos were provided by the client (originals) or sourced from [Adobe](https://www.adobe.com/stock) and [Pexels](https://www.pexels.com/).

All content, text, and materials on the website were provided by the client.

## Acknowledgments and Code

The Residenza126 project was developed in alignment with the client’s brief and agreement. While the project's core elements were shaped based on the client’s specific needs and vision, I also conducted research on similar websites in the industry. This allowed me to better understand market trends and user expectations, ensuring that the final product met both the client’s objectives and industry best practices.

The below websites and Youtube channels have been used to understand the logic of building this project with Django;

- The walk-through project 'Boutique Ado' from Code Institute videos - some of its codes were used in the project: <https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+2021_T1/courseware/eb05f06e62c64ac89823cc956fcd8191/3adff2bf4a78469db72c5330b1afa836/>

- <https://www.youtube.com/watch?v=YZvRrldjf1Y>

- shimmer button: <https://codepen.io/Amarjit/pen/mrbjNy>
- admin site list_display: <https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display>
- Carousel: - <https://codepen.io/chingy/pen/yLLZRbj>
            - <https://codepen.io/Navneet-Dwivedi/pen/LYXbvVL>


[Back to top](https://github.com/Lilla-Kavecsanszki/residenza127#contents)




•	Data Protection: We must ensure that the website is GDPR-compliant, especially regarding the collection, storage, and processing of personal data. This includes implementing measures such as consent management, data encryption, and user rights management.