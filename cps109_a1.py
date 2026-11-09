# Please keep disentangle_entries.txt in the same working folder when running the program.

# By Noorin Sakhi, student number: 501439243, email: nsakhi@torontomu.ca

# little note: I began coding when i was 12, focusing on javascript and react.js, and in my js classes I had projects like this that
# i would build, and i began learning to code in python in 2023, both javascript and python being really similar, except 
# python the syntax and terminologies being more simple compared to javascript, which is ironically is my biggest obstacle with python
# as i tend to overthink the language due to it being more simple.
# this project i enjoyed creating, it took a lot of time, as i kept coming up with new ideas to add and implement, but i enjoyed putting together
# the things i know in python so far into 1 full project.

#---------------------------------------------------------------------

# Disentangle is a personal reflection and pressure-management
# python application made for students and teenagers to organise and manage the
# different pressures they experience in their everyday life.

# When starting university, I thought I was prepared for the pressure and
# mental strain that I would experience, but honestly, it is a lot more than
# what I expected. With the constant exams and tests, studying, while also
# balancing work and social life, I had stress and pressure mounting upon me
# yet I didn't have enough time to sit and analyse and disentangle the issues
# and stress I was facing. Just writing down an endless, negative list in my
# notes app really just isn't efficient.

# Teenagers and students experience overlapping academic, social, family
# and personal expectations, which sooner or later add up and become difficult
# to organise and address manageably. Yes, we do have traditional productivity
# tools and organisers but they just focus primarily on deadlines and scheduled
# tasks, instead of helping to distinguish and connect between all the
# different types of personal pressures and identify appropriate ways to
# approach them.

# Disentangle addresses this problem as it lets users record each pressure,
# and then they get categorised into their predefined sections, indicate their
# personal attention level, and also identify if each situation is within
# their influence, requires support from another person, or is outside
# their control.

# This python program takes these entries, generates a categorised overview,
# displays their attention levels and classifications, and allows users to
# record possible next steps. It then produces a personalised reflection
# report for the user.

# Users can then load previously recorded entries from a text file and save
# their generated report to another text file.


categories = ("Academic", "Social", "Family", "Personal", "Other")

# three possible influence classifications.
influence_options = ("INFLUENCE", "SUPPORT", "OUTSIDE")

# names of the input and output files.
input_file = "disentangle_entries.txt"
output_file = "disentangle_report.txt"


# Load the existing pressure entries func
def load_entries():
    """
    Read existing pressure entries input text file.

    Each valid line has five fields separated by |.
    Return list of tuples containing the recorded information.
    """

    # empty list to store the pressure entries.
    entries = []

    try:
        # Open the input file in read mode.
        with open(input_file, "r") as file:
            # Process each line in the input file.
            for line in file:
                # Remove unnecessary spaces and newline characters.
                line = line.strip()
                # Ignore empty lines in input file.
                if line == "":
                    continue
                # Separate the five fields using the | character.
                parts = line.split("|")
                # Check that the line contains exactly five fields.
                if len(parts) != 5:
                    print("Skipped an entry with an incorrect format.")
                    continue

                # Extract individual fields from the line.
                category = parts[0].strip()
                description = parts[1].strip()
                attention_text = parts[2].strip()
                influence = parts[3].strip()
                next_step = parts[4].strip()

                # Check whether the category is valid.
                if category not in categories:
                    print("Skipped an entry with an invalid category.")
                    continue
                # Check whether the influence classification is valid.
                if influence not in influence_options:
                    print("Skipped an entry with an invalid influence.")
                    continue

                # Convert the attention level from a string to an int.
                try:
                    attention = int(attention_text)

                except ValueError:
                    print("Skipped an entry with an invalid attention level.")
                    continue
                # the attention level is between 1 and 5.
                if attention < 1 or attention > 5:
                    print("Skipped an entry with an invalid attention rating.")
                    continue
                # description and next step are not empty.
                if description == "" or next_step == "":
                    print("Skipped an entry with missing information.")
                    continue

                # Store validated information together in a tuple.
                entry = (category, description, attention,
                         influence, next_step)

                # tuple to the list of recorded entries.
                entries.append(entry)

    except FileNotFoundError:
        # tell  the user if the input file cant be located.
        print("The input file could not be found.")
        print("Please check that it is in the project folder.")

    # Return  successfully loaded entries.
    return entries

# add new pressure func

