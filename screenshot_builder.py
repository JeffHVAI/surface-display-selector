import os
import subprocess

# Define paths
WORKSPACE_DIR = r"C:\Users\Jeff\OneDrive - Hoververse\Antigravity Apps\surface-display-selector"
SOURCE_HTML_PATH = r"C:\Users\Jeff\OneDrive - Hoververse\Antigravity Apps\surface-display-selector\surface-display-selector.html"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Read original HTML
with open(SOURCE_HTML_PATH, "r", encoding="utf-8") as f:
    original_html = f.read()

# Helper to write and screenshot
def capture_screenshot(html_content, temp_filename, output_png_filename, window_size="1024,1400"):
    temp_path = os.path.join(WORKSPACE_DIR, temp_filename)
    output_png_path = os.path.join(WORKSPACE_DIR, output_png_filename)
    
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    url = "file:///" + temp_path.replace("\\", "/")
    print(f"Capturing {output_png_filename} from {url}...")
    
    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        f"--screenshot={output_png_path}",
        f"--window-size={window_size}",
        url
    ]
    
    subprocess.run(cmd, check=True)
    print(f"Captured {output_png_filename} successfully!")
    
    # Clean up temp file
    try:
        os.remove(temp_path)
    except OSError:
        pass

# ----------------- Tab 1: Survey Protocol -----------------
# Tab 1 is default, no major changes needed, but let's make sure the window size is right.
# We'll use the original HTML directly but copied to the workspace for clean URL.
capture_screenshot(original_html, "temp_tab1.html", "tab1_survey.png", window_size="1024,1550")

# ----------------- Tab 2: Input Sheet -----------------
tab2_html = original_html
# Activate Tab 2 button in nav
tab2_html = tab2_html.replace(
    '<button class="active" onclick="showTab(0,this)">1 · Survey Protocol</button>',
    '<button onclick="showTab(0,this)">1 · Survey Protocol</button>'
)
tab2_html = tab2_html.replace(
    '<button onclick="showTab(1,this)">2 · Input Sheet</button>',
    '<button class="active" onclick="showTab(1,this)">2 · Input Sheet</button>'
)
# Show Tab 2 content and hide Tab 1
tab2_html = tab2_html.replace(
    '<section class="tab show" id="tab0">',
    '<section class="tab" id="tab0">'
)
tab2_html = tab2_html.replace(
    '<section class="tab" id="tab1">',
    '<section class="tab show" id="tab1">'
)
capture_screenshot(tab2_html, "temp_tab2.html", "tab2_input.png", window_size="1024,1200")

# ----------------- Tab 3: Decision (Standard) -----------------
tab3_html = original_html
# Activate Tab 3 button in nav
tab3_html = tab3_html.replace(
    '<button class="active" onclick="showTab(0,this)">1 · Survey Protocol</button>',
    '<button onclick="showTab(0,this)">1 · Survey Protocol</button>'
)
tab3_html = tab3_html.replace(
    '<button onclick="showTab(2,this)">3 · Decision</button>',
    '<button class="active" onclick="showTab(2,this)">3 · Decision</button>'
)
# Show Tab 3 content and hide Tab 1
tab3_html = tab3_html.replace(
    '<section class="tab show" id="tab0">',
    '<section class="tab" id="tab0">'
)
tab3_html = tab3_html.replace(
    '<section class="tab" id="tab2">',
    '<section class="tab show" id="tab2">'
)
capture_screenshot(tab3_html, "temp_tab3.html", "tab3_decision.png", window_size="1024,1150")

# ----------------- Tab 3: Decision (Alternative/Veto) -----------------
tab3_alt_html = tab3_html
# Change worst-case lux to 2500 and lighting controllability to none (uncontrolled)
tab3_alt_html = tab3_alt_html.replace(
    'value="400" oninput="calc()"',
    'value="2500" oninput="calc()"'
)
tab3_alt_html = tab3_alt_html.replace(
    '<option value="partial" selected>Partially (dimmers / blinds)</option>',
    '<option value="partial">Partially (dimmers / blinds)</option>'
)
tab3_alt_html = tab3_alt_html.replace(
    '<option value="none">Uncontrolled daylight</option>',
    '<option value="none" selected>Uncontrolled daylight</option>'
)
capture_screenshot(tab3_alt_html, "temp_tab3_alt.html", "tab3_decision_alternative.png", window_size="1024,1150")

print("All screenshots generated!")
