from flask import Flask, render_template, jsonify

app = Flask(__name__)

# pricing: "free" = usable free/open-source edition; "paid" = paid product
# or a product whose full editing workflow requires a paid plan/license.
TOOLS = [
    {"name":"DaVinci Resolve","category":"Video","pricing":"free","type":"Free edition available","description":"Professional editing, color grading, visual effects and audio post-production. Studio edition is paid.","url":"https://www.blackmagicdesign.com/products/davinciresolve","icon":"🎬","color":"violet","tags":["editing","color","vfx"]},
    {"name":"Adobe Premiere Pro","category":"Video","pricing":"paid","type":"Paid subscription","description":"Industry-standard video editing for films, social content and productions.","url":"https://www.adobe.com/products/premiere.html","icon":"▶","color":"purple","tags":["editing","adobe"]},
    {"name":"Final Cut Pro","category":"Video","pricing":"paid","type":"Paid license","description":"Apple's powerful video editor for Mac and iPad.","url":"https://www.apple.com/final-cut-pro/","icon":"✂️","color":"slate","tags":["editing","apple"]},
    {"name":"CapCut","category":"Video","pricing":"free","type":"Free + optional Pro","description":"Video editor with a free tier; some effects and features require Pro.","url":"https://www.capcut.com/","icon":"✦","color":"dark","tags":["shorts","reels"]},
    {"name":"VEGAS Pro","category":"Video","pricing":"paid","type":"Paid license","description":"Creative video and audio editing with advanced workflow tools.","url":"https://www.vegascreativesoftware.com/vegas-pro/","icon":"▰","color":"pink","tags":["editing","effects"]},
    {"name":"Filmora","category":"Video","pricing":"free","type":"Free + paid plans","description":"Try the editor for free; export and premium features may require a paid plan.","url":"https://filmora.wondershare.com/","icon":"◉","color":"cyan","tags":["editing","easy"]},
    {"name":"Shotcut","category":"Video","pricing":"free","type":"Free & open source","description":"Free, open-source, cross-platform video editor.","url":"https://shotcut.org/","icon":"◫","color":"blue","tags":["free","open source"]},
    {"name":"Kdenlive","category":"Video","pricing":"free","type":"Free & open source","description":"Feature-rich open-source nonlinear video editor.","url":"https://kdenlive.org/","icon":"▣","color":"green","tags":["free","open source"]},
    {"name":"OpenShot","category":"Video","pricing":"free","type":"Free & open source","description":"Simple, open-source video editing for beginners.","url":"https://www.openshot.org/","icon":"▱","color":"orange","tags":["free","open source"]},
    {"name":"Avid Media Composer","category":"Video","pricing":"paid","type":"Paid plans","description":"Professional post-production software used in film and television.","url":"https://www.avid.com/media-composer","icon":"A","color":"blue","tags":["film","editing"]},
    {"name":"Adobe After Effects","category":"Motion & VFX","pricing":"paid","type":"Paid subscription","description":"Motion graphics, compositing and visual effects.","url":"https://www.adobe.com/products/aftereffects.html","icon":"Ae","color":"purple","tags":["motion","vfx","adobe"]},
    {"name":"Blender","category":"3D & Animation","pricing":"free","type":"Free & open source","description":"3D creation suite for modeling, animation, rendering and compositing.","url":"https://www.blender.org/","icon":"♧","color":"orange","tags":["3d","free","open source"]},
    {"name":"Cinema 4D","category":"3D & Animation","pricing":"paid","type":"Paid subscription","description":"3D modeling, animation, simulation and motion graphics.","url":"https://www.maxon.net/en/cinema-4d","icon":"C4D","color":"slate","tags":["3d","motion"]},
    {"name":"Autodesk Maya","category":"3D & Animation","pricing":"paid","type":"Paid subscription","description":"3D animation, modeling, simulation and rendering.","url":"https://www.autodesk.com/products/maya/overview","icon":"M","color":"blue","tags":["3d","animation"]},
    {"name":"Adobe Animate","category":"3D & Animation","pricing":"paid","type":"Paid subscription","description":"Create 2D animations and interactive content.","url":"https://www.adobe.com/products/animate.html","icon":"An","color":"purple","tags":["2d","animation"]},
    {"name":"Krita","category":"Photo & Design","pricing":"free","type":"Free & open source","description":"Free digital painting and illustration application.","url":"https://krita.org/","icon":"✎","color":"green","tags":["drawing","free","open source"]},
    {"name":"Adobe Photoshop","category":"Photo & Design","pricing":"paid","type":"Paid subscription","description":"Photo editing, image compositing and digital art.","url":"https://www.adobe.com/products/photoshop.html","icon":"Ps","color":"blue","tags":["photo","adobe"]},
    {"name":"Adobe Lightroom","category":"Photo & Design","pricing":"paid","type":"Paid subscription","description":"Photo organization, raw processing and color adjustments.","url":"https://www.adobe.com/products/photoshop-lightroom.html","icon":"Lr","color":"blue","tags":["photo","adobe"]},
    {"name":"Affinity Photo","category":"Photo & Design","pricing":"paid","type":"Check current license","description":"Advanced photo editing and raster design. Check the official site for current pricing and terms.","url":"https://affinity.serif.com/photo/","icon":"Af","color":"purple","tags":["photo","design"]},
    {"name":"GIMP","category":"Photo & Design","pricing":"free","type":"Free & open source","description":"Powerful free and open-source image editor.","url":"https://www.gimp.org/","icon":"G","color":"orange","tags":["photo","free","open source"]},
    {"name":"Canva","category":"Photo & Design","pricing":"free","type":"Free + Pro plan","description":"Browser-based design with free tools and optional Pro features.","url":"https://www.canva.com/","icon":"✿","color":"cyan","tags":["design","online"]},
    {"name":"Figma","category":"Photo & Design","pricing":"free","type":"Free + paid plans","description":"Collaborative interface design and prototyping with free and paid plans.","url":"https://www.figma.com/","icon":"◈","color":"pink","tags":["ui","design","online"]},
    {"name":"Inkscape","category":"Photo & Design","pricing":"free","type":"Free & open source","description":"Open-source vector graphics editor.","url":"https://inkscape.org/","icon":"◇","color":"slate","tags":["vector","free","open source"]},
    {"name":"Affinity Designer","category":"Photo & Design","pricing":"paid","type":"Check current license","description":"Vector graphic design and illustration. Check the official site for current pricing and terms.","url":"https://affinity.serif.com/designer/","icon":"Ad","color":"purple","tags":["vector","design"]},
    {"name":"Audacity","category":"Audio","pricing":"free","type":"Free & open source","description":"Free multi-track audio editor and recorder.","url":"https://www.audacityteam.org/","icon":"〰","color":"blue","tags":["audio","free","open source"]},
    {"name":"Adobe Audition","category":"Audio","pricing":"paid","type":"Paid subscription","description":"Professional audio editing, restoration and mixing.","url":"https://www.adobe.com/products/audition.html","icon":"Au","color":"purple","tags":["audio","adobe"]},
    {"name":"FL Studio","category":"Audio","pricing":"paid","type":"Paid license","description":"Digital audio workstation for music production.","url":"https://www.image-line.com/","icon":"♫","color":"orange","tags":["music","daw"]},
    {"name":"Ableton Live","category":"Audio","pricing":"paid","type":"Paid editions","description":"Music creation and performance software.","url":"https://www.ableton.com/live/","icon":"▥","color":"slate","tags":["music","daw"]},
    {"name":"Reaper","category":"Audio","pricing":"free","type":"Evaluation + paid license","description":"Fully featured evaluation; a paid license is required for continued licensed use.","url":"https://www.reaper.fm/","icon":"R","color":"green","tags":["music","daw"]},
    {"name":"Logic Pro","category":"Audio","pricing":"paid","type":"Paid license","description":"Apple's complete music production studio for Mac and iPad.","url":"https://www.apple.com/logic-pro/","icon":"♫","color":"blue","tags":["music","daw","apple"]},
    {"name":"OBS Studio","category":"Streaming & Capture","pricing":"free","type":"Free & open source","description":"Free software for live streaming and screen recording.","url":"https://obsproject.com/","icon":"◉","color":"slate","tags":["recording","streaming","free"]},
    {"name":"ShareX","category":"Streaming & Capture","pricing":"free","type":"Free & open source","description":"Screen capture, recording and productivity tool for Windows.","url":"https://getsharex.com/","icon":"⌗","color":"blue","tags":["screenshot","recording","free"]},
    {"name":"ScreenPal","category":"Streaming & Capture","pricing":"free","type":"Free + paid plans","description":"Screen recording and video messaging with free and paid options.","url":"https://screenpal.com/","icon":"▣","color":"pink","tags":["recording","screen"]},
]

@app.route("/")
def home():
    categories = ["All"] + sorted({tool["category"] for tool in TOOLS})
    return render_template("index.html", tools=TOOLS, categories=categories)

@app.route("/api/tools")
def api_tools():
    return jsonify(TOOLS)

if __name__ == "__main__":
    app.run(debug=True)
