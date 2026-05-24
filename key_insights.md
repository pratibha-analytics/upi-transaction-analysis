# My Analysis — UPI Transaction Data (2021–2022)

** Pratibha Singh | Netaji Subhas University of Technology**

---

## What is this data about?

This dataset contains monthly transaction records of all UPI (Unified Payments Interface) apps in India. It was published by NPCI (National Payments Corporation of India). The data tells us how many transactions happened on each app, and how much money was transferred.

- **2021 data** covers all 12 months
- **2022 data** covers January to July
- **121 different UPI apps and banks** are included

---

## Insight 1 — UPI grew very fast

The average monthly transactions jumped from **3,295 Million in 2021** to **5,561 Million in 2022**. That is a growth of **68.8% in just one year**.

To put it simply: in 2021, Indians were doing about 3,295 million UPI payments every month. By 2022, that number had grown to 5,561 million per month. This shows that more and more people are switching to digital payments.

---

## Insight 2 — Growth was steady, not sudden

In 2021, volume grew consistently every quarter:

| Quarter | Months | Avg Monthly Volume |
|---------|--------|--------------------|
| Q1 | Jan, Feb, Mar | ~2,492 Mn |
| Q2 | Apr, May, Jun | ~2,718 Mn |
| Q3 | Jul, Aug, Sep | ~3,557 Mn |
| Q4 | Oct, Nov, Dec | ~4,413 Mn |

This tells us UPI growth is not because of one event — it is a steady habit being formed by millions of Indians.

---

## Insight 3 — No slowdown at the start of 2022

Usually businesses see a drop in January (people spend less after December festivals). But UPI showed no such dip:

- December 2021: **4,658 Mn** transactions
- January 2022: **4,708 Mn** transactions

January 2022 was actually slightly higher than December 2021. This means UPI has become a daily habit — people use it every day regardless of the time of year.

---

## Insight 4 — PhonePe leads the market clearly

| App | Total Volume (Mn) | % of Top 3 |
|-----|-------------------|------------|
| PhonePe | 35,380 | ~46% |
| Google Pay | 26,640 | ~34% |
| Paytm | 11,445 | ~15% |
| All others | ~5,076 | ~5% |

PhonePe has nearly **1.5 times more volume than Google Pay**. Even though we see Google Pay advertisements more often, PhonePe is actually used more. This might be because PhonePe is popular in smaller cities and towns.

---

## Insight 5 — Market is concentrated at the top

Even though 121 different apps are in the dataset, the top 3 (PhonePe, Google Pay, Paytm) handle the huge majority of all transactions. The remaining 118 apps together make up only a small fraction. This is called a **concentrated market** — a few big players dominate.

---

## Insight 6 — People are also doing bigger transactions

The value (money amount) of transactions also grew:

| Period | Monthly Value |
|--------|--------------|
| January 2021 | ₹4.35 Lakh Crore |
| July 2022 | ₹10.79 Lakh Crore |

This is more than **2.5× growth in 18 months**. It means people are not just doing more transactions — they are also transferring larger amounts. UPI is being trusted for bigger payments now.

---

## My Overall Conclusion

UPI is one of India's biggest digital success stories. The data clearly shows that:
1. The number of transactions is growing rapidly every year
2. The amount of money being transferred is also growing
3. A few big apps dominate the market
4. Growth is consistent — not seasonal

This project helped me understand how to find stories inside raw data using Python.

---

*Analysis done using Python (pandas, matplotlib) | Data: NPCI*
