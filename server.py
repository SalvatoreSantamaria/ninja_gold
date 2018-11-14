from flask import Flask, render_template, request, redirect, session

import random # import the random module
# The random module has many useful functions. This is one that gives a random number in a range
# random.randrange(0, 101) # random number between 0-100

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # Set a secret key for security purposes

# Routing rules and rest of server.py below
# our index route will handle rendering our form


@app.route('/')
def index():
    session['gold_total'] #did not set it to a number, because elsewise it would reset every time here
    print(session['gold_total'])
    session['message']
    
    # render the index template
    return render_template("index.html", x = session['gold_total'], m = session['message'] )

@app.route('/process_money', methods=['POST'])
    # when a button is pressed, fire the below
def processor():
#     print(request.form['user_guess'])
#     print(session['random_number'])
#     print(session)

    # print(session['gold_total'])
    # print('button press')
    result = request.form # print(request.form.items()) prints weird, why?
    # message = ' '
    # a = request.form['name'] #how would I get this to work?
    # print(a + 'request.form[name]') #how would I get this to work?

    for key, value in result.items(): #loops through the object to find the keys and values
        # print(key, value) this will print the key and value
        if value == 'farm':
            # print(value + ' was pressed!')
            farm_random_num = random.randrange(9, 21) # generate a random number
            session['gold_total'] += farm_random_num
            session['message'] += "<p class='gainmoney'>"  + str(farm_random_num) + ' gold gained from farming!' + "</p>"
            print(session['message'])
            # + farm_random_num +

        if value == 'cave':
            print(value + ' was pressed!')
            cave_random_num = random.randrange(4, 11) # generate a random number
            session['gold_total'] += cave_random_num
            session['message'] += "<p class='gainmoney'>"  + str(cave_random_num) + ' gold found in the cave!' + "</p>"

        if value == 'house':
            print(value + ' was pressed!')
            house_random_num = random.randrange(1, 6) # generate a random number
            session['gold_total'] += house_random_num
            session['message'] += "<p class='gainmoney'>"  + str(house_random_num) + ' gold found in a house!' + "</p>"

        if value == 'casino':
            print(value + ' was pressed!')
            casino_random_num = random.randrange(-51, 51) # generate a random number
            session['gold_total'] += casino_random_num
            if casino_random_num > 0:
                session['message'] += "<p class='gainmoney'>"  + str(casino_random_num) + ' gold won in the Casino!' + "</p>"
            if casino_random_num < 0:
                session['message'] += "<p class='lostmoney'>"  + str(casino_random_num) + ' gold lost in the Casino!' + "</p>"

    # if request.form['name'] == 'casino':
        # print('Casino was pressed')
    return redirect('/')  

@app.route('/reset')
def destroy_session():
    print("Session Destroyed")
    session.clear() #clears session
    return redirect('/')


















# Old Code for reference below


# # guess is low
#     if int(session['random_number']) > int(request.form['user_guess']):
#         print('Too Low')
#         return render_template('index.html', u_guess = request.form['user_guess'] + ' is too low')  

# # guess is high
#     if int(session['random_number']) < int(request.form['user_guess']):
#         print('Too High')
#         return render_template('index.html', u_guess = request.form['user_guess'] + ' is too high')  

# # guess is correct. render_template is intructed to pass 'guessed = True' through jinja so the template knows to generate the reset button
#     if int(session['random_number']) == int(request.form['user_guess']):
#         print(session['random_number'], 'was the number!')
#         return render_template('index.html', u_guess = request.form['user_guess'] + ' is the number!', guessed = True) 

# # this route is for the reset button. a new random number is generated
# @app.route('/reset', methods=['POST'])
# def restfunction():   
#     session['random_number'] = random.randrange(1, 101)
#     return render_template('index.html')    



















                       
if __name__=="__main__":
    # run our server
    app.run(debug=True) 