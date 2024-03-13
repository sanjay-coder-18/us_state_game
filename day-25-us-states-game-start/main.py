from turtle import Turtle,Screen
import pandas
turtle=Turtle()
t=Turtle()
screen=Screen()
screen.title('US States Game')
screen.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')
game_on=True
score=0
data=pandas.read_csv('50_states.csv')
collection=data.state.str.lower().to_list()
print(collection)
data_list=data['state'].str.lower()
guessed=[]

while score <50:
    answer=screen.textinput(title=f"Score={score}  Guess the state  " ,prompt="Type the state name").lower()
    print(f'answer {answer}')
    if answer=="exit":
        break

    if answer in data_list.values:
        
        score+=1
        guessed.append(answer)
        collection.remove(answer)
        print(guessed)
        x= data[data['state'].str.lower()== answer]
        m=x['x'].values[0]
        y=data[data['state'].str.lower()==answer]
        n=y['y'].values[0]
        print(m)
        print(n)
        t.hideturtle()
        t.penup()
        t.goto(m,n)
        t.pendown()
        t.write(f"{answer}", font=("Arial", 12, "normal"))


# state_to_learn

new_data=pandas.DataFrame(collection)
new_data.to_csv('state_to_learn.csv')

        




