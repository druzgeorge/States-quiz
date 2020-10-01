#! python3
#quizgame.py 

# import modules
import random,os
#cool progress bar
from tqdm import tqdm
from pathlib import Path
import sys
sys.append('.')
#import the states
import states

#create the multiple choice
def multiple_choice(correct_answer,statesdict):
  #prevent repition of states
  returnme = []
  validstates = 0
  while True:
    #break out if all random states have been gotten
    if validstates == 3:
      break
    #get a random state
    tempstate = random.choice(list(statesdict.values()))                    
    #check if state is not repeating
    if tempstate not in returnme:
      returnme.append(tempstate)
      validstates += 1
  #insert correct answer and shuffle
  returnme.append(correct_answer)
  #shuffle
  random.shuffle(returnme)
  #return
  return returnme

#create the quiz and answer files
def create_files(folderpath,filenum,statesdict):
  #make a list of all the states
  states = list(statesdict.keys())
  #shuffle them
  random.shuffle(states)
  #make text file for the quiz
  filename = f'1uiz{filenum}.txt'
  #make text file for answers
  ansfilename = f'cheatsheet{filenum}.txt'
  #open file
  ansfilename = os.path.join(folderpath,ansfilename)
  ansfile  = open(ansfilename, 'w')
  #open files
  quizfilename_path = os.path.join(folderpath, filename)
  with open(quizfilename_path,"w") as quiz:
    #write heading
    quiz.write(" " * 20 + "Capital quiz" + "\n\n")
    #write child details
    quiz.write("Name: " + " " * 10 + "Date: " + " " * 10 + "Subject: Geography" )
    #newlines
    quiz.write("\n\n")
    #loop through states and create questions
    quiznumber = 1
    for state in states:
      quiz.write(str(quiznumber) + f". What is the capital of {state}?")
      quiz.write('\n')
      #multiple choice.
      
      #correct answer
      correctans = statesdict[state]
      #write the correct answer to answer file
      #write the answer and newline
      ansfile.write(f"{str(quiznumber)}: {correctans}")
      ansfile.write("\n\n")
      #get list of multiple choice which are totally random
      possible_answers = multiple_choice(correctans,statesdict)
      #write a possible ans
      quiz.write(f"a: {possible_answers[0]}" + " " * 2)
      #write b
      quiz.write(f"b: {possible_answers[1]}" + " " * 2)
      #write c
      quiz.write(f"c: {possible_answers[2]}" + " " * 2)
      #write d
      quiz.write(f"d: {possible_answers[3]}" + " " * 2)
      #newlines
      quiz.write("\n\n")
      #add 1 to make new question number
      quiznumber += 1
    #note for kids (:{)
    quiz.write("THOUGHT YOU COULD CHEAT HUH?")
    #newline
    quiz.write("\n")
    #close ans file
    ansfile.close()
 quiz.close()
    
    
    

   
#generate 35 diferrent quizes
def main():
  #create folder
  quiz_foldername = ('quizes')
  quiz_folder = os.path.join(os.getcwd(), quiz_foldername)
  #check if the directory is there or not
 if os.path.exists(quiz_folder) :
    print('Quiz folder already exists!')
 else:
    print('Quiz folder does not eixst creating it.')
    #gotta have some progress bars!
    for i in tqdm(range(100)):
      
      print('.', end='', flush=True)
      pass #just do nothing.Just need some progress bars!
  #create 35 files
  for num in range(35):
    #file number
    filenum = num + 1
    #create the files 
    create_files(quiz_folder,filenum,states.states) 
  #Give message
  #need another progress bar
  for i in tqdm(range(100)):
    print('.', end='', flush=True)
  print("Files successfully written")
#run main    
if __name__ == '__main__':
  main()




