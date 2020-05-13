from flask import Flask, jsonify, request
import solver
# initialize our Flask application
app= Flask(__name__)
@app.route("/mincost", methods=["POST"])
def find_mincost():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['data']
        sol = solver.api_solve(data)
        return jsonify(str("Min Cost: " + str(sol)))

if __name__=='__main__':
    app.run(debug=True)