def add_entry(entries):
    """
    Collect info about a new pressure and add it
    to the existing list of pressure entries.
    """

    print("\n__________Disentangle__________")

    # Display all available categories.
    print("\nChoose a category:")

    for i in range(len(categories)):
        print(i + 1, "-", categories[i])

    # Ask the user for valid category.
    while True:
        category_choice = input("\nEnter category number (1-5): ")

        if category_choice.isdigit():
            category_choice = int(category_choice)

            if category_choice >= 1 and category_choice <= len(categories):
                category = categories[category_choice - 1]
                break

        print("Invalid selection. Please choose a number from 1 to 5.")

    # Collect a description of the pressure.
    while True:
        description = input("\nDescribe what is on your mind: ")
        description = description.strip()

        if description != "":
            break

        print("Please enter a description.")

    # Ask the user how much attention this entry needs.
    print("\nHow much attention would you like to give this?")
    print("1 - Very little")
    print("2 - Low")
    print("3 - Moderate")
    print("4 - High")
    print("5 - Highest")

    while True:
        attention_text = input("Enter attention level (1-5): ")

        if attention_text.isdigit():
            attention = int(attention_text)
            if attention >= 1 and attention <= 5:
                break

        print("Please enter a number between 1 and 5.")

    # Display the available influence classifications.
    print("\nHow would you classify this situation?")
    print("1 - Within my influence")
    print("2 - I might need support")
    print("3 - Outside my direct control")

    # Collect a valid influence selection.
    while True:
        influence_choice = input("Enter your choice (1-3): ")

        if influence_choice == "1":
            influence = "INFLUENCE"
            break
        elif influence_choice == "2":
            influence = "SUPPORT"
            break
        elif influence_choice == "3":
            influence = "OUTSIDE"
            break

        else:
            print("Invalid selection. Please choose 1, 2 or 3.")

    # Ask user to identify one possible next step.
    while True:
        next_step = input("\nWhat is one possible next step? ")
        next_step = next_step.strip()

        if next_step != "":
            break
        print("Please enter a possible next step.")

    # Combine all five pieces of information into a tuple.
    new_entry = (category, description, attention,
                 influence, next_step)

    # Add the new tuple to the existing list.
    entries.append(new_entry)

    # Confirm that the entry has been added.
    print("\nYour pressure has been successfully added!")
    print("Category:", category)
    print("Attention level:", attention)
    print("Influence:", influence)

    return new_entry

# displating all pressure entries func
def display_entries(entries):
    """
    Display all recorded pressures in organised format.

    Each entry displays category, description, attention
    level, influence classification and suggested next step.
    """
    print("YOUR PRESSURE OVERVIEW: ")

    # Check whether there are any recorded entries.
    if len(entries) == 0:
        print("\nYou haven't recorded any pressures yet.")
        print("Choose option 1 to unpack your first pressure.")
        return
    # Display the total number of recorded entries.
    print("\nTotal recorded pressures:", len(entries))

    # Process and display every entry in the list.
    for i in range(len(entries)):

        # Retrieve the current entry.
        entry = entries[i]

        # Extract the individual pieces of information.
        category = entry[0]
        description = entry[1]
        attention = entry[2]
        influence = entry[3]
        next_step = entry[4]

        # Determine the attention label.
        if attention >= 4:
            priority = "Higher attention"
        elif attention == 3:
            priority = "Moderate attention"
        else:
            priority = "Lower attention"

        # Display the entry number and its information.
        print("\nPRESSURE", i + 1)

        print("Category:", category)
        print("Description:", description)
        print("Attention level:", attention, "/ 5")
        print("Priority:", priority)

        # Display a readable influence classification.
        if influence == "INFLUENCE":
            print("Classification: Within my influence")

        elif influence == "SUPPORT":
            print("Classification: May benefit from support")
        else:
            print("Classification: Outside my direct control")
        print("Possible next step:", next_step)
    print("END OF PRESSURE OVERVIEW")

