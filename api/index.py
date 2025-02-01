from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Example student marks data (for 100 students)
student_marks = {
    "Alice": 90, "Bob": 80, "Charlie": 70, "David": 60, "Eve": 50,
    # Add more students and marks as needed
}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [student_marks.get(name, None) for name in names]
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)

