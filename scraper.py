import requests
from bs4 import BeautifulSoup
import json

job_data = [
    {
        "id": "12345",
        "title": "Software Engineer",
        "company": "Tech Innovators Inc.",
        "location": "123 Silicon Valley Blvd, San Francisco, CA",
        "description": "As a Software Engineer, you will be responsible for developing and maintaining web applications. You will work in a collaborative environment with a focus on writing efficient and scalable code. Your tasks will include designing software architecture, building scalable web services, and implementing testing strategies. You should have a deep understanding of object-oriented programming principles and an ability to write clean, reusable code. You will also be responsible for optimizing applications for maximum performance and ensuring compatibility with various platforms.",
        "degree_requirements": "Bachelor's degree in Computer Science, Information Technology, or a related field."
    },
    {
        "id": "67890",
        "title": "Backend Developer",
        "company": "CodeCraft Solutions",
        "location": "45 Tech Park, Austin, TX",
        "description": "We are looking for a skilled Backend Developer to join our team. You will build and maintain server-side applications, ensuring high performance and responsiveness. Your primary responsibilities will involve writing robust code, working with databases, and integrating third-party services. A strong understanding of algorithms and data structures is essential, along with experience in API development and cloud services. You will collaborate with frontend developers to ensure seamless data exchange and improve user experiences. The role will require you to actively participate in the design and architecture of the backend systems.",
        "degree_requirements": "Bachelor\u2019s or Master\u2019s degree in Computer Science or equivalent experience."
    },
    {
        "id": "11223",
        "title": "Frontend Developer",
        "company": "FutureTech Labs",
        "location": "89 Innovation Drive, Seattle, WA",
        "description": "As a Frontend Developer, you will create engaging and user-friendly interfaces for web applications. You will work closely with the design team to implement beautiful designs and ensure the application works smoothly across multiple devices. Your responsibilities include writing clean, maintainable HTML, CSS, and JavaScript code, and optimizing it for performance and accessibility. You will work with tools like React, Vue, or Angular to build reusable components. Your work will directly impact the user experience, and you should have an eye for detail and a passion for delivering polished, high-quality applications.",
        "degree_requirements": "Bachelor's degree in Web Development, Computer Science, or a related field."
    },
    {
        "id": "44567",
        "title": "Full Stack Developer",
        "company": "TechPioneers Inc.",
        "location": "77 Digital Way, New York, NY",
        "description": "Join our team as a Full Stack Developer. You will design, develop, and deploy web applications, working across the full stack of technologies. Your primary responsibilities include building and maintaining the front-end and back-end architecture, ensuring seamless integration between the user interface and server-side components. You will collaborate closely with the design team to implement user-friendly features and troubleshoot issues. Familiarity with JavaScript, Node.js, and databases such as MySQL or MongoDB is essential. Your role will involve ensuring the scalability, performance, and security of the applications, as well as debugging and resolving production issues.",
        "degree_requirements": "Bachelor's degree in Computer Science or related field, or equivalent practical experience."
    },
    {
        "id": "78901",
        "title": "Data Scientist",
        "company": "DataWorks Solutions",
        "location": "12 Big Data Street, Chicago, IL",
        "description": "We are looking for a Data Scientist to analyze and interpret complex data sets to provide actionable insights. You will use your expertise in statistics and machine learning to improve business strategies. Your responsibilities will include developing predictive models, performing data wrangling and cleaning, and working with large datasets to uncover trends and patterns. You will collaborate with other teams to understand their data needs and translate those into clear, actionable analysis. This role requires strong problem-solving skills, familiarity with data visualization techniques, and a deep understanding of machine learning algorithms.",
        "degree_requirements": "Master's or PhD in Data Science, Machine Learning, Computer Science, or related field."
    },
    {
        "id": "10111",
        "title": "AI Engineer",
        "company": "Smart Solutions AI",
        "location": "456 Tech Road, Boston, MA",
        "description": "As an AI Engineer, you will design, develop, and deploy machine learning models to solve real-world problems. You will work with large datasets, develop algorithms, and create systems that can learn from data. Your role will involve building models that can predict outcomes, automate tasks, and provide business insights. You will collaborate with data engineers to build the infrastructure needed for training and deploying models. This role requires proficiency in Python, TensorFlow, PyTorch, and cloud-based AI services. You will also need experience in working with neural networks, deep learning, and natural language processing.",
        "degree_requirements": "Bachelor's or Master's degree in Computer Science, AI, Machine Learning, or a related field."
    },
    {
        "id": "12389",
        "title": "Mobile Developer",
        "company": "AppWorks",
        "location": "112 Mobile Street, Los Angeles, CA",
        "description": "We are looking for an experienced Mobile Developer to join our team. You will be responsible for designing, developing, and maintaining mobile applications for both iOS and Android platforms. Your tasks will include building user-friendly mobile interfaces, ensuring app performance, and integrating with back-end systems. You will work closely with UX/UI designers to create seamless and intuitive experiences. The ideal candidate will have strong knowledge of Swift, Kotlin, and React Native. Experience with REST APIs and cloud services is a plus. You will need to ensure the apps are optimized for both performance and battery life.",
        "degree_requirements": "Bachelor's degree in Computer Science, Information Technology, or related field."
    },
    {
        "id": "23124",
        "title": "DevOps Engineer",
        "company": "CloudTech Solutions",
        "location": "98 DevOps Way, Dallas, TX",
        "description": "As a DevOps Engineer, you will play a key role in automating and improving the development lifecycle. Your responsibilities will include creating and maintaining CI/CD pipelines, automating deployment processes, and ensuring infrastructure scalability. You will work closely with development and IT teams to ensure smooth and efficient deployment of applications. Your expertise in cloud services like AWS or Azure and containerization technologies such as Docker and Kubernetes will be critical. You will also focus on improving system reliability and monitoring the health of production systems. Security best practices will be part of your daily tasks.",
        "degree_requirements": "Bachelor's degree in Computer Science, Engineering, or a related field."
    },
    {
        "id": "43112",
        "title": "Cloud Architect",
        "company": "SkyTech Systems",
        "location": "22 Cloud Lane, Denver, CO",
        "description": "We are seeking a Cloud Architect to design, implement, and manage our cloud infrastructure. You will be responsible for developing and maintaining cloud strategies, overseeing cloud services, and ensuring the cloud environment is secure and efficient. Your role will involve designing cloud architecture that supports business operations and optimizes cost, scalability, and performance. You will also collaborate with teams to ensure the proper deployment and management of cloud resources. Expertise in AWS, Azure, or Google Cloud is essential. You will need to have experience in system architecture, cloud security, and cost optimization.",
        "degree_requirements": "Bachelor's degree in Computer Science, Cloud Computing, or a related field."
    },
    {
        "id": "98712",
        "title": "Systems Administrator",
        "company": "IT Solutions Corp.",
        "location": "85 Admin Lane, Miami, FL",
        "description": "As a Systems Administrator, you will manage and support our IT infrastructure. Your responsibilities will include installing, configuring, and maintaining servers and networks, troubleshooting technical issues, and ensuring that systems run smoothly. You will work with both on-premise and cloud-based systems and will be responsible for monitoring system performance and security. The ideal candidate will have experience with Linux and Windows server environments, as well as networking, virtualization, and database management. You should be proactive in identifying potential issues and implementing solutions before they become critical.",
        "degree_requirements": "Bachelor's degree in Information Technology, Computer Science, or a related field."
    },
    {
        "id": "56487",
        "title": "Network Engineer",
        "company": "NetWorks Global",
        "location": "44 Network Blvd, Atlanta, GA",
        "description": "We are seeking a Network Engineer to design, implement, and support our company's network infrastructure. You will be responsible for configuring and maintaining routers, switches, firewalls, and other networking devices. The role requires troubleshooting network issues, ensuring network security, and optimizing network performance. You will also be involved in planning for future network expansion and upgrades. Strong knowledge of networking protocols, VPNs, and network management tools is essential. A certification such as CCNA or CCNP is preferred, and experience with cloud networking is a plus.",
        "degree_requirements": "Bachelor's degree in Network Engineering, Computer Science, or related field."
    },
    {
        "id": "23156",
        "title": "UX/UI Designer",
        "company": "DesignWorks Studios",
        "location": "10 Design Avenue, Portland, OR",
        "description": "We are looking for a talented UX/UI Designer to join our team. You will work closely with product managers and developers to create intuitive, user-friendly designs for web and mobile applications. Your responsibilities will include conducting user research, creating wireframes and prototypes, and designing user interfaces. You should be proficient in design tools like Figma, Sketch, or Adobe XD. You will need to have an eye for detail and be able to implement designs that are both functional and aesthetically pleasing. Your work will directly impact the user experience, and you will play a key role in the success of our products.",
        "degree_requirements": "Bachelor's degree in Graphic Design, UX/UI Design, or a related field."
    },
    {
        "id": "34567",
        "title": "Cybersecurity Analyst",
        "company": "SecureTech Solutions",
        "location": "65 Security Blvd, San Diego, CA",
        "description": "We are looking for a Cybersecurity Analyst to join our team. Your role will involve monitoring network traffic, identifying potential security risks, and implementing measures to protect sensitive information. You will be responsible for maintaining and improving security protocols, conducting vulnerability assessments, and ensuring compliance with security regulations. You will also respond to incidents and mitigate security breaches. The ideal candidate will have experience with firewalls, intrusion detection systems, and encryption technologies. A strong understanding of security best practices and industry standards is essential.",
        "degree_requirements": "Bachelor's degree in Cybersecurity, Information Security, or a related field."
    },
    {
        "id": "67834",
        "title": "Software Test Engineer",
        "company": "QA Solutions Inc.",
        "location": "34 Test Drive, Orlando, FL",
        "description": "As a Software Test Engineer, you will be responsible for developing and executing tests to ensure the quality of our software products. You will work closely with developers to understand the functionality of the applications and create test plans and cases. Your role will involve manual and automated testing to identify bugs and ensure the software meets the required specifications. You will need to be familiar with testing frameworks such as Selenium, JUnit, or TestNG. You will also work on performance testing, security testing, and ensuring compatibility across different platforms.",
        "degree_requirements": "Bachelor's degree in Computer Science, Software Engineering, or related field."
    },
    {
        "id": "90234",
        "title": "Blockchain Developer",
        "company": "Crypto Innovations",
        "location": "77 Blockchain Ave, Los Angeles, CA",
        "description": "We are seeking a Blockchain Developer to help design and develop blockchain-based applications. Your responsibilities will include creating smart contracts, developing decentralized applications, and working with blockchain platforms like Ethereum or Hyperledger. You will collaborate with other developers to ensure scalability, security, and performance of the blockchain applications. The ideal candidate will have experience with Solidity, JavaScript, and blockchain frameworks. A strong understanding of cryptography, consensus algorithms, and decentralized systems is required.",
        "degree_requirements": "Bachelor's degree in Computer Science, Blockchain Technology, or a related field."
    },
    {
        "id": "10234",
        "title": "Game Developer",
        "company": "Epic Games Studios",
        "location": "55 Game Road, Austin, TX",
        "description": "As a Game Developer, you will be responsible for developing interactive, immersive video games. You will work closely with the design and art teams to implement gameplay features, improve the user experience, and optimize game performance. You will be involved in writing game logic, integrating sound and graphics, and troubleshooting issues. You should be proficient in programming languages like C++, C#, or Unity, and have experience with game engines and frameworks. Your role will involve developing both client-side and server-side components of the game.",
        "degree_requirements": "Bachelor's degree in Computer Science, Game Development, or related field."
    },
    {
        "id": "98324",
        "title": "IT Support Specialist",
        "company": "Tech Helpdesk Solutions",
        "location": "67 Support Blvd, Seattle, WA",
        "description": "We are looking for an IT Support Specialist to provide technical support to our employees and clients. Your responsibilities will include troubleshooting hardware and software issues, setting up new systems, and maintaining IT infrastructure. You will also assist with network administration, managing user accounts, and ensuring that all IT systems are functioning properly. Strong communication skills and a customer service-oriented approach are essential for this role, as you will be the first point of contact for technical issues.",
        "degree_requirements": "Bachelor's degree in Information Technology, Computer Science, or related field."
    },
    {
        "id": "HR001",
        "title": "HR Executive",
        "company": "Studiokon Ventures",
        "location": "Gurugram, Haryana",
        "description": "As an HR Executive, you will be responsible for handling end-to-end recruitment processes, including job postings, screening candidates, conducting interviews, and onboarding new employees. Your role also involves maintaining employee records, ensuring compliance with labor laws, and supporting various HR initiatives such as employee engagement and training programs. You will act as a point of contact between management and employees, addressing concerns and fostering a positive work environment. Excellent communication, organizational, and problem-solving skills are required to excel in this role. Knowledge of HR software and the ability to handle confidential information are essential.",
        "degree_requirements": "Bachelor's degree in Human Resources, Business Administration, or a related field."
    },
    {
        "id": "HR002",
        "title": "Senior HR Executive",
        "company": "Dr Lal PathLabs",
        "location": "Gurugram, Haryana",
        "description": "The Senior HR Executive will manage HR operations, including recruitment, employee relations, performance management, and policy development. Key responsibilities include creating and implementing HR strategies that align with the company's objectives, conducting training sessions, and handling employee grievances. You will also be responsible for compliance with labor laws and company policies. The role requires strong leadership skills, excellent communication abilities, and the capability to manage a team. Previous experience in a similar role, coupled with a strong understanding of HR practices and procedures, is essential to succeed in this position.",
        "degree_requirements": "Bachelor's degree in Human Resources, Business Administration, or a related field; Master's preferred."
    },
    {
        "id": "HR003",
        "title": "HR Manager",
        "company": "Navchitra Designs Private Limited",
        "location": "DLF Phase-III, Gurugram, Haryana",
        "description": "As an HR Manager, you will oversee the overall HR functions, including recruitment, training and development, performance management, and employee engagement. Your role will involve implementing HR policies, managing employee benefits, and ensuring adherence to labor laws and company standards. You will work closely with leadership to align HR strategies with business goals, address employee concerns, and foster a culture of inclusivity and collaboration. The role demands strong decision-making skills, excellent communication, and the ability to lead a team. Prior experience in a managerial HR role is highly desirable.",
        "degree_requirements": "Bachelor's degree in Human Resources or a related field; Master's preferred."
    },
    {
        "id": "HR004",
        "title": "HR Generalist",
        "company": "NMG Technologies",
        "location": "Gurugram, Haryana",
        "description": "The HR Generalist will be responsible for a wide range of HR activities, including recruitment, onboarding, performance management, and compliance with labor laws. In this role, you will collaborate with different departments to support business needs, address employee queries, and drive initiatives to enhance employee engagement and satisfaction. You will also manage payroll processing, employee benefits, and training programs. Strong interpersonal skills, attention to detail, and a deep understanding of HR best practices are crucial for this role. Familiarity with HR tools and technology will be an added advantage.",
        "degree_requirements": "Bachelor's degree in Human Resources, Business Administration, or a related field."
    },
    {
        "id": "HR005",
        "title": "Human Resources Specialist - Employee Relations",
        "company": "Boston Consulting Group",
        "location": "Gurugram, Haryana",
        "description": "In this role, you will focus on maintaining positive employee relations by addressing grievances, conducting investigations, and ensuring a safe and inclusive workplace. You will provide expert advice on employment laws and company policies, mediate conflicts, and implement programs to enhance workplace culture. Additional responsibilities include supporting diversity and inclusion initiatives, organizing training sessions, and maintaining accurate employee records. The ideal candidate should possess strong problem-solving skills, excellent communication abilities, and a thorough understanding of employment regulations. Prior experience in employee relations or a related field is highly preferred.",
        "degree_requirements": "Bachelor's degree in Human Resources, Law, or a related field."
    },
    {
        "id": "HR006",
        "title": "HR Business Partner",
        "company": "Infosys",
        "location": "Bengaluru, Karnataka",
        "description": "As an HR Business Partner, you will act as a strategic advisor to business leaders, aligning HR strategies with organizational objectives. Your responsibilities include workforce planning, succession planning, employee engagement, and resolving employee relations issues. You will also lead initiatives to enhance productivity and foster a high-performance culture. This role requires strong analytical skills, excellent communication, and the ability to build relationships across all levels of the organization. Prior experience as an HRBP or in a similar role is essential for success in this position.",
        "degree_requirements": "Bachelor's degree in Human Resources, Business Administration, or a related field; MBA preferred."
    },
    {
        "id": "HR007",
        "title": "Recruitment Specialist",
        "company": "Tata Consultancy Services",
        "location": "Mumbai, Maharashtra",
        "description": "As a Recruitment Specialist, you will be responsible for sourcing, screening, and hiring top talent to meet the organization's staffing needs. Your duties will include coordinating with hiring managers, posting job advertisements, and conducting interviews. You will also play a key role in improving the recruitment process, ensuring timely onboarding, and maintaining a talent pipeline. The ideal candidate will have excellent interpersonal skills, a deep understanding of recruitment strategies, and the ability to work in a fast-paced environment. Experience in tech hiring will be an added advantage.",
        "degree_requirements": "Bachelor's degree in Human Resources or a related field."
    },
    {
        "id": "HR008",
        "title": "Talent Acquisition Manager",
        "company": "Accenture",
        "location": "Hyderabad, Telangana",
        "description": "The Talent Acquisition Manager will lead a team of recruiters to attract and hire top talent for the organization. Your responsibilities include developing recruitment strategies, managing relationships with recruitment agencies, and ensuring an excellent candidate experience. You will collaborate with business leaders to forecast hiring needs and build a robust talent pipeline. The role requires strong leadership skills, a strategic mindset, and a proven track record in managing large-scale recruitment efforts. Familiarity with applicant tracking systems (ATS) and metrics-driven hiring processes is essential.",
        "degree_requirements": "Bachelor's degree in Human Resources, Business Administration, or a related field; MBA preferred."
    },
    {
        "id": "HR009",
        "title": "HR Coordinator",
        "company": "Amazon",
        "location": "Delhi, India",
        "description": "The HR Coordinator will provide administrative support to the HR department, ensuring smooth operations and effective communication. Responsibilities include maintaining employee records, coordinating training sessions, assisting with recruitment logistics, and supporting HR projects. You will also handle employee queries related to policies and procedures. This role requires exceptional organizational skills, attention to detail, and proficiency in HR software. Strong communication and multitasking abilities are crucial to succeed in this position. Prior experience in a similar role is advantageous but not mandatory.",
        "degree_requirements": "Bachelor's degree in Human Resources or a related field."
    },
    {
        "id": "HR010",
        "title": "Learning and Development Specialist",
        "company": "Wipro",
        "location": "Pune, Maharashtra",
        "description": "As a Learning and Development Specialist, you will design, implement, and evaluate training programs to enhance employee skills and performance. Your role involves identifying training needs, creating learning materials, and facilitating workshops. You will work closely with managers to align training initiatives with organizational goals and measure the effectiveness of programs. Strong communication skills, creativity, and a passion for employee development are essential. Familiarity with e-learning tools and experience in instructional design will be considered an advantage.",
        "degree_requirements": "Bachelor's degree in Human Resources, Education, or a related field."
    },
    {
        "id": "HR011",
        "title": "Compensation and Benefits Manager",
        "company": "Deloitte",
        "location": "Chennai, Tamil Nadu",
        "description": "The Compensation and Benefits Manager will oversee the design and implementation of employee compensation and benefits programs. Responsibilities include conducting market analyses, developing salary structures, managing bonus programs, and ensuring compliance with labor laws. You will also evaluate and negotiate benefits packages to attract and retain talent. This role requires a strong understanding of HR metrics, excellent analytical skills, and a proactive approach to problem-solving. Prior experience in compensation management is essential for this position.",
        "degree_requirements": "Bachelor's degree in Human Resources, Finance, or a related field; MBA preferred."
    },
    {
        "id": "HR012",
        "title": "HR Technology Specialist",
        "company": "Capgemini",
        "location": "Noida, Uttar Pradesh",
        "description": "As an HR Technology Specialist, you will be responsible for managing HR systems and tools to enhance operational efficiency. Your duties include system implementation, troubleshooting technical issues, and training employees on HR software. You will also analyze HR data to provide insights and support decision-making. Strong technical skills, knowledge of HRIS platforms, and an analytical mindset are essential for this role. Experience in integrating and optimizing HR technology solutions will be highly valued.",
        "degree_requirements": "Bachelor's degree in Information Technology, Human Resources, or a related field."
    },
    {
        "id": "HR013",
        "title": "Diversity and Inclusion Manager",
        "company": "Microsoft",
        "location": "Bengaluru, Karnataka",
        "description": "The Diversity and Inclusion Manager will lead initiatives to promote diversity, equity, and inclusion across the organization. Your responsibilities include developing strategies, conducting training sessions, and ensuring representation in hiring practices. You will collaborate with leadership to create a culture that values diversity and address any challenges related to inclusivity. Strong communication skills, a strategic mindset, and a passion for social equity are critical for this role. Prior experience in DEI roles will be an added advantage.",
        "degree_requirements": "Bachelor's degree in Human Resources, Sociology, or a related field."
    },
    {
        "id": "HR014",
        "title": "HR Analyst",
        "company": "IBM",
        "location": "Kolkata, West Bengal",
        "description": "As an HR Analyst, you will be responsible for analyzing HR data to provide insights that support strategic decision-making. Your duties include creating reports, tracking key metrics, and identifying trends in employee performance and satisfaction. You will also support workforce planning and budgeting processes. The ideal candidate will have strong analytical skills, proficiency in data visualization tools, and the ability to interpret complex data sets. Experience in HR analytics or a similar role is highly desirable.",
        "degree_requirements": "Bachelor's degree in Human Resources, Statistics, or a related field."
    }
    ,
        {
            "id": "TEACH001",
            "title": "Mathematics Teacher",
            "company": "Bright Future High School",
            "location": "Pune, Maharashtra",
            "description": "As a Mathematics Teacher, you will be responsible for delivering engaging lessons that foster a love for math among students. Your duties include preparing lesson plans, assessing student performance, and providing additional support to struggling students. You will also be expected to organize math-related activities and competitions to promote problem-solving skills. The ideal candidate should have excellent communication skills, patience, and a passion for teaching. Prior experience in a teaching role is preferred.",
            "degree_requirements": "Bachelor's degree in Mathematics or Education; B.Ed. preferred."
        },
        {
            "id": "TEACH002",
            "title": "Science Teacher",
            "company": "Oakridge International School",
            "location": "Hyderabad, Telangana",
            "description": "As a Science Teacher, you will create and implement lesson plans to teach concepts in physics, chemistry, and biology to middle or high school students. Responsibilities include conducting experiments, fostering critical thinking, and using innovative teaching methods to make science engaging. You will also evaluate students' progress and provide constructive feedback. The ideal candidate should have strong subject knowledge, excellent communication skills, and a commitment to inspiring a love for science.",
            "degree_requirements": "Bachelor's degree in Science or Education; Master's degree preferred."
        },
        {
            "id": "TEACH003",
            "title": "English Teacher",
            "company": "Green Valley Academy",
            "location": "Delhi, India",
            "description": "As an English Teacher, you will be responsible for teaching grammar, literature, and creative writing to students. Your tasks will include developing lesson plans, conducting reading sessions, and encouraging students to express themselves through writing. You will also organize debates and presentations to enhance their communication skills. The ideal candidate should have excellent command over the English language, creativity, and a passion for teaching. Experience in curriculum development will be an added advantage.",
            "degree_requirements": "Bachelor's degree in English or Education; B.Ed. preferred."
        },
        {
            "id": "TEACH004",
            "title": "Computer Science Teacher",
            "company": "Global Tech School",
            "location": "Bengaluru, Karnataka",
            "description": "As a Computer Science Teacher, you will teach programming, data structures, and other computer-related topics to students. Your role includes designing practical projects, conducting coding workshops, and preparing students for technology competitions. You will also guide students in understanding the applications of technology in real-world scenarios. The ideal candidate should have a strong technical background, excellent teaching skills, and the ability to make complex concepts understandable.",
            "degree_requirements": "Bachelor's degree in Computer Science or Education; Master's preferred."
        },
        {
            "id": "TEACH005",
            "title": "History Teacher",
            "company": "The Heritage School",
            "location": "Chennai, Tamil Nadu",
            "description": "As a History Teacher, you will educate students about historical events, cultures, and their significance. Your duties include preparing engaging lessons, organizing field trips to historical sites, and encouraging critical discussions on historical perspectives. You will also guide students in preparing research projects and presentations. The ideal candidate should have excellent storytelling abilities, a passion for history, and strong classroom management skills.",
            "degree_requirements": "Bachelor's degree in History or Education; B.Ed. preferred."
        },
        {
            "id": "TEACH006",
            "title": "Primary School Teacher",
            "company": "Little Scholars Academy",
            "location": "Mumbai, Maharashtra",
            "description": "As a Primary School Teacher, you will be responsible for teaching foundational subjects, fostering a positive learning environment, and nurturing young learners. Responsibilities include preparing lesson plans, assessing student progress, and engaging students in creative activities. You will also communicate with parents about their child's development. Patience, creativity, and strong organizational skills are essential for this role. Experience in early childhood education is preferred.",
            "degree_requirements": "Bachelor's degree in Education or a related field; B.Ed. preferred."
        },
        {
            "id": "TEACH007",
            "title": "Physical Education Teacher",
            "company": "Fitness First School",
            "location": "Ahmedabad, Gujarat",
            "description": "As a Physical Education Teacher, you will promote physical fitness and teach sports to students. Your responsibilities include organizing physical activities, monitoring student fitness levels, and encouraging teamwork and sportsmanship. You will also plan school sports events and provide guidance to students interested in competitive sports. The ideal candidate should have excellent fitness knowledge, strong motivational skills, and the ability to inspire a healthy lifestyle.",
            "degree_requirements": "Bachelor's degree in Physical Education or a related field."
        },
        {
            "id": "TEACH008",
            "title": "Art Teacher",
            "company": "Creative Minds Academy",
            "location": "Kolkata, West Bengal",
            "description": "As an Art Teacher, you will inspire students to express their creativity through various art forms. Your responsibilities include teaching techniques in drawing, painting, and sculpture, organizing art exhibitions, and guiding students in developing their portfolios. You will also integrate art into interdisciplinary projects to enhance overall learning. A passion for art, strong communication skills, and the ability to nurture creativity are essential for this role.",
            "degree_requirements": "Bachelor's degree in Fine Arts or Education; MFA preferred."
        },
        {
            "id": "TEACH009",
            "title": "Music Teacher",
            "company": "Harmony School of Music",
            "location": "Lucknow, Uttar Pradesh",
            "description": "As a Music Teacher, you will teach students the fundamentals of music, including theory, composition, and performance. Responsibilities include organizing music classes, conducting choir sessions, and preparing students for musical competitions. You will also foster an appreciation for music and guide students in mastering their instruments. The ideal candidate should have a strong musical background, excellent teaching skills, and a passion for nurturing musical talent.",
            "degree_requirements": "Bachelor's degree in Music or Education."
        },
        {
            "id": "TEACH010",
            "title": "Economics Teacher",
            "company": "Scholars Academy",
            "location": "Jaipur, Rajasthan",
            "description": "As an Economics Teacher, you will educate students on economic principles, market dynamics, and global financial systems. Your duties include preparing lesson plans, conducting discussions on economic policies, and helping students analyze real-world economic issues. You will also guide students in preparing for exams and competitive assessments. A strong knowledge of economics, excellent communication skills, and the ability to engage students in critical thinking are essential for this role.",
            "degree_requirements": "Bachelor's degree in Economics or Education; Master's preferred."
        }
    ]
  
