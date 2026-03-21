Here’s a set of **engaging, realistic exercises** that require students to *choose* an appropriate visualisation based on the structure and meaning of the data. Each exercise includes a small DataFrame and a short prompt that forces learners to think: *“What plot best communicates this?”*  

They’re designed to fit neatly into a Pandas or Matplotlib lesson, and they scale well from beginner to intermediate.

---

# 🎯 **Exercise Set: Choosing the Right Visualisation**

Below are **10 exercises**, each with a DataFrame and a question. Students must:

1. Identify the most appropriate plot  
2. Justify their choice  
3. Produce the plot using Pandas/Matplotlib  

---

## **1. Daily Temperatures (Trend Over Time)**

```python
import pandas as pd

df1 = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "temperature": [12, 14, 15, 13, 16, 18, 17]
})
```

**Task:**  
Visualise how temperature changes across the week.  
What plot best shows a trend over time?

---

## **2. Fruit Sales (Categorical Comparison)**

```python
df2 = pd.DataFrame({
    "fruit": ["Apples", "Bananas", "Cherries", "Dates"],
    "sales": [50, 75, 40, 20]
})
```

**Task:**  
Show which fruit sold the most.  
Which plot makes category comparisons easiest?

---

## **3. Student Study Hours vs Test Score (Relationship)**

```python
df3 = pd.DataFrame({
    "hours_studied": [1, 2, 3, 4, 5, 6],
    "test_score": [50, 55, 65, 70, 80, 85]
})
```

**Task:**  
Visualise the relationship between hours studied and test score.  
Which plot best shows correlation?

---

## **4. Distribution of Exam Scores (Spread)**

```python
df4 = pd.DataFrame({
    "score": [55, 60, 62, 65, 70, 72, 75, 80, 85, 90, 92, 95]
})
```

**Task:**  
Show how exam scores are distributed.  
Which plot reveals clusters, skew, or gaps?

---

## **5. Monthly Revenue for Two Products (Multiple Trends)**

```python
df5 = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "product_A": [1000, 1200, 1300, 1250, 1400],
    "product_B": [900, 950, 1100, 1150, 1200]
})
```

**Task:**  
Compare revenue trends for two products over time.  
Which plot shows two lines clearly?

---

## **6. Budget Breakdown (Proportions)**

```python
df6 = pd.DataFrame({
    "category": ["Rent", "Food", "Transport", "Entertainment", "Savings"],
    "amount": [800, 300, 120, 150, 200]
})
```

**Task:**  
Show how a monthly budget is divided across categories.  
Which plot best shows proportions of a whole?

---

## **7. Class Scores by Group (Distribution Comparison)**

```python
df7 = pd.DataFrame({
    "class": ["A", "A", "A", "B", "B", "B"],
    "score": [70, 75, 80, 65, 68, 72]
})
```

**Task:**  
Compare the score distributions between Class A and Class B.  
Which plot highlights medians and outliers?

---

## **8. Website Traffic Sources (Categorical Proportions)**

```python
df8 = pd.DataFrame({
    "source": ["Search", "Direct", "Social", "Referral"],
    "visits": [500, 300, 150, 50]
})
```

**Task:**  
Show which traffic sources contribute most to total visits.  
Which plot communicates proportions clearly?

---

## **9. Sales by Quarter and Product (Grouped Categories)**

```python
df9 = pd.DataFrame({
    "quarter": ["Q1", "Q1", "Q2", "Q2", "Q3", "Q3"],
    "product": ["A", "B", "A", "B", "A", "B"],
    "sales": [100, 80, 120, 90, 140, 110]
})
```

**Task:**  
Compare product sales across quarters.  
Which plot shows grouped categories effectively?

---

## **10. Height vs Weight (Scatter With Trend)**

```python
df10 = pd.DataFrame({
    "height_cm": [150, 155, 160, 165, 170, 175, 180],
    "weight_kg": [50, 55, 60, 65, 70, 75, 80]
})
```

**Task:**  
Show the relationship between height and weight.  
Which plot best visualises a linear relationship?

---

# 🌟 Want to turn these into a worksheet or Jupyter Notebook?

I can format them into:

- A printable worksheet  
- A Jupyter Notebook with starter code  
- A version with hints and solutions  
- A version with extension challenges (e.g., styling, subplots, annotations)

Just tell me what format you want.