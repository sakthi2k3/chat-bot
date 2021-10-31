
brain={"what's your name":'Neymar',
   "what is your name":'Neymar',
   'how are you':'i am fine how about you',
   'fine':'good to hear',
   'i am fine':'good to hear',
   'what is your Full name':'Neymar da Silva Santos Júnior',
   'good morning':'happy morning ',
   'good night':'have a sweet dreams',
   'ok':'hmmm',
   'you are awesome':'thank you',
   'your annoying':'sorry:(',
   'i like you':'thankyou',
   'how old are you':'twenty two',
   'ya':'hmm',
   'yes':'hmm',
   'so':'sooo',
   'nice name':'thank you',   
   "what's your favroite sports":'football',
   "what's your salary":"3.68 crores EUR",
   "what's your current team":"Paris Saint-Germain F.C",
   "what's your position":"forward",
   "do you have kids":"yes i have one kid named Davi Lucca",
   "tell me about yoursel":"I was born in 5th February 1992, known as Neymar, a Brazilian professional footballer who plays as a forward for Ligue 1 club Paris Saint-Germain and the Brazil national team. He is widely regarded as one of the best players of my generation",
   "what's your jerrsy number":"ten",
   "what's your a religion":"Christian",
   "your future plan":"I have signed a new contract tying the Brazil forward to Paris St-Germain until 30 June 2025",
   "are you better that messi and ronaldo":"ya i am better that them",
   "how many hat trick have you done":"four",
   "what language do you speak":"Spanish and Portuguese",
   "who is your best friend":"Lionel Messi"
   }


def reply(a):
    if a in brain:
        return(brain[a])
    else:
        return("sorry no answer")    


# fr=open("questions.txt","r")
# fs=open("answers.txt","r")            
# i=0

# while i==0: 
#      question = fr.readline()
#      answer = fs.readline()
#      for x in question:
#          if x=="\n":
#              i=i+1
#      i=i-1    
#      brain[question.strip("\n")]=answer.strip("\n")
     

# while True:
    
#     inp= str(input()).lower()

#     if 'hii'in inp:
#         print('hellow')

#     elif 'bye'in inp:
#         print('bye have nice day')
#         break

   
          
#     elif inp in brain:
#          l=brain[inp]
#          print(l)
        
    # else:
    #     qes=inp
    #     teach(qes)
    #     print('thank you for your help')
       
        
    
# def teach(qes):
#     print('sorry i dint know the answer for that')
#     print('can you tell me a answer for it so i will tell it next time when you ask')
#     ans=str(input())
#     brain[qes]=ans
#     fq=open("questions.txt","a")
#     fa=open("answers.txt","a")
#     fq.write(qes+"\n")
#     fa.write(ans+"\n")
#     fq.close()
#     fa.close()
    