class Scraper:

    def __init__(self, proxies=None):
        
        self.proxies = proxies
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }

    def scrape(self, keywords):
       
        # for keyword in keywords:
        #     base_url = f'https://apna.co/jobs?search=true&text={keyword}'
        #     print(f"Scraping URL: {base_url}")
            
        #     try:
        #         response = requests.get(base_url, headers=self.headers, proxies=self.proxies, timeout=10)
        #         response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
                
        #         html_content = response.text
        #         page_data = self.parse(html_content)
        #         job_data.extend(page_data)

        #     except requests.exceptions.RequestException as e:
        #         print(f"Error fetching jobs for keyword '{keyword}': {e}")

        return job_data

    def parse(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        jobs = []
        script_tags = soup.find_all("script", {"type": "application/json"})

        for script_tag in script_tags:
            try:
                script_content = script_tag.string
                job_data = json.loads(script_content)

                if 'props' in job_data and 'pageProps' in job_data['props']:
                    jobs_data = job_data['props']['pageProps'].get('jobs', [])
                    
                    for job in jobs_data:
                        job_details = job['data']
                        description = self.scrape_description(job_details.get('id'))
                        extracted_job = {
                            'id': job_details.get('id', 'N/A'),
                            'title': job_details.get('title', 'N/A'),
                            'company': job_details.get('organization', {}).get('name', 'N/A'),
                            'location': job_details.get('address', {}).get('line_1', 'N/A'),
                            'description': description.get('description', 'N/A'),
                            'degree_requirements': description.get('degree_requirements', 'N/A')
                        }
                        jobs.append(extracted_job)

            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error parsing script content: {e}")

        return jobs

    def scrape_description(self, job_id):
        base_url = f'https://apna.co/job/{job_id}'
        print(f"Scraping job description URL: {base_url}")

        try:
            response = requests.get(base_url, headers=self.headers, proxies=self.proxies, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            html_content = response.text
            return self.parse_description(html_content)

        except requests.exceptions.RequestException as e:
            return {'degree_requirements': 'N/A', 'description': 'N/A'}

    def parse_description(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        script_tags = soup.find_all("script", {"type": "application/json"})

        for script_tag in script_tags:
            try:
                script_content = script_tag.string
                job_data = json.loads(script_content)

                if 'props' in job_data and 'pageProps' in job_data['props']:
                    job_details = job_data['props']['pageProps'].get('job', {})
                    degree_requirements = job_details.get('degree_requirements', {})
                    degree_subtitle = BeautifulSoup(
                        degree_requirements.get('subtitle', 'N/A'), 'html.parser'
                    ).get_text(strip=True) if degree_requirements else 'N/A'
                    description = BeautifulSoup(
                        job_details.get('description', 'N/A'), 'html.parser'
                    ).get_text(strip=True)
                    return {
                        'degree_requirements': degree_subtitle,
                        'description': description
                    }

            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error parsing job description content: {e}")

        return {'degree_requirements': 'N/A', 'description': 'N/A'}