# create presure map func
def create_pressure_map(entries):
    """
    Analyse recorded pressures, display a summary
    showing category totals and average attention.
    """

    # Create counters for each pressure category.
    academic = 0
    social = 0
    family = 0
    personal = 0
    other = 0

    # Keep track of the total attention rating.
    total_attention = 0

    # Examine every recorded pressure.
    for entry in entries:
        # get category and attention rating.
        category = entry[0]
        attention = entry[2]

        # Increase the counter for the matching category.
        if category == "Academic":
            academic = academic + 1
        elif category == "Social":
            social = social + 1
        elif category == "Family":
            family = family + 1
        elif category == "Personal":
            personal = personal + 1
        else:
            other = other + 1

        # Add the attention rating to the running total.
        total_attention = total_attention + attention

    # Calc the total number of recorded pressures.
    total_entries = len(entries)

    # Calc the average attention rating.
    if total_entries > 0:
        average_attention = total_attention / total_entries

    else:
        average_attention = 0

    # Display the pressure map.
    print("YOUR PRESSURE MAP")


    print("\nCategory breakdown:")
    print("Academic:", academic)
    print("Social:", social)
    print("Family:", family)
    print("Personal:", personal)
    print("Other:", other)

    print("\nTotal pressures:", total_entries)
    print("Average attention level:", round(average_attention, 2), "/ 5")


# save pressure report func

def save_report(entries):
    """
    Create a summary of recorded pressures and save it to the output text file.
    """

    # Create counters for each category.
    academic = 0
    social = 0
    family = 0
    personal = 0
    other = 0

    # Keep track of the total attention rating.
    total_attention = 0

    # Examine every recorded entry.
    for entry in entries:

        category = entry[0]
        attention = entry[2]

        # Count the entries belonging to each category.
        if category == "Academic":
            academic = academic + 1

        elif category == "Social":
            social = social + 1

        elif category == "Family":
            family = family + 1

        elif category == "Personal":
            personal = personal + 1

        else:
            other = other + 1

        # Add the attention rating to the total.
        total_attention = total_attention + attention

    # Calc the total number of entries.
    total_entries = len(entries)

    # Calc the average attention rating.
    if total_entries > 0:
        average_attention = total_attention / total_entries

    else:
        average_attention = 0

    # Open the output file in write mode.
    with open(output_file, "w") as report_file:

        # Write the report heading.
        report_file.write("DISENTANGLE REPORT\n")

        # Write the category breakdown.
        report_file.write("PRESSURE CATEGORY BREAKDOWN\n")
        report_file.write("----------------------------------------\n")
        report_file.write("Academic: " + str(academic) + "\n")
        report_file.write("Social: " + str(social) + "\n")
        report_file.write("Family: " + str(family) + "\n")
        report_file.write("Personal: " + str(personal) + "\n")
        report_file.write("Other: " + str(other) + "\n")

        # Write the overall statistics.
        report_file.write("\nTOTAL PRESSURES: " + str(total_entries) + "\n")
        report_file.write("AVERAGE ATTENTION: " +
                          str(round(average_attention, 2)) + " / 5\n")

        # Write each recorded pressure.
        report_file.write("\nRECORDED PRESSURES\n")
        report_file.write("----------------------------------------\n")

        for i in range(len(entries)):
            entry = entries[i]

            report_file.write("\nPressure " + str(i + 1) + "\n")
            report_file.write("Category: " + entry[0] + "\n")
            report_file.write("Description: " + entry[1] + "\n")
            report_file.write("Attention: " + str(entry[2]) + "/5\n")
            report_file.write("Influence: " + entry[3] + "\n")
            report_file.write("Next step: " + entry[4] + "\n")

    # Confirm  report was successfully created.
    print("\nYour DISENTANGLE report has been saved!")
    print("File:", output_file)

# main applicaton menu func
def main():
    """
    Run Disentangle and connect features through interactive menu.
    """
    # Load previously recorded entries.
    entries = load_entries()
    # Display the application welcome message.
    print("DISENTANGLE")
    # Keep displaying the menu until the user exits.
    running = True
    while running:

        print("\nWhat would you like to do?")
        print("1. Add a new pressure")
        print("2. View recorded pressures")
        print("3. View pressure map")
        print("4. Save reflection report")
        print("5. Exit")

        # Ask the user to select a menu option.
        choice = input("\nEnter your choice (1-5): ")
        # Add a new pressure entry.
        if choice == "1":
            add_entry(entries)
        # Display all recorded pressure entries.
        elif choice == "2":
            display_entries(entries)
        # Display the category breakdown and average.
        elif choice == "3":
            create_pressure_map(entries)

        # Generate and save the reflection report.
        elif choice == "4":
            save_report(entries)

        # Exit the application.
        elif choice == "5":
            print("\nThank you for using DISENTANGLE.")
            print("Remember, you don't have to address")
            print("everything at once.")
            running = False

        # Handle invalid menu selections.
        else:
            print("\nInvalid choice. Please choose from 1 to 5.")

# Start the application.
main()