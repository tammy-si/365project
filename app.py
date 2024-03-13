from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__, static_folder="static")


@app.route('/')
@app.route('/home')
def index():
    connect = sqlite3.connect('boxoffice.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM Movie')

    data = cursor.fetchall()
    res_data = []
    for value in data:
        new_movie = {
            "movie_id": value[0],
            "movie_title": value[1],
            "release_date": value[2],
            "budget": value[3],
            "director_id": value[4],
            "studio_id": value[5],
            "sales_record_id": value[6]
        }
        res_data.append(new_movie)
    return render_template('index.html', data=res_data)



@app.route('/director/<int:director_id>', methods=['GET'])
def getDirector(director_id):
    connect = sqlite3.connect('boxoffice.db')
    cursor = connect.cursor()
    # get director info by movie_id
    print(director_id)
    cursor.execute('''SELECT * FROM Director 
                   JOIN People
                   ON Director.person_id = People.person_id
                   WHERE director_id = ?''',  (director_id,))
    data = cursor.fetchone()
    
    connect.close()
    # Check if data exists
    if data:
        # Convert data to JSON format and return as response
        return jsonify(data)
    else:
        # Return error response if director not found
        return jsonify({"error": "Director not found"}), 404



@app.route('/studio/<int:studio_id>', methods=['GET'])
def getStudio(studio_id):
    connect = sqlite3.connect('boxoffice.db')
    cursor = connect.cursor()
    # get director info by movie_id
    cursor.execute('''SELECT * FROM Studio 
                   WHERE studio_id = ?''',  (studio_id,))
    data = cursor.fetchone()
    
    connect.close()
    # Check if data exists
    if data:
        # Convert data to JSON format and return as response
        return jsonify(data)
    else:
        # Return error response if Studio not found
        return jsonify({"error": "Studio not found"}), 404
    
@app.route('/sales/<int:sales_id>', methods=['GET'])
def getSales(sales_id):
    connect = sqlite3.connect('boxoffice.db')
    cursor = connect.cursor()
    # get director info by movie_id
    cursor.execute('''SELECT * FROM SalesRecord 
                   WHERE sales_record_id = ?''',  (sales_id,))
    data = cursor.fetchone()
    
    connect.close()
    # Check if data exists
    if data:
        # Convert data to JSON format and return as response
        return jsonify(data)
    else:
        # Return error response if Studio not found
        return jsonify({"error": "SalesRecord not found"}), 404
    
@app.route('/actors/<int:movie_id>', methods=['GET'])
def getActors(movie_id):
    connect = sqlite3.connect('boxoffice.db')
    cursor = connect.cursor()
    # get director info by movie_id
    cursor.execute('''SELECT * FROM MovieCast
                   JOIN Actor 
                   ON MovieCast.actor_id = Actor.actor_id
                   JOIN People
                   ON People.person_id = Actor.person_id
                   WHERE MovieCast.movie_id = ?''',  (movie_id,))
    data = cursor.fetchall()
    
    connect.close()
    # Check if data exists
    if data:
        # Convert data to JSON format and return as response
        return jsonify(data)
    else:
        # Return error response if Actors not found
        return jsonify({"error": "Actors not found"}), 404

@app.route('/producers/<int:movie_id>', methods=['GET'])
def getProducers(movie_id):
    connect = sqlite3.connect('boxoffice.db')
    cursor = connect.cursor()
    # get director info by movie_id
    cursor.execute('''SELECT * FROM ProducingCredit
                   JOIN Producer 
                   ON ProducingCredit.producer_id = Producer.producer_id
                   JOIN People
                   ON People.person_id = Producer.person_id
                   WHERE ProducingCredit.movie_id = ?''',  (movie_id,))
    data = cursor.fetchall()
    
    connect.close()
    # Check if data exists
    if data:
        # Convert data to JSON format and return as response
        return jsonify(data)
    else:
        # Return error response if Producers not found
        return jsonify({"error": "Producers not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)
