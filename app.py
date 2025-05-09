from flask import Flask, render_template, request, jsonify 

app = Flask(__name__)

def process_query(user_query):
    if "select all customers" in user_query.lower():
        sql_query = "SELECT * FROM customers;"
        llm_output = "Select all customers."
        results = [
            {'name': 'John Doe', 'email': 'johndoe@example.com'},
            {'name': 'Jane Smith', 'email': 'janesmith@example.com'},
            {'name': 'Alice Johnson', 'email': 'alicej@example.com'}
        ]
    else:
        sql_query = "SELECT * FROM data;"
        llm_output = "Default query, unrecognized input."
        results = [
            {'name': 'Sample', 'email': 'sample@example.com'},
            {'name': 'Data', 'email': 'data@example.com'}
        ]
    return sql_query, llm_output, results

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_query = request.form['query']
        sql_query, llm_output, results = process_query(user_query)
        return render_template('index.html', query=user_query, sql_query=sql_query, llm_output=llm_output, results=results)
    return render_template('index.html', query=None, sql_query=None, llm_output=None, results=None)

if __name__ == '__main__':
    app.run(debug=True)
