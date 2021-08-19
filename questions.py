class Questions():
    def __init__(self):
        self.ques = ["color of cricket ball?\nA)white\nB)black\nC)pink\nD)blue", "cat says?\nA)meow\nB)bow\nC)chrip\nD)none", "Sachin Tendulkar is also known as\nA)Dada\nB)God of Cricket\nC)Captain India\nD)Google Master", "Who is considered to be the God of War in Greek Mythology?\nA)Theseus\nB)Ares\nC)Kronos\nD)Hera, What is the approximate height of the International Space Station from the ground?\nA)250 km\nB)410 km\nC)323 km\nD)443 km", "Who is called 'The Father of the Atom bomb'?\nA)Jan Koum\nB)Brian Action\nC)Oppenheimer\nD)Charles Sweeney", "Pick the odd one out in the following options.\nA)Hausa\nB)Guarani\nC)Quechua\nD)Takoyaki", "Who is the first person from india to win a gold medal individually in the olympics?\nA)Karnam Malleshwari\nB)Sakshi  Malikk\nC)Abhinav Bindra\nD)Leander Paes", "Who led the first expedition to Antarctica?\nA)Roald Amudsen\nB)Jonathan Kristie\nC)Lewis Hamilton\nD)Terry Kane", "Who shot Mahatma Gandhi?\nA)Sir Arthur Cotton\nB)Nathuram Godsey\nC)Roger Drake\nD)Holwell", "Who is the first person to step onto the moon?\nA)Buzz Aldrin\nB)Yuri Gagarin\nC)Neil Armstrong\nD)Alan Shepard", "What is the most powerful telescope on earth?\nA)Spitzer\nB)Fermi Gamma Ray\nC)Kepler\nD)Hubble", "What is the height of the heighest mountain  in the world (in metres)?\nA)4232\nB)2593\nC)8848\nD)6634", "What is the fastest ball in the cricket history?\nA)142.4\nB)183.3\nC)161.3\nD)185.2 kph", "Which metal is the most expensive?\nA)Plutonium\nB)Rhodium\nC)Platinum\nD)Gold", "What is the deepest point on the earth?\nA)Tiger's point\nB)The Dark Lake\nC)Lion's shallow\nD)Mariana Trench", "Which is the toughest exam in the whole world?\nA)IIT-JEE\nB)Gaokao\nC)Gate\nD)CCIE", "Which is the country with highest HDI in 2018?\nA)Switzerland\nB)Norway\nC)Australia\nD)Denmark", "Who is the father of computer?\nA)Charles Darwin\nB)Jack Kilby\nC)Charles Babbage\nD)Robert Noyce", "Who is the current governor of Assam?\nA)Jagdish Mukhi\nB)Kalyan Singh\nC)Mishra\nD)Ram Kovind"]
        self.ans = ["A","A","B", "B", "B", "C", "D", "C", "A", "B", "C", "D", "C", "C", "B", "D", "D", "B", "C", "A"]

    def quest(self,k):
        return self.ques[k]

    def answer(self,k):
        return self.ans[k]

    def length(self):
        return len(self.ques)

