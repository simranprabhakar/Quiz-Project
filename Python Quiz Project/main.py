import pandas as pd
import numpy as np
import random
from string import ascii_lowercase
questions={"Who was First Prime Minister of India":["Jawaharlal Nehru","Narendra Modi","Manmohan Singh","Indira Gandhi"],
           "National Fruit of India":["Mango","Apple","Melon","Grapes"],
           "Clouded Leopard National Park is located in":["Tripura","Sikkim","U.P.","Jammu and Kasmir"],
           "Who is called Father of Biology":["Aristole","Lamarck","Cuvier","Treviranus"],
           "Entomology is the Science that studies":["Insects","Behavior of Human","Formation of rocks","Origin of Planet"],
           "For which of the following disciplines is Nobel Prize awarded?":["All","Literature, Peace and Economics","Physiology or Medicine","Physics and Chemistry"],
           "Exposure to sunlight helps a person improve his health because":["uv rays convert skin oil into Vitamin D","resistance power decreases","the skin cellsget stimulated and produce healthy tan","the infrared light kills bacteria in the body"],
           "First China War was fought between":["China and Britain","China and Greek","China and France","China and Egypt"],
           "Each year World Red Cross and Red Crescent Day is celebrated on":["May 8","June 18","June 8","May 18"],
           "Film and TV institute of India is located at":["Pune (Maharashtra)","Perambur (Tamilnadu)","Pimpri (Maharashtra)","Rajkot (Gujarat)"],
           "Friction can be reduced by changing from":["sliding to rolling","potential energy to kinetic energy","dynamic to static","rolling to sliding"],
           "The Indian Air Force celebrated its Golden Jubilee in":[1982,1962,1989,1972],
           "The main crop of Meghalaya is":["Rice","Barley","Sugacane","Wheat"],
           "The major minerals found in Uttar Pradesh are":["Limestone and Dolomite","Copper and Graphite","Rock phosphate and Dolomite","No minerals"],
           "The main reserves of phosphorus in the biosphere is in":["lithosphere","troposphere","atmosphere","hydrosphere"],
           "The Loktak lake is situated in":["Manipur","Agra","Assam","Kerala"],
           "The Coldest Planet of Our Solar System":["Uranus","Neptune","Earth","Venus"],
           "Longest River in India":["Ganga","Brahmaputra","Tapi","Bhagirathi"],
           "Longest River of World":["Nile","Amazon","Congo","Amur"],
           "Giddha is the folk dance of":["Punjab","Gujarat","U.P.","Assam"],
           "Who was the first President of India":["Dr.Rajendra Prasad","Droupadi Murmu","K.R.Narayanan","Pranab Mukherjee"],
           "Who is known as Father of Indian Constitution":["Dr.B.R.Ambedkar","James Madison","Dr. Rajendra Prasad","Jawaharlal Nehru"],
           "Which is the most sensitive organ in our body":["Skin","Eyes","Brain","Tongue"],
           "Who invented Computer":["Charles Babbage","Douglas Engelbart","Elon Musk","Mark Zuckerberg"],
           "What city is the statue of liberty in":["New York","Mumbai","Sydney","Paris"],
           "Gir National Park in Gujarat is famous for":["Asiatic Lion","One horned Rhino","Asian Eleplant","Giraffe"],
           "Highest dam of India is":["Tehri Dam","Hirakud Dam","Mettur Dam","Ukai Dam"],
           "Who wrote Harry Potter":["J.K.Rowling","Rick Riordan","H.G.Wells","Jonathan Swift"],
           "Cataract is the disease of":["Eyes","Heart","Lungs","Teeth"],
           "Goitre is caused due to the deficiency of":["Iodine","Vitamin B","Vitamin D","Protein"],
           "Olylmpics games are held once after":["4 years","5 years","8 years","10 years"],
           "What is King Arthur's sword called":["Excalibur","Katana","Kilij","Tizona"],
           "Who was popularly known as Netaji?":["Subhash Chandra Bose","Jawaharlal Nehru","Mangal Pandey","Nana Sahib"],
           "Which country does the company Sony come from?":["Japan","China","India","America"],
           "Scientific study of birds is called":["Ornithology","Archaeology","Paleontology","Aetiology"],
           "Who is the author of the book - The Broken Wing:Sound of Love,Death & Destiny?":["Sarojini Naidu","Vikram Seth","Arundhati Roy","Indra Das"],
           "Largest desert in the world is?":["Antartic Desert","Sahara desert","Indian Desert","Gobi Desert"],
           "Kuchipudi is the dance form of which state?":["Andhra Pradesh","Gujarat","Bihar","Assam"],
           "National Education Day":["11Nov","12Nov","11Dec","12Dec"],
           "Which is the smallest bird ?":["Bee Humming Bird","Songbird","Kinglet","Kiwi"],
           "Which is the largest ocean in the world ?":["Pacific Ocean","Arctic Ocean","Indian Ocean","Atlantic Ocean"],
           "Which is India's largest fresh water lake?":["Wular Lake","Chilka Lake","Dal Lake","Lonar Lake"],
           "Which is the tallest waterfall in the world ?":["Angel Falls","Niagara Fall","Iguazu Falls","Victoria Falls"],
           "Narendra Modi was the Chief Minister of which states?":["Gujarat","Assam","Kerala","Odisha"],
           "Name the first female Indian Astronaut":["Kalpana Chawla","Sally Ride","Samantha Christoforetti","Sunita Willams"],
           "Who was the first Indian to go to space?":["Rakesh Sharma","Raja Chari","Anil Menon","Ravish Malhotra"],
           "Who was India's longest serving Prime Minister?":["Jawaharlal Nehru","Narendra Modi","Manmohan Singh","Indira Gandhi"],
           "Which is the smallest continent?":["Australia","Africa","Asia","Europe"],
           "Who invented the telephone?":["Alexander Graham Bell","Galileo Galilei","Marie Curie","C.V.Raman"],
           "Which acid is found in lemon?":["Citric Acid","Acetic Acid","Nitric Acid","Hydrochloric Acid"],
           "Madhubani is popular in which of the following states in India?":["Bihar","Kerala","Maharashtra","Punjab"],
           "What is the full form of AM?":["Ante Meridiem","Antei Meridim","Ante Meridem","Anti Meridiem"],
           "Who wrote Panchatantra":["Vishnu Sharma","Mirabai","Kalidasa","Gulzar"],
           "Who among the followinghas won first Nobel Peace Prize and was born in Madha Pradesh ?":["Kailash Satyarthi","Rabindranath Tagore","Amartya Kumar Sen","H.Gobind Khorana"],
           "Name the highest mountain peak of India":["Mount Kanchenjunga","Nanda Devi","Jongsong Peak","K12"],
           "What is the ratio of width to the length of National Flag of India?":["2:3","1:3","2:5","4:3"],
           "Which gas commonly known as laughing gas":["Nitrous oxide","Nitrogen Dioxide","Acetylene","Nitric monoxide"],
           "Gandhi Ji started the Dandi March in?":["1930","1932","1927","1925"],
           "Who was known as the Indian Napoleon?":["Samudragupta","Maharana Pratap","Ashoka","Humayun"],
           "Who gave the slogan Do or Die?":["Mahatma Gandhi","Subhash Chandra Bose","Bal Gangadhar Tilak","Bhagat Singh"],
           "What is the distance between Earth and Sun?":["147.31 Million km","148.73 Million km","151.64 Million km","149.45 Million km"],
           "Which is the first biosphere reserve in India?":["Nilgiri Biosphere Reserve","Nanda Devi Biosphere Reserve","Great Nicobar Biosphere Reserve","Gulf of Mannar Biosphere Reserve"],
           "Who Record formula of Gunpowder":["Roger Bacon","G. Ferdinand Von Zeppelin","Sir Frank Whittle","Leo H Baekeland"],
           "Who invented the ballpoint pen?":["Biro Brothers","Bicc Brothers","Waterman Brothers","Write Brothers"],
           "Which of the following metals was not known during the Indus Valley Civilization?":["Iron","Silver","Copper","Gold"],
           "Dancing girl (Bronze) is found in which of the following civilzation?":["Indus Valley Civilization","Mesopotamian Civilization","Persian Civilization","Egyptian Civilization"],
           "Which of the following Indian literature is the earliest known works?":["Rig Vedas","Puranas","Sama Vedas","Rajtrangini"],
           "In India, Ancient Iron Age is attached with":["Gray pottery","Black and Red Pottery"," Ocher Coloured Pottery","Northern Black Polish Pottery"],
           "Halley’s comet appears once in a period of ":["76 years","84 years","74 years","86 years"],
           "Why stars look more in west than east?":["Earth is moving from west to east","Earth is moving from east to west","Earth is moving around the Sun","Universe is moving from east to west"],
           "Sirius, the brightest star outside of the Solar System, is also called":["Dog star","Lion star","Cat star","Fox star"],
           "Who of the following discovered the laws of planetary orbits?":["Johannes Kepler","Isaac Newton","Nicholas Copernicus","Galileo Galilei"],
           "The planet with the maximum number of satellites is":["Saturn","Uranus","Jupiter","Neptune"],
           "The outermost layer of Sun is called":["Corona","Convection zone","Chromosphere","Photosphere"],
           "An investor invests in assets known as ":["Portfolio","Block of Assets","Securities","Assets Holder"],
           "The currency Rial is of":["Iran","Indonesia","Namibia","Zambia"],
           "Which of the following gods is also known as ‘Gauri Nandan’":["Ganesha","Hanuman","Agni","Indra"],
           "The wife of which of these famous sports persons was once captain of Indian volleyball team":["Milkha Singh","Prakash Padukone","Dhyan Chand","K.D.Jadav"],
           "The Central Command of Army is located at":["Lucknow","Udhampur","Mhow","Pune"],
           "What is the full form of SQL?":["Structured Query Language","Simple Query List","Structured Query List","Simple Query Language"],
           "Which is the subset of SQL commands used to manipulate Oracle Database structures, including tables?":["Data Definition Language(DDL)","Data Manipulation Language(DML)","Both","None"],
           "The tree which sends down roots from its branches to the soil is known as:":["Banyan","palm","Pine","Oak"],
           "Chlorophyll is a naturally occurring chelate compound in which central metal is":["Magnesium","Calcium","Copper","Iron"],
           "Quartz crystals normally used in quartz clocks etc. is chemically":["Silicon Dioxide","Sodium Silicate","Germanium Oxide","A mixture of Germanium Oxide and Silicon dioxide"],
           "Water is a good solvent of ionic salts because:":["It has a high dipole moment","It has a high boiling point","It has no colour","It has a high specific heat"],
           "The main constituents of pearls are":["Calcium Carbonate","Magnesium Carbonate","Calcium Oxide","Ammonium Sulphate"],
           "'.MPG' extension refers usually to what kind of file?":["Animation/movie file","WordPerfect Document file","MS Office document","Image"],
           "Who developed Yahoo?":["David Filo & Jerry Yang","Dennis Ritchie & Ken Thompson","Vint Cerf & Robert Kahn","Steve Case & Jeff Bezos"],
           "Who is the father of English Poetry?":["Geoffrey Chaucer","William Wordsworth","John Milton","Charles Dickens"],
           "In which year was the 'All India Radio' set up .":["1936","1950","1947","1927"],
           "The first death anniversary day of Sri Rajiv Gandhi was observed as the":["Anti-Terrorism Day","Secularism Day","Peace and Love Day","National Integration Day"],
           "Pigmentation of skin is due to":["melanocytes","leucocytes","monocytes","lymphocytes"],
           "Our major foods,fibres,spices,fruits and beverage crops are":["flowering plants","gymnosperms plants","pteridophytes","bryophytes"],
           "B.C.Roy Award is given in the field of":["Medicine","Environment","Journalism","Music"],
           "The first black American to win the Nobel Prize for literature is":["Toni Morrison","Arthur Ashe","Martin Luther King","Nelson Mandela"],
           "National Institute of Aeronautical Engineering is located at":["Dehradun","Kanpur","Bangalore","Lucknow"],
           "The famous Rock Garden is located in which city?":["Chandigarh","Jaipur","Simla","Lucknow"],
           "The largest and the oldest museum of India is located in the state/union territory of":["West Bengal","Uttar Pradesh","Andhra Pradesh","New Delhi"],
           "'Apsara' is the name of India's first":["Nuclear Reactor","Railway Locomotive","Ground Battle Tank","Helicopter"],
           "Sun Temple is situated at?":["Konark","Bangalore","Haridwar","Kerala"],
           "Who elects the Vice President of India":["Both Houses of Parliament","Council of States","Both Houses of Parliament and state legislatures","House of the People"]}
print(questions)
df=pd.DataFrame(questions)
df.to_csv('Quiz.csv',na_rep='NULL',index=False)

