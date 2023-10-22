quiz = {
    "Question1" :{
    "Question" : " what is Capital of Canada? " ,
    "answer" : "Ottawa"
    },

      "Question2" :{
    "Question" : " what is Capital of Oman? " ,
    "answer" : "Muscat"
    },
    
         "Question3" :{
    "Question" : " what is Capital of Russia? " ,
    "answer" : "Moscow"
    },

         "Question4" :{
    "Question" : " what is Capital of US? " ,
    "answer" : "New York"
    },

         "Question5" :{
    "Question" : " what is Capital of UK? " ,
    "answer" : "London"
    },
}

score = 0 

for key, value in quiz.items ():
    print ( value['Question']) 
    ansewr = input ("Pls Write Yor Ansewr : ")

    if ansewr.lower () == value ['answer'].lower ():
        print ('correct !')
        score = score + 1
        print ("Youve got +1 Point! ")
        print ('Total score : ' + str(score))
    
    else :
        print('Wrong !')
        print ('The correct answer is :' + value['answer'])
        print ( "youve Got 0 Point")
        print ('Total score  : ' + str(score)
        )
print ('You got' + str(score) + " Out of 5 Question correctly")
print("your Persentage is" + str(score / 5 * 100) + "%")



