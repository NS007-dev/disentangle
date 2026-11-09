# DISENTANGLE

**You don't have to carry everything at once.**

DISENTANGLE is a small Python app I made to help sort out all the different pressures that pile up in student life. You type in what's on your mind, say how much attention it needs, and figure out what you can actually do about it.

I built it as my first big project for CPS109 at university, so it's a console program with no fancy interface, and I'm pretty proud of it.

## Why I Built It

When I started university, I thought I was ready for it. Then exams, studying, work and trying to still have a social life all landed at the same time, and it was a lot harder than I expected.

My head was full of things I needed to deal with, and I never knew where to start. Writing everything down helped a bit, but a long list is still just a long list. I wanted something that would let me separate the pressures, see which ones were actually worth my energy, and think about what to do next.

Most productivity apps are about deadlines and to-do lists. I wanted something that came before that, a place to just work out what I'm dealing with. That became DISENTANGLE.

## What It Does

- **Sorts pressures into categories:** Academic, Social, Family, Personal and Other.
- **Attention ratings:** Rate each pressure from 1 to 5 depending on how much of your attention it's taking.
- **Influence check:** Decide whether something is in your control, needs help from someone else, or is outside your control entirely.
- **Overview:** See all your entries in one place, with descriptions, classifications and next steps.
- **Pressure map:** See how your pressures break down by category, plus the total number of entries and your average attention rating.
- **Reflection report:** Save a report with your category stats and every entry.
- **Input validation:** Checks what you type and what it loads from a file, so bad data doesn't break things.

## Built With

- **Python 3**
- **Lists and tuples** to store and organise entries
- **Conditional statements** for validation and classification
- **For and while loops** for the menu and for going through entries
- **File handling** to load old entries and save reports

No external libraries needed.

## Getting Started

1. Clone the repo:

   ```bash
   git clone https://github.com/YOUR-USERNAME/DISENTANGLE.git
   ```

2. Go into the folder:

   ```bash
   cd DISENTANGLE
   ```

3. Check you have Python 3:

   ```bash
   python3 --version
   ```

4. Run it:

   ```bash
   python3 cps109_a1.py
   ```

## 📁 Project Structure

```text
DISENTANGLE/
│
├── cps109_a1.py
├── disentangle_entries.txt
├── disentangle_report.txt
└── README.md
```

| File | What it's for |
|---|---|
| `cps109_a1.py` | The main program |
| `disentangle_entries.txt` | Entries saved from before, loaded when the program starts |
| `disentangle_report.txt` | The reflection report (created when you save one) |
| `README.md` | This file |

## 🖥️ How to Use It

When you run the program, you'll see this menu:

```text
========================================
              DISENTANGLE
    You don't have to carry everything
              at once.
========================================

What would you like to do?

1. Add a new pressure
2. View recorded pressures
3. View pressure map
4. Save reflection report
5. Exit
```

| Option | What happens |
|---|---|
| 1 | Add a new pressure and fill in its details |
| 2 | View everything you've recorded |
| 3 | See the category breakdown and average attention level |
| 4 | Save a reflection report |
| 5 | Exit |

## Input File Format

DISENTANGLE can load earlier entries from `disentangle_entries.txt`. Each line has five fields separated by a pipe (`|`):

```text
Category|Description|Attention|Influence|Next Step
```

For example:

```text
Academic|Preparing for upcoming exams|5|INFLUENCE|Create a revision schedule
Social|Balancing social commitments|3|SUPPORT|Talk through my commitments
Family|Managing family expectations|4|OUTSIDE|Focus on what I can control
Personal|Keeping up with daily responsibilities|2|INFLUENCE|Break things into smaller steps
```

**Categories:** Academic, Social, Family, Personal, Other

**Influence options:**
- `INFLUENCE`: it's within your control
- `SUPPORT`: you might need help from someone else
- `OUTSIDE`: it's outside your control

Attention has to be a whole number from 1 to 5. If a line is invalid or formatted wrong, the program skips it when loading.

## Reflection Reports

Choosing option 4 creates `disentangle_report.txt`, which includes:

- A breakdown of entries across all five categories
- The total number of pressures
- The average attention rating
- Each entry's description, attention rating, influence classification and next step

Any entries you add during a session go into the report. One thing to know: they're only kept in memory while the program is running, so they don't get added to `disentangle_entries.txt` automatically.

## What I Practised

This was my chance to use what I've learned in intro Python on something I actually cared about:

- Variables and arithmetic
- `if`, `elif` and `else`
- Strings, lists and tuples
- `for` and `while` loops
- Writing my own functions
- Console input and output
- Reading from and writing to text files

## A Note

DISENTANGLE is a personal organisation and reflection tool. It isn't meant to diagnose or treat anything, or to replace real support if you're struggling.

For me, the idea comes down to this: before you can figure out what to do, it helps to understand what you're dealing with.

**You don't have to figure everything out at once.**

---

*Created by Noorin Sakhi as a CPS109 introductory programming project*
