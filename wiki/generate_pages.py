import os

# Define the base template for all pages
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
    <link rel="stylesheet" href="../styles/wiki.css">
</head>
<body>
    <div class="header">
        <img src="https://image.eveonline.com/Corporation/144534752_128.png" alt="Mercurialis Inc.">
        <h1>Mercurialis Inc. Wiki</h1>
        <h2>Your Guide to All Things MINC</h2>
    </div>

    <div class="navigation-panel">
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="corporation.html">Corporation</a></li>
            <li><a href="fleetops.html">Fleet Operations</a></li>
            <li><a href="intel.html">Intel Tools</a></li>
            <li><a href="resources.html">Resources</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="doctrines.html">Doctrines</a></li>
            <li><a href="recruitment.html">Recruitment</a></li>
            <li><a href="history.html">History</a></li>
            <li><a href="faq.html">FAQ</a></li>
        </ul>
    </div>

    <div class="wiki-section">
        <h3>{page_heading}</h3>
        <p>{page_content}</p>
    </div>

    <div class="footer">
        <p>&copy; 2025 Mercurialis Inc. All rights reserved.</p>
    </div>
</body>
</html>
"""

# Define the pages to generate
PAGES = [
    {"filename": "index.html", "title": "Home", "heading": "Welcome to the Mercurialis Inc. Wiki", "content": "This wiki is your ultimate guide to all things MINC. Explore our pages to learn more."},
    {"filename": "corporation.html", "title": "Corporation Overview", "heading": "About Mercurialis Inc.", "content": "Learn about our mission, history, and leadership structure."},
    {"filename": "fleetops.html", "title": "Fleet Operations", "heading": "Fleet Operations", "content": "Join our fleet operations and dominate the battlefield!"},
    {"filename": "intel.html", "title": "Intel Tools", "heading": "Eve Rift Intel Fusion Tool", "content": "Learn how to use our official intel tools to stay ahead."},
    {"filename": "resources.html", "title": "Resources", "heading": "Player Resources", "content": "A collection of useful resources for new and veteran players alike."},
    {"filename": "contact.html", "title": "Contact Leadership", "heading": "Contact Leadership", "content": "Get in touch with our leaders for diplomacy or recruitment inquiries."},
    {"filename": "doctrines.html", "title": "Doctrines", "heading": "Fleet Doctrines", "content": "Our official fleet doctrines and ship fittings."},
    {"filename": "recruitment.html", "title": "Recruitment", "heading": "Join Mercurialis Inc.", "content": "Learn how to join our ranks and become part of EVE's legacy."},
    {"filename": "history.html", "title": "History", "heading": "Corporation History", "content": "A timeline of major events and achievements in our history."},
    {"filename": "faq.html", "title": "FAQ", "heading": "Frequently Asked Questions", "content": "Find answers to the most common questions about our corporation."}
]

# Define the output directory
OUTPUT_DIR = "wiki"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Generate each page
for page in PAGES:
    file_path = os.path.join(OUTPUT_DIR, page["filename"])
    with open(file_path, "w") as file:
        file.write(TEMPLATE.format(
            page_title=page["title"],
            page_heading=page["heading"],
            page_content=page["content"]
        ))
    print(f"Generated {file_path}")

print("All pages have been generated successfully!")
