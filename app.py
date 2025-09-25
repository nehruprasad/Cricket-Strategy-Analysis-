import streamlit as st
import spacy
import pandas as pd
from nltk.tokenize import sent_tokenize
from collections import Counter
import random

# Download NLTK punkt tokenizer if not already installed
import nltk
nltk.download('punkt')

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# ----------------- Helper Functions -----------------

def analyze_strategy(commentary_text):
    """
    Analyze strategies from commentary:
    - Batting aggression, defensive shots
    - Bowling type (spin, pace)
    - Fielding patterns
    """
    sentences = sent_tokenize(commentary_text)
    strategy_summary = {"Batting": [], "Bowling": [], "Fielding": []}

    for s in sentences:
        s_lower = s.lower()
        # Batting strategies
        if any(word in s_lower for word in ["six", "four", "boundary", "drive", "cut", "pull"]):
            strategy_summary["Batting"].append(s)
        # Bowling strategies
        if any(word in s_lower for word in ["bowled", "yorker", "spin", "bouncer", "slower ball", "line and length"]):
            strategy_summary["Bowling"].append(s)
        # Fielding strategies
        if any(word in s_lower for word in ["catch", "run out", "fielding", "slip", "silly point", "mid-off"]):
            strategy_summary["Fielding"].append(s)
    
    return strategy_summary

def performance_insights(strategy_summary):
    """
    Generate simple performance insights from strategies
    """
    insights = {}
    for key, events in strategy_summary.items():
        insights[key] = f"{len(events)} key events detected in {key.lower()}"
    return insights

def predict_outcome(strategy_summary):
    """
    Basic prediction logic: more aggressive batting -> likely win
    """
    batting_score = len(strategy_summary["Batting"])
    bowling_score = len(strategy_summary["Bowling"])
    fielding_score = len(strategy_summary["Fielding"])

    total_score = batting_score*2 + bowling_score + fielding_score
    if total_score > 15:
        return "Team likely to win 🏆"
    elif total_score > 8:
        return "Match could be close ⚖️"
    else:
        return "Team may struggle ❌"

def tactical_recommendations(strategy_summary):
    """
    Provide tactical recommendations based on commentary analysis
    """
    recommendations = []
    if len(strategy_summary["Batting"]) < 3:
        recommendations.append("Increase aggressive batting, target boundaries")
    else:
        recommendations.append("Maintain batting momentum")

    if len(strategy_summary["Bowling"]) < 2:
        recommendations.append("Use more variations in bowling (spin/pace)")
    else:
        recommendations.append("Bowling strategy seems balanced")

    if len(strategy_summary["Fielding"]) < 2:
        recommendations.append("Improve field placements and catching practice")
    else:
        recommendations.append("Fielding is strong, maintain positions")

    return recommendations

# ----------------- Streamlit App -----------------

st.set_page_config(page_title="Cricket Strategy Analytics", layout="wide")
st.title("🏏 Cricket Strategy Analytics")

st.markdown("Analyze cricket match commentary for strategy, performance insights, and tactical recommendations.")

# Input commentary
commentary_text = st.text_area("Paste match commentary here (multiple lines)", height=250)

if st.button("Analyze Commentary"):
    if commentary_text.strip() == "":
        st.warning("Please enter match commentary to analyze.")
    else:
        st.success("Analyzing commentary...")

        # Strategy analysis
        strategy_summary = analyze_strategy(commentary_text)
        st.header("⚡ Strategy Analysis")
        for key, events in strategy_summary.items():
            st.subheader(key)
            if events:
                for e in events:
                    st.write("- " + e)
            else:
                st.write("No key events detected.")

        # Performance insights
        insights = performance_insights(strategy_summary)
        st.header("📊 Performance Insights")
        for key, insight in insights.items():
            st.write(f"{key}: {insight}")

        # Outcome prediction
        st.header("🎯 Outcome Prediction")
        prediction = predict_outcome(strategy_summary)
        st.write(prediction)

        # Tactical recommendations
        st.header("📝 Tactical Recommendations")
        recommendations = tactical_recommendations(strategy_summary)
        for r in recommendations:
            st.write("- " + r)
