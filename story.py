from fpdf import FPDF

# Create a PDF instance
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set title font
pdf.set_font("Arial", style="B", size=24)
pdf.set_text_color(0, 102, 204)  # Blue color
pdf.cell(200, 10, "From Dorms to Disruptors", ln=True, align="C")
pdf.ln(10)

# Set subtitle font
pdf.set_font("Arial", style="B", size=16)
pdf.set_text_color(0, 0, 0)
pdf.multi_cell(0, 10, "The Reality Show That Turns Student Startups into Global Giants", align="C")
pdf.ln(10)

# Set body text font
pdf.set_font("Arial", size=12)

content = """
Concept Overview
What if your college side project wasn’t just an assignment, but the next billion-dollar idea? 
From Dorms to Disruptors is a high-stakes reality series that follows college entrepreneurs 
as they transform their raw ideas into fully functional startups. This show is more than just 
entertainment—it’s a real startup accelerator where young founders compete for funding, mentorship, 
and the chance to launch the next big thing.

Blending the high-energy drama of Shark Tank, the intensity of a startup incubator like Y Combinator, 
and the authentic struggles of student entrepreneurs, this series will uncover what it really takes 
to build a company from scratch while still managing college life.

Target Audience & Impact
- Aspiring entrepreneurs & college students looking for inspiration
- Startup enthusiasts, VCs, and business leaders seeking the next big disruptors
- Tech and business influencers who thrive on innovation and risk-taking
- Casual viewers who love high-stakes reality shows with real-world consequences

This series will inspire a whole generation of student founders by showing them that the 
biggest ideas often start in dorm rooms. It will demystify the startup world and create a 
mainstream cultural movement around student-led innovation.

Format & Episode Structure
🔥 Episode 1: The Ultimate Startup Draft
- Founders pitch their ideas within one hour to their peers.
- Twist: The best founders get to hand-pick their dream team from the crowd.
- First eliminations happen before the show even starts!

🛠️ Episode 2: The "Launch or Get Lost" Challenge
- Teams must launch an MVP in 48 hours.
- Surprise hacker attack: A team faces a real security vulnerability on launch day.
- First investor rejection round: "Your idea sucks" moments begin.

💀 Episode 3: The "Pivot or Die" Episode
- Lowest-performing team must either pivot or leave the show.
- One startup unexpectedly goes viral on TikTok and has to decide whether to completely shift focus.

💰 Episode 4: "Burn Rate or Bust"
- Startups pitch how they would spend a fake $100K to investors.
- Surprise guest investor: A billionaire like Balaji Srinivasan or Kunal Shah challenges them live.

🚀 Episode 5: The "Shark Tank Showdown"
- Final demo day with real venture capitalists.
- Surprise Acquisition: One startup gets an unexpected buyout offer on air.
- Final confessions: Founders reflect on their journey and self-doubt.

Why This Show Will Be a Hit
✅ It’s Not Just a Show, It’s a Launchpad
- Winning startups could receive real funding and enter major incubators.

✅ Failure is Just as Valuable as Success
- The show will highlight what NOT to do in a startup.

✅ It Will Inspire a Whole Generation
- From Dorms to Disruptors will be THE reality show for Gen Z entrepreneurs, making startup 
culture mainstream and turning founders into rockstars.

Final Pitch
From Dorms to Disruptors isn’t just a show—it’s a cultural movement that brings the energy, risk, 
and excitement of real startup life to the screen. It will educate, inspire, and entertain while 
launching the next generation of legendary founders.

Are you ready to disrupt the way we see entrepreneurship?
"""

# Add text to the PDF
pdf.multi_cell(0, 8, content)

# Save PDF
pdf_output_path = "/mnt/data/From_Dorms_to_Disruptors.pdf"
pdf.output(pdf_output_path)

# Provide the download link
pdf_output_path
