from flask import Flask, render_template, request, redirect
                                          
app = Flask(__name__)                     
                                          
@app.route('/')                                                                                 
def whatsyourname():
    
    return render_template('index.html')   

@app.route('/process', methods=['POST'])                                                                                 
def your_name():
    
    name2 = request.form['name1']
    return render_template('index.html', name3 = name2)   
    return redirect('/')

app.run(debug=True)