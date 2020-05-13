# twf

This is an API use to solve the warehouse delivery problem

Instructions to Run Program Locally:
- use command 
  ```bash
  python3 solver.py
  ```
- when prompted with the "Input the amount of each item" provide the input
- the input takes the form "(# of A) (# of B) ..... (# of I)"
- Note: do not include quotations

Example:
- If input is A-1, G-1, H-1, I-3
- Then, the format should be 1 0 0 0 0 0 1 1 3

Instructions for API:
- To set up the API run
  ```bash
  python3 app.py
  ```
- Note: Make sure to have networkx, flask, and flask-restful installed (use pip3)
- Now you can use postman to send a POST requests to http://127.0.0.1:5000/mincost
- Make sure the Body is raw and JSON type
- Input format should be:
  {
    "data":"(# of A) (# of B) ..... (# of I)"
  }
- After sending the request you should be prompted with the min cost

Format for API POST request:
- If input is A-1, G-1, H-1, I-3
- Then POST request body should be

{

	"data":"1 0 0 0 0 0 1 1 3"
	
}


