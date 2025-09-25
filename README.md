# Cricket-Strategy-Analysis-
# Cricket Strategy Analytics 🏏

A **Streamlit-based Python application** to analyze cricket match commentary and provide strategic insights, performance analysis, outcome predictions, and tactical recommendations.  

---

## **Features**

1. **Input Match Commentary**  
   - Paste live or historical commentary of a cricket match.

2. **Strategy Analysis**  
   - Detects batting aggression, defensive shots, bowling variations, and fielding patterns.

3. **Performance Insights**  
   - Summarizes key batting, bowling, and fielding events.

4. **Outcome Predictions**  
   - Provides a basic prediction of match outcome based on commentary analysis.

5. **Tactical Recommendations**  
   - Suggests strategies to improve team performance.

---

## **Requirements**

- Python 3.8+  
- Streamlit  
- pandas  
- NLTK  
- spaCy  

---

## **Setup Instructions**

1. **Clone the repository**:

```bash
git clone <repository-url>
cd cricket_strategy_analytics
Create a virtual environment (recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows

bash
Copy code
venv\Scripts\activate
Linux / Mac

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install streamlit pandas nltk spacy
Download NLTK punkt tokenizer:

python
Copy code
import nltk
nltk.download('punkt')
Download spaCy English model:

bash
Copy code
python -m spacy download en_core_web_sm
Running the App
Make sure your virtual environment is active.

Run the Streamlit app:

bash
Copy code
streamlit run app.py
Open the URL shown in the terminal (usually http://localhost:8501).

Paste cricket match commentary in the text area and click "Analyze Commentary".

Sample Input
markdown
Copy code
1. Smith hits a glorious six over mid-off.
2. Johnson delivers a perfect yorker, and the batsman is bowled.
3. Warner cuts the ball elegantly for four.
4. Fielding at silly point saves a certain boundary.
5. Rashid spins the ball sharply, beating the bat.
6. A sharp run out by the mid-off fielder dismisses Kohli.
7. Finch pulls a short ball for another boundary.
8. Anderson bowls a bouncer, narrowly missing the batsman.
9. The slip cordon takes a brilliant catch.
10. Stokes drives the ball straight back past the bowler for four runs.
Expected Output
Strategy Analysis

Batting: Lines 1, 3, 7, 10

Bowling: Lines 2, 5, 8

Fielding: Lines 4, 6, 9

Performance Insights

Batting: 4 key events

Bowling: 3 key events

Fielding: 3 key events

Outcome Prediction

"Team likely to win 🏆"

Tactical Recommendations

Maintain batting momentum

Bowling strategy seems balanced

Fielding is strong, maintain positions

